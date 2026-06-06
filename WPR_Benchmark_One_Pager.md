# WPR Benchmark One Pager

This instruction generates a HTML "Benchmark" report comparing multiple websites across one, two, three, or four dimensions (Performance, Security, Accessibility, Analytics). It is flexible: the client, sites, dimensions, week, and output language all change per request; the editorial criteria and visual system stay constant.

This instruction complements `WPR_Claude_Instructions.md` and `WPR_Inbox_Workflow.md`. When this instruction is active, its specific flow takes precedence; when it is not active, the other project files govern Claude's behavior.

---

## 1. When to activate this instruction

Activate this template when the user requests any of the following:

- "Make me the benchmark for [client]"
- "Generate the one pager for [client] week #N"
- "Compare the sites of [client] in [dimension(s)]"
- "Multidimensional benchmark of [client]"
- Any variant that combines: comparison of multiple sites + one or more WPR dimensions + HTML editorial format.

Do not activate it for: single-site analyses, single-dimension deep-dives without site comparison, or generic reports that do not involve cross-site comparison. For those cases, follow the general project instructions.

If in doubt about applicability, ask before proceeding.

---

## 2. Required inputs before starting

Before extracting data or generating HTML, make sure you have these six inputs. If any are missing, ask the user in a single consolidated question:

1. **Client**: commercial name of the group or company (e.g., "Anthropic"). Include legal name if relevant.
2. **Sites**: list of URLs to compare, ideally between 3 and 6. If fewer than 3, warn that the format does not work well with so few sites and propose adjustments. If more than 6, warn that the matrix becomes illegible and propose prioritizing.
3. **Reporting week**: week number (e.g., "Week 20") and year (e.g., "2026").
4. **Dimensions to include**: any combination of `performance`, `security`, `accessibility`, `analytics`. The user can request 1, 2, 3, or all 4. This is the critical input that determines the report structure. Do not assume; if the user did not specify, ask.
5. **Target audience**: one of: "non-technical C-level", "mixed executive committee", "technical team", "public communication". Default to non-technical C-level if not specified.
6. **Output language**: English, Spanish, or other. Default to English if not specified.

Do not ask for all of these if the user has already implied them in the message. For example, "Make me the benchmark for Anthropic week 21, only security, in English" already gives client, week, dimensions (1), and language. You only confirm and proceed.

---

## 3. Data pipeline

### 3.1 Extraction from WebPerformance Report

Follow the rules of `WPR_Inbox_Workflow.md` for retrieval. Specifically:

- For each site and each requested dimension, search for the corresponding report for the indicated week using the subject pattern.
- Expected total: `number_of_sites × number_of_dimensions` reports.
- If a report is missing, do NOT fabricate data. Flag the absence both in the report content and in the methodology note.

### 3.2 CrUX vs Lab handling

This is an important editorial decision:

- **Use CrUX (field data) as the primary source** for LCP, INP, CLS, and TTFB across all visible sections of the report. CrUX reflects real user experience over the last 28 days.
- **If a site does not have CrUX data in WebPageTest**, before assuming no data exists, verify with PageSpeed Insights, which sometimes performs automatic origin-level fallback. If the user confirms PSI data, use it.
- **Do not use lab as primary data even though it is more dramatic**. Lab can be noisy, depends on specific test conditions (typically São Paulo + 3G Fast in WebPageTest), and may not represent real users. Using lab as primary data can damage the credibility of the report.
- **Lab remains available as a methodology note** for analyzing worst-case scenarios or validating early warnings, but does not enter the main body of the report unless the user explicitly requests it.

### 3.3 Missing report handling

If a site has no data for a dimension (for example, the WAVE report for docs.anthropic.com did not arrive), do not fill with data from the previous week. Mark the cell as "Pending" in the consolidated matrix and omit that site from the corresponding deep-dive with a short note.

---

## 4. Dimensional logic (1, 2, 3, or 4 dimensions)

The number of dimensions requested by the user changes the structure of several sections. The rules below apply by case.

### 4.1 Document title

The title adapts to the included dimensions:

- **4 dimensions**: "Multidimensional Benchmark" (or "Benchmark Multidimensional" in Spanish).
- **3 dimensions**: "Multidimensional Benchmark" (or "Benchmark Multidimensional" in Spanish).
- **2 dimensions**: "Benchmark of [dimension 1] and [dimension 2]" (e.g., "Benchmark of Performance and Security"). Order: Performance > Security > Accessibility > Analytics.
- **1 dimension**: "Benchmark of [dimension]" (e.g., "Benchmark of Analytics").

The hero badge follows the same logic.

### 4.2 Hero KPIs

Three KPI cards in all cases. The source changes:

- **4 dimensions**: choose the 3 strongest stories across the four dimensions. Do not force one per dimension; pick those with the clearest executive impact.
- **3 dimensions**: one KPI per dimension. Each KPI is chosen by the strongest story in its dimension.
- **2 dimensions**: distribute the three KPIs between the two dimensions. Typically two from one dimension and one from the other, depending on which story is stronger. Avoid having one KPI from each dimension plus a generic third one.
- **1 dimension**: all three KPIs come from that dimension. They must be distinct (do not repeat the same metric in three forms). Suggested types: one of magnitude ("X out of Y sites fail"), one of distribution ("range from F to B"), one of severity ("the most exposed site has Z").

### 4.3 Consolidated matrix

The matrix changes shape:

- **4 dimensions**: 6 columns (site | performance | security | accessibility | analytics | ranking).
- **3 dimensions**: 5 columns (site | performance | security | accessibility | ranking).
- **2 dimensions**: 4 columns (site | dimension 1 | dimension 2 | ranking).
- **1 dimension**: the matrix loses its name as "matrix" and becomes a simplified ranking table. 3 columns (site | dimension | rank), with the eyebrow renamed to "Ranking" instead of "Consolidated matrix". The title also changes (suggested: "Where each site stands" or similar).

### 4.4 Consolidated ranking

- **4 dimensions**: equal weighting across the four dimensions, normalized score (0-100) per dimension, simple average. This is the default. The user may explicitly override the weighting.
- **3 dimensions**: equal weighting across the three dimensions, normalized score (0-100) per dimension, simple average. This is the default. The user may explicitly override the weighting.
- **2 dimensions**: equal weighting between the two dimensions by default. If the user requests another weighting, apply it and mention it in the matrix subtitle.
- **1 dimension**: direct ranking by that dimension's metric. No weighting required.

In case of ties, prioritize the site with lower variance between dimensions (more balanced). For single-dimension, ties are broken by the secondary metric of that dimension.

### 4.5 Deep-dives

One deep-dive per included dimension, in mandatory order: Performance → Security → Accessibility → Analytics.

- **4 dimensions**: four deep-dive sections, labeled "Dimension 1 of 4", "Dimension 2 of 4", "Dimension 3 of 4", "Dimension 4 of 4".
- **3 dimensions**: three deep-dive sections, labeled "Dimension 1 of 3", "Dimension 2 of 3", "Dimension 3 of 3".
- **2 dimensions**: two deep-dive sections, labeled "Dimension 1 of 2", "Dimension 2 of 2".
- **1 dimension**: one deep-dive section, but the eyebrow changes to "Detailed analysis" (or equivalent) instead of "Dimension 1 of 1", which sounds redundant.

### 4.6 Recommendations

- **4 dimensions**: between 4 and 6 recommendations, prioritized by consolidated impact across all four dimensions.
- **3 dimensions**: between 3 and 5 recommendations, prioritized by consolidated impact across all three dimensions.
- **2 dimensions**: between 3 and 4 recommendations, prioritized by consolidated impact across both dimensions.
- **1 dimension**: between 2 and 4 recommendations, all focused on the single dimension. The cards' tags drop the dimension tag (it would be redundant) and keep only the affected site tag.

In all cases, the first recommendation is always the most urgent failure of the portfolio, regardless of which site it belongs to.

---

## 5. Fixed document structure

The HTML report has these sections, in this exact order. Do not change the order. Skip sections only as indicated.

### 5.1 Top navigation

Sticky bar at the top with: brand "WebPerformance.Report" (the period in accent color), and on the right "Week N · Month Year" in mono typeface.

### 5.2 Hero (cover)

- Badge with the report title (per section 4.1).
- Large title in two lines: "Digital portfolio" / "[Client]" (client in italic accent color).
- Subtitle of 1-2 sentences synthesizing the scope. The subtitle mentions explicitly which dimensions are included.
- Strip of cards with one site per column: name + URL.
- Three KPI cards (per section 4.2).

### 5.3 Consolidated matrix or ranking table

Per section 4.3. Includes:
- Eyebrow ("Consolidated matrix" for N≥2, "Ranking" for N=1).
- Title with last word in italic accent.
- Subtitle that mentions the weighting used (or absence of weighting for N=1).
- The matrix/table itself.
- Color legend at the foot.
- "Key finding" card after the matrix: 1-2 sentences with the strongest conclusion. It is the thesis of the report.

### 5.4 Deep-dives (one per included dimension)

Each deep-dive has the same internal structure:

**5.4.1 Section header**
- Eyebrow (per section 4.5).
- Large title with key word in italic accent.
- Short subtitle.

**5.4.2 Plain-language introductory block**
- Card with large icon on the left.
- Title "What this dimension measures and why it matters".
- Two paragraphs: the first explains what is being measured in non-technical terms. The second explains why it matters for the specific client (their business, their users).

**5.4.3 Per-site summary cards**
- One card per site, with the most important data point of the dimension in large type.
- Performance: LCP from CrUX.
- Security: grade + score.
- Accessibility: total number of errors.
- Analytics: Engagement Rate (GA4).

**5.4.4 Main visualization**
- Performance: horizontal bars per metric (LCP, INP, CLS, TTFB, weight). One bar per site within each metric. Include Google thresholds as visual references.
- Security: control matrix (rows = controls, columns = sites), with pass/partial/fail marks.
- Accessibility: stacked bars per site, segmented by error category (contrast, missing alt images, forms, structure).
- Analytics: grouped bars per site showing Sessions, Engagement Rate, and Average Engagement Time. Include a secondary indicator for Bounce Rate where available.

**5.4.5 "What is being left on the table" closing card**

This card has three visual elements:
- Header with eyebrow "What is being left on the table", dimension-adapted title, subtitle.
- Industry reference band: quantified range attributed to a recognized public source. See section 6.4 for valid sources.
- Per-site blocks: one block per site with its particular effect. Each block has a colored dot (good/warn/bad), the site name, and a 2-4 line paragraph that connects the technical data with the business impact specific to that site.

### 5.5 Prioritized recommendations

- Eyebrow "Action plan".
- Title and subtitle adapted to the number of recommendations (per section 4.6).
- Cards with: large number (01, 02...), tags (dimension + affected site(s)), actionable title, 2-4 line description, estimated effort and timeline, impact indicator on the right (Critical/High/Medium).

### 5.6 Methodology

- Eyebrow "About this report".
- Title "How we measured it" with italic accent on the last word.
- Grid of 4 blocks in two columns: Sources and tools, Test conditions, Classification thresholds, Report coverage.
- **Mandatory final note** about the nature of the data: "This report uses field data (Chrome User Experience Report) reflecting the average experience of returning users over the last 28 days. Laboratory data, simulating the worst case of a first visit on poor connection, is available on request to analyze specific acquisition scenarios or validate early warnings."

### 5.7 Footer

One line: "Generated by WebPerformance Report · Benchmark data week N of year · Internal document of [Client]".

---

## 6. Editorial criteria

These decisions always apply, unless the user explicitly instructs otherwise.

### 6.1 Data and honesty

- **Never fabricate client-specific figures** (traffic volume, conversion, revenue, validated demographic segments). If the client did not provide them, do not use them.
- If you need demographic or behavioral data to support a narrative, use reasonable assumptions for the type of business (traditional retail, financial, etc.) and clearly mark them as assumptions, not facts.
- If a technical data point is missing, say it is missing. Never fill it in.

### 6.2 Language and tone

These style rules apply **independent of output language**:

- Plain language before jargon. If you must use technical terms (LCP, INP, CSP, WCAG), explain them on first appearance.
- **No em-dashes (—)**. Use commas, periods, or parentheses.
- **No emojis** in the body of the report (visual dimension icons are allowed as design elements).
- Direct voice. First person plural sparingly; avoid overuse of "we".
- Short sentences. If a sentence exceeds 30 words, split it.
- Zero catastrophism. Instead of "they are losing millions", use attributed ranges.

**Technical terms remain in English** regardless of output language, because they are industry-standard nomenclature: LCP, INP, CLS, TTFB, CSP, HSTS, SRI, WCAG, ARIA, CrUX, etc. Their explanation can be in the output language, but the term itself is not translated.

### 6.3 Ranking and matrix

Follow the rules in section 4.4. Document the weighting used in the matrix subtitle so the reader can see it transparently.

### 6.4 Impact cards: quantification and differentiation

**Industry layer (quantified reference)**: use ranges attributed to recognized public sources. Approved sources:
- Google (for Core Web Vitals, conversion, and bounce rate).
- Akamai (for load times and conversion impact).
- Deloitte (for commercial impact of performance).
- IBM Cost of a Data Breach Report (for security).
- Edelman Trust Barometer (for consumer trust).
- WebAIM (for accessibility and population affected).
- Click-Away Pound (for commercial impact of accessibility).

If a source outside this list is needed, validate it is (a) public, (b) industry-recognized, (c) with documented methodology. Attribute it explicitly.

**Qualitative layer (per-site effects)**: for each site, differentiate the impact according to the business type and the typical customer. Use four possible mechanisms:
- Quality signaling and brand perception.
- Friction in the omnichannel journey.
- Reputational cost of security failures.
- Silent exclusion from accessibility issues.

Do not use all four every time. Choose those that apply to the specific site.

### 6.5 Tone differentiation per site

For each site, adjust the language to its profile. If the client provides context, use it. If not, reasonably infer from the business type (traditional retail, financial, hardware store, etc.) and mark assumptions as such.

---

## 7. Visual system

The HTML must be self-contained (a single file, no external dependencies except Google Fonts). Maintain a consistent visual system across all reports generated by this instruction.

### 7.1 Palette

- Base background: `#0B0E1A` (deep blue-black).
- Elevated background: `#131729`.
- Card background: `#1A1F36`.
- Primary text: `#F4F1EA`.
- Muted text: `#8C92A8`.
- Dim text: `#5A6080`.
- Primary accent: `#FF6B35` (orange).
- Good: `#4ADE80` (green).
- Warn: `#FBBF24` (amber).
- Bad: `#F87171` (red).
- Info: `#60A5FA` (blue).
- Borders: `rgba(255,255,255,0.08)`.

### 7.2 Typography

- Display (large headlines): Fraunces, weight 300-500, letter-spacing -0.02em to -0.04em.
- Sans (body and data): Inter, weight 300-700.
- Mono (metadata, technical numbers, eyebrows): JetBrains Mono.

All via Google Fonts. Import them in the `<head>`.

### 7.3 Spacing and composition

- Max wrapper: 1100px, lateral padding 32px (20px on mobile).
- Section vertical padding: 96px (more generous than a typical dashboard).
- Section separators: subtle border `1px solid rgba(255,255,255,0.08)`.
- Border radius: 12px for small cards, 16-20px for large containers.

### 7.4 Recurring components

- **KPI card**: large number in Fraunces 72px, small label below in Inter 14px muted, with a `<strong>` highlighting the key word.
- **Bar chart row**: 3-column grid (label 100px, bar flex, value 60px), bar with border-radius 100px, height 22px.
- **Stacked bar**: height 32px, border-radius 8px, segments with flex proportional to value.
- **Site impact block**: 2-column grid (140px name + 1fr text), name with colored dot (8px) on the left.

### 7.5 Responsive

- Mobile breakpoint: 880px.
- Below: KPIs in 2 columns, matrix collapses to one column, recommendation cards in one column.

---

## 8. Expected output

- **A single self-contained HTML file**.
- **Location**: `/mnt/user-data/outputs/`.
- **File name**: `benchmark_[client_slug]_[dimensions_slug]_week_[N].html`.
  - Client slug in lowercase, no diacritics, with underscores.
  - Dimensions slug: `perf_sec_a11y_ga4` for 4D, `perf_sec_a11y` / `perf_sec_ga4` / `perf_a11y_ga4` / `sec_a11y_ga4` for 3D, `perf_sec` / `perf_a11y` / `perf_ga4` / `sec_a11y` / `sec_ga4` / `a11y_ga4` for 2D, `perf` / `sec` / `a11y` / `ga4` for 1D.
  - Examples:
    - `benchmark_anthropic_perf_sec_a11y_ga4_week_20.html`
    - `benchmark_anthropic_perf_sec_a11y_week_20.html`
    - `benchmark_anthropic_ga4_week_25.html`
    - `benchmark_anthropic_perf_ga4_week_22.html`
- **After creation**: use the `present_files` tool to deliver to the user.
- **Accompanying message**: short. Summarize what the report shows, which findings are strongest, and ask if anything needs adjustment before closing. Do not explain the extraction process or mention the inbox connector (the opacity rules of `WPR_Claude_Instructions.md` apply).

---

## 9. Behavior during generation

- Work silently. Do not narrate intermediate steps to the user ("now I'm creating the styles", "now I'm extracting site data"). Deliver only the final result.
- If you must make an editorial decision not covered by this instruction, make it with judgment and briefly flag it in the final message so the user can validate it.
- If a data point is ambiguous, suspicious, or contradicts expectations, flag it in the final message. Do not hide it.
- The first version of the report is a starting point, not an end. Expect user iteration and keep the HTML structured so minor changes do not require redoing everything.

---

*End of instruction · WPR Benchmark One Pager · v2 (English, N-dimensional)*
