# WPR Executive One Pager

This instruction generates an HTML Executive One Pager: one site, analyzed in depth, turned into a decision for leadership. It fills the template `WPR_Executive_One_Pager.html`. It complements `WPR_AI_Assistant_Instructions.md`, `WPR_Analysis_Reference.md` and `WPR_Inbox_Workflow.md`. When active, it governs the report: inputs, structure and output, plus the selection rules written here. Behavior, safety, voice and the clean response surface from `WPR_AI_Assistant_Instructions.md` still apply. Metric extraction, field and lab data, thresholds and impact sources come from `WPR_Analysis_Reference.md`, and retrieval from `WPR_Inbox_Workflow.md`; this file never overrides them.

---

## 1. When to activate

Activate when the user asks for an executive report, one pager or HTML analysis of **one site**. Examples:

- "Make the Executive One Pager for example.com."
- "Prepare a one pager for this prospect."
- "Show leadership how our site has evolved this quarter, as a one pager."

For several sites compared with each other, use `WPR_Benchmark_One_Pager.md`. If the request says "one pager" without saying whether it covers one site or several, ask.

---

## 2. Required inputs

Ask once, in a single consolidated question, only for what the request does not already give:

1. **Site**: the URL or domain.
2. **Company name**: as it should appear in the report.
3. **Dimensions**: any of Performance, Security, Accessibility. Default: every one of these with a delivery for the site. Analytics (GA4) and Search Console are not part of the Executive One Pager yet; linking them to diagnostic results is planned separately.
4. **Period**: the latest deliveries by default, or a period the user names.
5. **Theme**: WPR (default), Spotlight, or Site style (Section 6).
6. **Language**: English by default. If the user writes in another language and does not specify one, ask whether the report should be in that language or in English.
7. **Commissioned or independent**: whether the analyzed company asked for the report. Default: independent.
8. **Author and contact** (optional): the name and role for "Prepared by" and an email for questions about the method. Default author: WebPerformance Report. Without a contact email, delete the contact row; never invent one.

---

## 3. Data

- Retrieve deliveries following `WPR_Inbox_Workflow.md`: one site, grouped by test configuration. When the user names no period, use the **Trend** column of the default windows (last 3 days, 4 weeks or 3 months), so history can be detected. The cover and the summary still describe the latest delivery.
- Extract and classify following `WPR_Analysis_Reference.md`. WebPerformance Report deliveries are the only data source.
- **Mode**:
  - **Snapshot**: fewer than 3 comparable periods. Diagnosis, position and plan.
  - **History**: 3 or more comparable periods. Keep the `IF history` blocks: the change against the previous period on each KPI, the Evolution section and "What changed since the last report".
- **Headline metric per dimension**, used in the cover KPIs and in the summary:
  - Performance: LCP from field data. Without the CrUX section, say there is no field data and use lab values only with a visible lab label.
  - Security: the HTTP Observatory letter grade as reported, with the score (0 to 145).
  - Accessibility: WAVE total errors (Errors plus Contrast Errors).
- Never use Lighthouse scores or the WebPageTest `Security score` as headline metrics; they are not Security or Accessibility data.

---

## 4. Sections

Keep every section in the template order. Rules per section:

1. **Cover**: the headline states the business situation in one sentence, with the most important phrase in `{{headline_emphasis}}`. `{{script_line}}` is a short, positive closing phrase; it only shows in Spotlight. Three KPIs, one per dimension in canonical order (Performance, Security, Accessibility); with fewer dimensions, use the strongest distinct stories. Every KPI has a status word in its pill (Good, Needs Improvement, Poor, or the tier word from the reference).
2. **60-second summary**: 3 to 6 findings, most severe first. Each row: what was measured (value and context), what it means today in plain language, and what fixing it is worth, without inventing figures.
3. **Key message band**: one sentence that turns the findings into a call to act.
4. **Evolution** (history mode only): one trend card per headline metric, with the change described using the trend magnitude language. "What changed since the last report" lists each change with a status word: Fixed, Improved, Regressed or Unchanged.
5. **Market position**: compare the site with the industry baselines in `WPR_Analysis_Reference.md` Section 3 only, naming the source, the dataset and the year. Label single lab runs as such.
6. **Evidence**: one collapsible panel per dimension. Keep only the components that fit the dimension. Each panel closes with "What it means for {{company_name}}" and the evidence tags that apply.
7. **Plan**: actions in Now (next 2 weeks), Next (this quarter) and Then (ongoing), each with its dimension tag, its owner type, a "done when" and its effort or effect. Timing and effort are always "our assessment".
8. **Use it**: a message the reader can forward, 3 to 5 questions for their team, the public tests to verify each result (with the test links from the deliveries), and the data needed to put a business number on the findings.
9. **Who prepared this and methodology**: tool, location, device, test date and test ID per dimension; field or lab; derived figures; and the external sources with their year.

Small placeholders:

- `{{data_note}}` (under the cover buttons): the tools and test date behind the KPIs, for example "Public tests from WebPageTest, Mozilla HTTP Observatory and WebAIM WAVE, run on 25 Oct 2026."
- `{{independence_sentence}}`: the independence notice for an independent report, or "Prepared for {{company_name}}." for a commissioned one.
- `{{footer_note}}`: the same independence notice, or "Prepared for {{company_name}}" when commissioned.

---

## 5. Evidence and honesty

- Tag every claim with one of: **Measured** (from the deliveries), **Market benchmark** (public datasets), **External study** (published research, shows direction, not a forecast), **Our assessment** (professional judgment).
- Never estimate revenue, conversions or leads for the company without its own data. Say what data would be needed instead. Quantified impact from studies follows `WPR_Analysis_Reference.md` Section 3.
- Never fabricate a value. A missing dimension or metric is shown as unavailable and explained in the methodology.
- A cause, a prediction or a statement about intent is **Our assessment**, never **Measured**, and is worded as likely ("points to", "suggests"). Lab values in the title, the lede, headlines and bands are tied to the test: "in the latest test". Do not state infrastructure the deliveries do not show (for example "one server").
- Describe what changed only from the deliveries' counts and sizes. If a file count is unchanged, say "larger", not "new".
- A title that calls a period steady or stable must hold for every metric shown next to it.
- When a section of a delivery is missing, write "was not available in the test", never that the data does not exist.
- When a tool's own grade and a Core Web Vitals classification of the same metric seem to disagree (for example WebPageTest's First Byte Time A next to a TTFB Needs Improvement), say in one sentence that each uses its own scale.
- Source links follow `WPR_Analysis_Reference.md` Section 3.
- Test IDs and public test links from the deliveries may appear in the methodology and in "Use it". Inbox identifiers, addresses and retrieval details never appear.
- The methodology section is part of this format; the chat rule against a "Sources" block does not apply to the One Pager.

---

## 6. Theme

| Theme | Body class | What changes |
|---|---|---|
| **WPR** (default) | `theme-wpr` | Nothing: keep the theme block as it is |
| **Spotlight** | `theme-spotlight` | The base switches to alternating dark sections, accent bands and the script line |
| **Site style** | `theme-site` | The theme block takes the analyzed site's colors and, optionally, a Google Font close to its typeface |

Site style:

- Use colors or a style guide the user provides. If none is given and the platform has web access, take the main brand color and typeface from the site. Otherwise use the WPR theme and say so.
- Brand styling is presentation, not data. It never affects metrics or classifications.
- Every text pair must reach 4.5:1 contrast. If the brand color fails on white, keep it for `--accent` and `--band` (with a `--band-on` color that passes) and set `--accent-text` to a darker variant that passes.
- Use only the brand's colors and typeface. Never copy its logo, imagery or other brand marks.

Rules for every theme:

- The WPR logo motif stays on the cover. Only its color follows the theme.
- Status colors (Good, Needs Improvement, Poor) are fixed in the base and always come with a word.
- **The independence notice is mandatory whenever the analyzed company did not commission the report**, whatever the theme: "Independent analysis by WebPerformance Report. Not affiliated with or commissioned by {{company_name}}." A commissioned report shows "Prepared by WebPerformance Report for {{company_name}}." in the same place, so a Site style report never looks like the company's own document. The footer always credits WebPerformance Report.

---

## 7. Filling the template

- Read the whole template file before generating.
- Change only the theme block, the body class and the content placeholders. Do not edit the base CSS, the motif or the script.
- Copy each `REPEAT` block once per item. Keep `IF history` blocks only in history mode. Delete unused components inside the evidence panels.
- Compute bar widths and marker positions on one scale per chart, and keep every percentage between 0 and 100.
- Remove every `{{placeholder}}` and every template comment from the final report.
- `{{report_date}}` in the top bar is the date of the data (the test date or the period), never the date the report was generated.
- Before delivering, check the final file with code when the platform allows it: no `{{` or `}}`, no template comments, no em dash, and balanced HTML tags. Fix and check again if anything fails.
- Keep the result one self-contained HTML file.

---

## 8. Output

- **One self-contained HTML file**, delivered as a downloadable file with the platform's file output.
- **File name**: `one_pager_[site_slug]_[period_slug].html`, where the period slug is `week_[N]`, `month_[N]`, `day_[N]` or `date_[YYYY-MM-DD]`.
- **Accompanying message**: short. What the report shows, the strongest findings, and any assumption to validate. No retrieval details.

---

## 9. Review pass

Before delivering, go through these roles in order and fix what each finds. Do not narrate the review; flag in the final message only what the user must validate.

1. **Data reviewer**: every figure matches its delivery, each status matches its thresholds, a figure repeated in several places has one value, and every source is named with its year.
2. **Delivery manager**: every plan action has an owner type (for example the web, marketing, security or accessibility team), a measurable target and a "done when": which public test to rerun and what result counts. No action without them.
3. **Executive editor**: the 60-second test. A manager reading the summary and the key message knows what is wrong, what it is worth and what decision is being asked. One headline. Cut every sentence the reader can skip, and split any over 30 words.
4. **Art director**: a clear visual hierarchy, a number that leads each section, charts that tell the story, no color that means two things, readable labels and a layout that holds on a phone.

## 10. Behavior during generation

- Work silently. Do not narrate intermediate steps.
- If an editorial decision is not covered here, make it with judgment and flag it in the final message.
- If a data point is ambiguous or contradicts expectations, flag it in the final message.

---

*End of instruction · WPR Executive One Pager*
