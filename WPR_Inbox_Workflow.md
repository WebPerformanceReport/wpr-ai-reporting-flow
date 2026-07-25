# WPR_Inbox_Workflow.md

Authority for **retrieval**: finding, validating, and selecting WebPerformance Report deliveries from a connected inbox with the fewest calls and the least loaded content. Analysis is governed by `WPR_AI_Assistant_Instructions.md`.

---

# 1. Retrieval Contract

Every retrieval follows this sequence, without exception:

```text
Search summaries
→ Validate subjects internally
→ Select only the deliveries needed
→ Retrieve bodies only for the selected deliveries
→ Extract only the metrics the request needs
→ Analyze
```

Never do this:

```text
Search everything → read all bodies → decide later what mattered
```

Four rules govern it: subject is the universal baseline, so every inbox works unconfigured and a label, folder, or category is only ever an optimization; summaries come before bodies; pagination stops the moment the goal is met; and retrieval mechanics stay invisible outside Verification Mode.

---

# 2. Connector Detection

Email access is named differently per platform (integration, connector, connected app, app, Gmail connection, Outlook connection). Detect the underlying provider, apply its query syntax, and never name it in a response.

**Default: Gmail.** Apply Gmail rules (Section 6) unless one of these is true, in which case apply Outlook rules (Section 7):

- The user says they use Outlook, Microsoft 365, or a Microsoft inbox.
- The available integration is identified as Microsoft Graph or Outlook.
- A Gmail-syntax search errors and the user confirms Outlook.

Keep the detected provider for the whole session unless the user changes it.

---

# 3. Fast Path (default mode)

Use Fast Path for every clear, unambiguous request. It requires no confirmation before reading valid report bodies.

1. Infer the report category (Performance, Security, Accessibility, Analytics, or several).
2. Infer the time range or number of deliveries requested.
3. Capture any stated website, period, device, report type, or metric.
4. Build the narrowest search the request supports (Section 6 or 7).
5. Retrieve **summaries only** (subject, received date, internal identifier, snippet).
6. Request only enough summaries to satisfy the goal plus a small validation buffer: **N + 2, minimum 3**.
7. Normalize and validate subjects internally (Section 5).
8. Select the valid deliveries the analysis actually needs.
9. Retrieve full bodies **only** for those selected deliveries.
10. Extract only the metrics the question requires (`WPR_AI_Assistant_Instructions.md` Section 4).
11. Stop retrieving as soon as the request can be answered reliably.
12. Present the analysis directly, with no account of how it was retrieved.

In Fast Path: do not list subjects, do not show queries, do not ask for confirmation, do not report internal skips of invalid results.

### Worked patterns

| Request | Search scope | Summaries | Bodies | Stop condition |
|---|---|---|---|---|
| "Analyze my latest performance report." | WebPageTest only | up to 3 | 1 (newest valid) | 1 valid delivery selected |
| "Compare my last five security reports." | HTTP Observatory only | about 7 | the 5 selected | 5 valid deliveries selected |
| "Did my LCP improve vs last week?" | WebPageTest, last ~2 periods | up to 4 | the 2 selected | 2 comparable deliveries selected |
| "Accessibility trend, last month." | Wave, last 30–35 days | enough to cover the window | those in the window | window fully covered |
| "Executive overview." | one query per category | up to 3 per category | newest valid per category | newest valid found per category |

---

# 4. Verification Mode

Enter Verification Mode **only** when one of these applies:

- The user asks to see which reports were found, or to verify the search.
- Results are missing, duplicated, inconsistent, or ambiguous.
- Subject validation fails for results that should have matched.
- The requested reporting period looks incomplete (a gap in the sequence).
- Fast Path cannot resolve the request confidently.
- The user requests a broad audit or a historical inventory.

In this mode the assistant may show the exact query, display normalized subjects, explain what was included or excluded and why, identify missing periods, paginate more broadly, and ask for confirmation when genuine ambiguity remains.

It is never the default, and a missing label, folder, or category never triggers it.

---

# 5. Subject Grammar and Validation

## 5.1 Official grammar

```text
WebPerformance Report <Period> #<N> | <Source>
```

- `<Period>`: `Day`, `Week`, or `Month`.
- `<N>`: numeric index.
- `<Source>`: source tool from the table below.

| Category | Source (subject suffix) |
|---|---|
| Performance | `WebPageTest` |
| Security | `HTTP Observatory` |
| Accessibility | `Wave` |
| Analytics | `GA4` |

A new report type is added by adding one row here; the grammar and the rest of this workflow stay unchanged. Treat an unrecognized source as valid only if the rest of the grammar matches, and flag it as a new type.

## 5.2 Normalization

Decode HTML entities before validating: `&#124;` to `|`, `&#39;` to `'`, and all others. Normalization is mandatory and always internal.

## 5.3 Validation behavior

- Subjects that do not match the grammar are excluded from analysis.
- **Fast Path**: exclude silently. Do not display subjects, counts of skipped items, or raw metadata.
- **Verification Mode**: show normalized subjects and explain exclusions.
- Before any comparison, sort selected deliveries by period type, then numeric index, then received date.

---

# 6. Gmail Query Strategy

Build the narrowest query the request supports. Combine only the filters the request justifies:

`label` (when it exists) · `subject` · source tool · `newer_than` / `older_than` · period number · website or report name when present · result count.

```text
subject:"WebPerformance Report" "WebPageTest"
subject:"WebPerformance Report" "HTTP Observatory" newer_than:30d
subject:"WebPerformance Report" "Wave" newer_than:30d
subject:"WebPerformance Report" "GA4" newer_than:35d
```

If the optional label exists, use it as a narrower scope:

```text
label:WebPerformanceReport "WebPageTest"
label:WebPerformanceReport "HTTP Observatory" newer_than:30d
```

The label is an optimization only: if it does not exist, run the subject query and continue. That is not an error and is never surfaced. Never retrieve all WPR emails and filter afterward when a narrower query exists.

---

# 7. Outlook / Microsoft 365 Query Strategy

Same principle, Graph filters. Combine the narrowest available of:

dedicated folder (when it exists) · category (when it exists) · subject contains `WebPerformance Report` · subject contains the source tool · `receivedDateTime` range · sort · result limit.

- Sort `receivedDateTime` descending whenever the user asks for recent deliveries, and apply a result limit equal to the Fast Path buffer.
- Apply a `receivedDateTime` range whenever the request states or implies a window.
- Prefer folder scope, then category scope, then subject scope. Only subject always works; a missing folder or category is not an error and is never surfaced.

---

# 8. Bounded Pagination

Never paginate through the whole inbox by default. Request another page **only** when:

- the required number of valid deliveries has not been reached;
- the requested date window is not yet fully covered;
- duplicates or invalid subjects reduced the usable count below the goal;
- the user explicitly asked for a complete historical audit.

Stop immediately once the goal is satisfied:

| Goal | Stop at |
|---|---|
| Latest report | 1 valid delivery selected |
| Last N reports | N valid deliveries selected |
| Date window | oldest result older than the window start |
| Executive overview | newest valid delivery found per requested category |
| Benchmark One Pager | one valid delivery per site and dimension for the requested week |
| Complete audit | audit scope covered |

If a goal cannot be met after a reasonable number of pages, stop, analyze what is available, and state the gap plainly (`WPR_AI_Assistant_Instructions.md` Section 8).

---

# 9. Error Recovery

Apply in order, silently, and only as far as needed:

1. **Widen one step**: drop the narrowest filter (label or folder, then source tool, then date range) and repeat.
2. **Fall back to the subject baseline**: `WebPerformance Report`, unrestricted by label, folder, or category.
3. **Re-normalize** subjects and revalidate before concluding that nothing matched.
4. **Extend pagination** by one bounded step if results were truncated.
5. **Report the outcome, not the attempts**: "No Security report is available for Week #15."

Repeated failure or genuinely ambiguous results promote the request to Verification Mode.

---

# 10. Scope and Safety

Read-only, WebPerformance Report deliveries only. Never send, draft, modify, delete, or label email, and never read unrelated inbox messages. Full behavior rules: `WPR_AI_Assistant_Instructions.md` Sections 8 and 9.

---

# 11. File Responsibilities

**This file** owns connector detection, retrieval modes, subject grammar and validation, query strategy, optional label or folder usage, pagination, body selection, and error recovery.

**`WPR_AI_Assistant_Instructions.md`** owns identity, report categories, metric extraction, interpretation, comparison, visualization, output structure, recommendations, behavior, and safety.

Cross-reference. Never restate the other file's rules.

---

*End of WPR_Inbox_Workflow.md*
