# WPR Benchmark One Pager

This instruction generates a HTML "Benchmark" report comparing multiple websites across one or more dimensions (Performance, Security, Accessibility, Analytics). It fills the template `WPR_Benchmark_One_Pager.html`. The client, sites, dimensions, period, theme and output language change per request; the editorial criteria and the template stay constant.

This instruction complements `WPR_AI_Assistant_Instructions.md`, `WPR_Analysis_Reference.md` and `WPR_Inbox_Workflow.md`. When active, it governs the report: inputs, structure and output, plus the selection rules written here. Behavior, safety, voice and the clean response surface from `WPR_AI_Assistant_Instructions.md` still apply. Metric extraction, field and lab data, thresholds and impact sources come from `WPR_Analysis_Reference.md`, and retrieval from `WPR_Inbox_Workflow.md`; this file never overrides them.

---

## 1. When to activate this instruction

Activate this template when the user requests any of the following:

- "Make me the benchmark for [client]"
- "Generate the one pager for [client] week #N"
- "Quick benchmark of [sites] with their latest one-time reports"
- "Compare the sites of [client] in [dimension(s)]"
- "Multidimensional benchmark of [client]"
- Any variant that combines: comparison of multiple sites + one or more WPR dimensions + HTML editorial format.

Do not activate it for: single-site analyses, single-dimension deep-dives without site comparison, or generic reports that do not involve cross-site comparison. For those cases, follow the general project instructions.

If in doubt about applicability, ask before proceeding.

---

## 2. Required inputs before starting

Before extracting data or generating HTML, make sure you have these inputs. If any are missing, ask the user in a single consolidated question:

1. **Client**: commercial name of the group or company (e.g., "Anthropic"). Include legal name if relevant.
2. **Sites**: list of URLs to compare, ideally between 3 and 6. If fewer than 3, warn that the format does not work well with so few sites and propose adjustments. If more than 6, warn that the comparison table becomes illegible and propose prioritizing.
3. **Reporting period**: in recurring mode (default), the period type and number plus the year (e.g., "Week 20, 2026", "Month 10, 2026" or "Day 298, 2026"). In quick mode, a date or "latest" (Section 3.1). If the user names no period, identify the recurrence of the sites' deliveries (Day, Week or Month) and propose the latest complete period of that recurrence in the consolidated question.
4. **Dimensions to include**: any combination of the dimensions in Section 4 (`performance`, `security`, `accessibility`, `analytics`), one or more. This is the critical input that determines the report structure. Do not assume; if the user did not specify, ask.
5. **Target audience**: one of: "non-technical C-level", "mixed executive committee", "technical team", "public communication". Default to non-technical C-level if not specified.
6. **Output language**: English, Spanish, or other. Default to English if not specified. If the user writes in another language and does not specify one, ask in the consolidated question whether the report should be in that language or in English.
7. **Theme**: WPR (default), Spotlight, or Site style, following `WPR_Executive_One_Pager.md` Section 6.
8. **Commissioned or independent**: whether the client asked for the report. Assume commissioned only when every site belongs to the client. When the sites include other companies (for example a prospect and its competitors in quick mode) and the request does not say, ask in the consolidated question. The cover notice follows the case: own sites only, "Prepared by WebPerformance Report for [Client]."; with sites of other companies (for example competitors in quick mode), add that those companies are analyzed independently and did not commission or endorse the report; independent, the independence notice.

Do not ask for all of these if the user has already implied them in the message. For example, "Make me the benchmark for Anthropic week 21, only security, in English" already gives client, week, dimensions (1), and language. You only confirm and proceed.

---

## 3. Data pipeline

### 3.1 Extraction from WebPerformance Report

Follow the rules of `WPR_Inbox_Workflow.md` for retrieval. Specifically:

- For each site and each requested dimension, find the delivery for the requested period: filter by subject and period, then identify the site from the body header fields (`WPR_Inbox_Workflow.md` Section 5.4).
- Expected total: `number_of_sites × number_of_dimensions` reports.
- If a report is missing, do NOT fabricate data. Flag the absence both in the report content and in the methodology note.

**Two modes.**

- **Recurring** (default): the user names a period, such as `Week #43`, `Month #10` or `Day #298` of a year. The period defines which deliveries are comparable.
- **Quick**: the user asks for One Time Reports and gives a date or "latest", with no period. Useful for comparing a prospect with its competitors without waiting for recurring deliveries.

**Comparability.** For Performance, Security and Accessibility, each delivery is one test on its `Date:`.

- **Recurring mode**: a delivery belongs to the requested period when it has that period and number (same year), or when its test date falls inside that period (a One Time Report, or a delivery of another frequency, used for a site that has no delivery with that period and number). Deliveries that belong to the period are comparable. A `Month #N` benchmark can therefore combine tests up to a month apart; the methodology lists each test date.
- **Quick mode**: deliveries are comparable when no more than 7 days separate the earliest and the latest test date.
- **Analytics, in both modes**: deliveries are comparable only when their `Date range` covers the same dates.

A site whose delivery does not meet the rule is marked "Not comparable" in that dimension (Section 3.3).

### 3.2 CrUX vs Lab handling

Field and lab data follow the rule in `WPR_Analysis_Reference.md` Section 1.2. What is specific to the benchmark:

- **Field data is the source for LCP, INP, CLS, and TTFB in every visible section of the report.** Do not use lab as primary data even when it looks more dramatic. It can damage the credibility of the report.
- **If a site's WebPageTest delivery has no CrUX section**, show "No field data available" for its field metrics. Do not look for field data elsewhere: no PageSpeed Insights, no values supplied by the user. WebPerformance Report is the only data source. If the delivery has lab values that help the reader, show them with a visible "Lab" label, never as a substitute for field data. List the site in the "Report coverage" block of the methodology.
- **Lab remains available as a methodology note** for analyzing specific test scenarios or validating early warnings. It does not enter the main body of the report unless the user explicitly requests it or the site has no field data.

### 3.3 Missing report handling

If a site has no data for a dimension (for example, the WAVE report for docs.anthropic.com did not arrive), do not fill with data from the previous period. Mark the cell as "No data available" in the comparison table and omit that site from the corresponding deep-dive with a short note.

If a site has a delivery but it fails the comparability rule (Section 3.1), handle it the same way and mark the cell "Not comparable". Say why in the methodology, for example the test date.

---

## 4. Dimensional logic

The user can include any combination of the dimensions below. The rules in this section work for any number of them. Adding a dimension takes a row in this table, a visualization block in the template, and the rest of the checklist in `CLAUDE.md`.

| Dimension | Slug | Headline metric (comparison cell and site card) | Classified |
|---|---|---|---|
| Performance | `perf` | LCP from CrUX (Section 3.2) | Yes: Core Web Vitals |
| Security | `sec` | HTTP Observatory grade and score | Yes: official grading chart |
| Accessibility | `a11y` | Total WAVE errors (Errors plus Contrast Errors) | Yes: contextual interpretation |
| Analytics | `ga4` | Engagement Rate | No (`WPR_Analysis_Reference.md` Section 2) |

**Canonical order**: Performance, Security, Accessibility, Analytics. Titles, columns, deep-dives and slugs always follow it, whatever order the user used.

**No overall score or ranking.** The benchmark compares sites dimension by dimension. Do not normalize dimensions to a common scale, average them, or give sites an overall position. If the user asks for an overall ranking, explain that the benchmark compares each dimension on its own, and offer to order the sites by one dimension's headline metric instead.

### 4.1 Document title

- **One dimension**: "Benchmark of [dimension]" (e.g., "Benchmark of Security").
- **Two dimensions**: "Benchmark of [dimension 1] and [dimension 2]" (e.g., "Benchmark of Performance and Security").
- **Three or more**: "Multidimensional Benchmark" (or "Benchmark Multidimensional" in Spanish).

The hero badge follows the same logic.

### 4.2 Hero KPIs

Three KPI cards in all cases. Choose the three strongest stories across the included dimensions, by executive impact. Do not force one per dimension, and avoid one KPI per dimension plus a generic filler.

With one dimension, the three KPIs must be distinct (do not repeat the same metric in three forms). Suggested types: one of magnitude ("X out of Y sites fail"), one of distribution ("range from F to B"), one of severity ("the most exposed site has Z").

### 4.3 Comparison table

- **Columns**: site, then one column per included dimension in canonical order. No ranking column.
- **Cells**: the dimension's headline metric (table above), with its classification label when the dimension is classified. Analytics cells show the value and its trend, without a classification.
- **Missing data**: "No data available" (for Performance without CrUX, "No field data available", Section 3.2; for a delivery outside the comparability rule, "Not comparable", Section 3.3). Never show it as zero, and it does not affect the site's other cells.
- **Rows**: sites in the order the user gave them. Do not sort by an overall result.
- **One dimension**: add that dimension's secondary metrics as extra columns (e.g., INP and CLS for Performance), since there is room for them.

### 4.4 Deep-dives

One deep-dive per included dimension, in canonical order, as a collapsible panel inside the section "The evidence", labeled "Dimension X of N". With one dimension, use "Detailed analysis" (or equivalent) instead of "Dimension 1 of 1", which sounds redundant.

### 4.5 Plan actions

- **Count**: 2 to 4 actions with one dimension; otherwise between N and N + 2, where N is the number of included dimensions. The recurring check that closes the Ongoing column is not counted.
- **Horizon**: each action goes in Now (next 2 weeks), Next (this quarter) or Then (ongoing), as in `WPR_Executive_One_Pager.md` Section 4. The first action in Now is always the most urgent failure of the portfolio, regardless of which site it belongs to.
- **Tags**: each action carries the affected site tag and, when more than one dimension is included, its dimension tag.
- **Ongoing column**: it ends with the recurring check: re-run this benchmark with the next period's deliveries.
- Timing and effort are always "our assessment".

---

## 5. Fixed document structure

The HTML report has these sections, in this exact order. Do not change the order. Skip sections only as indicated.

The template `WPR_Benchmark_One_Pager.html` implements this structure. Section 7 explains how to fill it.

### 5.1 Top navigation

Sticky bar with the WebPerformance Report brand, the client and the period in one line: "Week N · Month Year" (or "Day N", "Month N") in recurring mode, the date in quick mode. On the right: links to Summary, Evidence and Plan, and the button "Use this benchmark".

### 5.2 Hero (cover)

- The cover notice for the case in input 8.
- Badge with the report title (per section 4.1).
- Large title in two lines: "Digital portfolio" / "[Client]" (client in accent color). The script line shows only in Spotlight.
- Subtitle of 1-2 sentences synthesizing the scope. The subtitle mentions explicitly which dimensions are included.
- Strip of cards with one site per column: name + URL.
- Three KPI cards (per section 4.2), each with a status word.
- Two buttons: "Read the 60-second summary" and "How to put it to work", with a short data note beside them: the tools and the test date or period behind the KPIs.

### 5.2a The 60-second summary and key message

- Eyebrow "The 60-second summary" and a title that states the situation of the portfolio.
- 3 to 6 findings, most severe first, in three columns: what we measured, what it means today, what fixing it is worth. Each finding names its site or sites and its dimension, so the reader can tell whose result it is. Do not invent figures for the third column.
- A findings table is not a ranking: do not name an overall winner or order findings by site.
- The key message band follows: one sentence with the strongest conclusion of the report (the thesis), with the button "How to use it".

### 5.3 Comparison table

Per section 4.3. Includes:
- Eyebrow "Comparison".
- Title with last word in accent color (suggested: "Where each site stands").
- Subtitle stating that sites are compared dimension by dimension, without an overall score.
- The table itself. Every classified cell shows the value and a status word.
- Legend at the foot.

### 5.3a Movement (history mode only)

When most sites have 3 or more comparable periods, each comparison cell adds its movement (for example "Improved, LCP -0.4 s") and a "Who improved and who slipped" section follows the table. Each entry has a status word: Improved, Slipped or Unchanged. Comparability follows Section 3.1 and `WPR_Inbox_Workflow.md` Section 3.

### 5.4 Deep-dives (one per included dimension)

Each deep-dive has the same internal structure:

**5.4.1 Panel header**

The section "The evidence" opens with an eyebrow, the title "The detail behind each dimension" and one line saying that each dimension opens to show the test results. Each panel's closed header shows:
- Eyebrow (per section 4.4).
- Title naming the dimension and its main story.
- Short subtitle.

The first panel starts open; the others start closed. A link to a panel's `id` (the dimension slug) opens it, and printing opens all of them. Everything below sits inside the panel body.

**5.4.2 Plain-language introductory block**
- Card with the dimension tag.
- Title "What this dimension measures and why it matters".
- Two paragraphs: the first explains what is being measured in non-technical terms. The second explains why it matters for the specific client (their business, their users).

**5.4.3 Per-site summary cards**
- One card per site, with the most important data point of the dimension in large type.
- Performance: LCP from CrUX. Without field data, "No field data available" (Section 3.2).
- Security: grade + score.
- Accessibility: total errors (Errors plus Contrast Errors, `WPR_Analysis_Reference.md` Section 1.2).
- Analytics: Engagement Rate (GA4).

**5.4.4 Main visualization**
- Performance: horizontal bars per metric (LCP, INP, CLS, TTFB, weight). One bar per site within each metric. Include Google thresholds as visual references.
- Security: control matrix (rows = controls, columns = sites), with pass/partial/fail marks.
- Accessibility: stacked bars per site, using the categories in `WPR_Analysis_Reference.md` Section 1.2: one segment for each of the three largest error types, one for "Other errors" when there are more, and one for Contrast Errors. A text breakdown under each bar lists every error type with its count. The segments add up to the total on the site card. Show Alerts separately, never stacked with errors. Do not chart Features, ARIA or Structural Elements as issues.
- Analytics: grouped bars per site showing Sessions, Engagement Rate, and Average Engagement Time. Include a secondary indicator for Bounce Rate where available.

**5.4.5 "What is being left on the table" closing card**

This card has three visual elements:
- Header with eyebrow "What is being left on the table", dimension-adapted title, subtitle.
- Industry reference band: quantified figure attributed to an approved source. See `WPR_Analysis_Reference.md` Section 3.
- Per-site blocks: one block per site with its particular effect. Each block has the site name, a status pill with its word, and a 2-4 line paragraph that connects the technical data with the business impact specific to that site, tagged "Our assessment".

**5.4.6 Evidence tags**

Each deep-dive ends with the evidence tags that apply to it (Section 6.7).

### 5.5 The plan

- Eyebrow "The plan", a title adapted to the number of actions (per section 4.5) and the line "Timing and effort are our assessment."
- Three columns: Now (next 2 weeks), Next (this quarter), Then (ongoing). Each action has its tags, its text and its effort or effect.

### 5.6 Put it to work

The section "Put it to work" turns the benchmark into something the reader can act on. The three steps (share, ask, check) are fixed. The rest follows the case in input 8:

- **Commissioned**: the title is "How to use this benchmark inside [Client]". The forward message and the questions are written for the client's teams (web, marketing, security, accessibility), and the data needs name the client's own owners.
- **Independent** (the compared companies did not commission it): the title is "How to use this benchmark". The reader is whoever compares or chooses between the sites, such as an analyst, a buyer or a team benchmarking itself. The forward message and the questions help them decide what to verify and ask; the data needs name each site's owner.

Content, in this order:
- A message the reader can forward (2 to 4 sentences, neutral, no accusation).
- 3 to 5 questions.
- The public tests that verify each included dimension, with the test links from the deliveries (Performance: WebPageTest, Security: Mozilla HTTP Observatory, Accessibility: WAVE, Analytics: no public test, name the GA4 property owner instead).
- The data needed to put a business number on the findings. The report never estimates revenue, conversions or leads without the owners' own data.

### 5.7 Who prepared this and methodology

- Eyebrow "Who prepared this", title "WebPerformance Report" and one sentence on what the benchmark does. Then the line "Prepared by WebPerformance Report." followed by the independence sentence for an independent report, or "Prepared for [Client]." for a commissioned one. No contact email.
- A collapsible "Methodology and sources" holds: a grid of 4 blocks in two columns (Sources and tools, Test conditions, Classification thresholds, Report coverage), the final note on performance data when Performance is included, and the list of external sources with year and link.
- Report coverage lists, per site and dimension, the delivery type (recurring or One Time) and the test date or `Date range` used, plus every "No data available" or "Not comparable" cell and why. If a delivery is left out of the report, say so and do not use it elsewhere in the report.
- **Final note on performance data**, only when Performance is among the dimensions (translated into the output language): "Performance figures use field data from the Chrome User Experience Report (CrUX): the 75th percentile of real Chrome user experiences over the 28 days ending about two days before each test, for the tested page and device. Lab data, from a single test visit under fixed conditions (location, device, connection), is available on request to analyze specific scenarios or validate early warnings."

### 5.8 Footer

One line: "Generated by WebPerformance Report · Benchmark data [period] · [footer note]", where [period] is, for example, "week 20 of 2026" or "as of 2026-09-27", and [footer note] is "Internal document of [Client]" for a commissioned benchmark or the independence notice for an independent one.

---

## 6. Editorial criteria

These decisions always apply, unless the user explicitly instructs otherwise.

### 6.1 Data and honesty

- **Never fabricate client-specific figures** (traffic volume, conversion, revenue, validated demographic segments). If the client did not provide them, do not use them.
- If you need demographic or behavioral data to support a narrative, use reasonable assumptions for the type of business (traditional retail, financial, etc.) and clearly mark them as assumptions, not facts.
- If a technical data point is missing, say it is missing. Never fill it in.
- Claims about causes, changes and steady periods follow the rules in `WPR_Executive_One_Pager.md` Section 5 (Our assessment for causes, "larger" not "new" when counts are unchanged, steady only if every metric shown is stable).

### 6.2 Language and tone

These style rules apply **independent of output language**:

- Plain language before jargon. If you must use technical terms (LCP, INP, CSP, WCAG), explain them on first appearance.
- **No em-dashes (—)**. Use commas, periods, or parentheses.
- **No emojis** in the body of the report (visual dimension icons are allowed as design elements).
- Direct voice. First person plural sparingly; avoid overuse of "we".
- Short sentences. If a sentence exceeds 30 words, split it.
- Zero catastrophism. Instead of "they are losing millions", use attributed ranges.

**Technical terms remain in English** regardless of output language, because they are industry-standard nomenclature: LCP, INP, CLS, TTFB, CSP, HSTS, SRI, WCAG, ARIA, CrUX, etc. Their explanation can be in the output language, but the term itself is not translated.

### 6.3 Comparison without ranking

Compare dimension by dimension (Section 4). Never name an overall winner or give sites an overall position. Within a deep-dive, charts may order sites by that dimension's metric.

### 6.4 Impact cards: quantification and differentiation

**Industry layer (quantified reference)**: use figures attributed to an approved source, following `WPR_Analysis_Reference.md` Section 3. In the HTML, the source is named on the band itself.

**Qualitative layer (per-site effects)**: for each site, differentiate the impact according to the business type and the typical customer. Use four possible mechanisms:
- Quality signaling and brand perception.
- Friction in the omnichannel journey.
- Reputational cost of security failures.
- Silent exclusion from accessibility issues.

Do not use all four every time. Choose those that apply to the specific site.

### 6.5 Tone differentiation per site

For each site, adjust the language to its profile. If the client provides context, use it. If not, reasonably infer from the business type (traditional retail, financial, hardware store, etc.) and mark assumptions as such.

### 6.6 Benchmark threshold rules

All benchmark classifications must follow the official thresholds defined in `WPR_Analysis_Reference.md` Section 2. Do not invent thresholds or create arbitrary Good / Needs Improvement / Poor classifications.

Apply thresholds in this hierarchy:

1. Official standard behind the metric (e.g., Google Core Web Vitals specification).
2. Official source tool classification (e.g., HTTP Observatory grading scale).
3. Clearly stated contextual interpretation.
4. No classification if no reliable threshold exists.

Dimension-specific notes:

- **Performance**: use the Core Web Vitals thresholds from `WPR_Analysis_Reference.md` Section 2. TTFB is a diagnostic metric, not one of the three Core Web Vitals (LCP, INP, CLS). Apply it as supporting context, not as a primary classification.
- **Security**: follow the HTTP Observatory grading scale from `WPR_Analysis_Reference.md` Section 2.
- **Accessibility**: follow WAVE findings and WCAG-based interpretation from `WPR_Analysis_Reference.md` Section 2.
- **Analytics**: do not classify. Follow the Analytics rule in `WPR_Analysis_Reference.md` Section 2.

If a threshold is unclear, missing, or not officially defined, state this limitation explicitly instead of forcing a rating.

### 6.7 Evidence tags and consistency

- Tag every claim with Measured, Market benchmark, External study or Our assessment, with the rules of `WPR_Executive_One_Pager.md` Section 5: causes, predictions and the effect on each site are Our assessment, worded as likely.
- A metric's status must agree with its thresholds in every place it appears. If any period in the history crossed a threshold, do not write that the metric "stayed Good" or "unchanged"; say that it left the range and came back.
- A delivery excluded from the report (for example a test with an evident irregularity) is excluded everywhere: comparisons, ranges and changes.
- An industry baseline for page weight or request counts comes from `WPR_Analysis_Reference.md` Section 3, one edition, naming the source and year. "Industry practice" without a source is not allowed.

---

## 7. Template and theme

The visual system lives in the shared One Pager base, built into `WPR_Benchmark_One_Pager.html`: palette, typography, spacing, components, accessibility (text contrast of at least 4.5:1, status always with a word) and print styles. Do not restate or override it.

- **Theme**: WPR, Spotlight or Site style, with the rules in `WPR_Executive_One_Pager.md` Section 6, including the fixed status colors and the independence notice. Site style uses the client's brand (the company that owns the portfolio or receives the report), never the brand of one of the compared sites.
- **Filling**: follow `WPR_Executive_One_Pager.md` Section 7. Read the whole template, change only the theme block, the body class and the placeholders, copy `REPEAT` blocks per item, keep `IF` blocks only when they apply, and remove every placeholder and template comment.
- **Main visualization**: in each dimension panel, keep only the visualization block that matches the dimension (Section 5.4.4) and delete the others. Page weight is lab only and never classified.
- **Analytics is never classified**: in the KPIs, comparison cells, site cards and left-on-the-table blocks, replace the status pill with the trend.
- **TTFB** is diagnostic context (Section 6.6), shown without a status pill.
- **Missing or not comparable data** shows its text ("No data available", "No field data available", "Not comparable") without a status pill.
- **Tones**: the summary is `tone-a` and the comparison is `tone-b`. Every section after it alternates, starting with `tone-a`: Movement when present, then the evidence section (its panels are not sections, so they carry no tone), the plan, "Put it to work" and "Who prepared this".
- **Use it and Who prepared this**: commissioned or independent follows input 8 (Section 5.6). Do not edit the script; the copy buttons work as they are.
- **Scales**: each chart uses one scale for every site, so bars and markers compare honestly. For Analytics, each metric shares one scale across the site cards. Every percentage stays between 0 and 100.

---

## 8. Expected output

- **A single self-contained HTML file**.
- **File name**: `benchmark_[client_slug]_[dimensions_slug]_[period_slug].html`.
  - Period slug: `day_[N]`, `week_[N]` or `month_[N]` in recurring mode; `date_[YYYY-MM-DD]` in quick mode.
  - Client slug in lowercase, no diacritics, with underscores.
  - Dimensions slug: the slugs of the included dimensions (Section 4), joined with underscores in canonical order. For example `perf_sec_a11y_ga4`, `perf_ga4` or `a11y`.
  - Examples:
    - `benchmark_anthropic_perf_sec_a11y_ga4_week_20.html`
    - `benchmark_anthropic_perf_sec_a11y_week_20.html`
    - `benchmark_anthropic_ga4_week_25.html`
    - `benchmark_anthropic_perf_ga4_week_22.html`
    - `benchmark_anthropic_perf_a11y_month_10.html`
    - `benchmark_anthropic_perf_sec_date_2026-09-27.html`
- **Delivery**: as a downloadable file with the platform's file output.
- **Accompanying message**: short. Summarize what the report shows, which findings are strongest, and ask if anything needs adjustment before closing. Do not explain the extraction process or mention the inbox connector (the opacity rules of `WPR_AI_Assistant_Instructions.md` apply).

---

## 9. Behavior during generation

- Work silently. Do not narrate intermediate steps to the user ("now I'm creating the styles", "now I'm extracting site data"). Deliver only the final result.
- If you must make an editorial decision not covered by this instruction, make it with judgment and briefly flag it in the final message so the user can validate it.
- If a data point is ambiguous, suspicious, or contradicts expectations, flag it in the final message. Do not hide it.
- The first version of the report is a starting point, not an end. Expect user iteration and keep the HTML structured so minor changes do not require redoing everything.

---

*End of instruction · WPR Benchmark One Pager · v4 (template-based)*
