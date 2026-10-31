# WPR_Analysis_Reference.md

Authority for **metric extraction, classification thresholds, business impact sources and visualization**. Consult it whenever you extract, classify, quantify or chart. Identity, voice, output structure and safety are governed by `WPR_AI_Assistant_Instructions.md`; retrieval by `WPR_Inbox_Workflow.md`.

---

## 1. Metric Extraction

Extraction is **targeted, not exhaustive**. Read the selected report bodies for what the request needs and nothing more. This is the single largest lever on context usage.

### 1.1 How much to extract

| Request | Extract |
|---|---|
| **Direct metric request** ("Did my LCP improve?") | That metric, its reporting period, and only the test context a valid comparison needs (device, location, connection). Nothing else. |
| **Single-report analysis** | The full metric set for that report type (Section 1.2). |
| **Multi-report comparison** | Only metrics that answer the question, exist across all selected reports, and compare reliably. |
| **Executive overview or benchmark** | The full metric set across each required category. |

On a direct metric request, do not pull unrelated metrics (CLS, INP, page size, request count, accessibility or security data). If the test context differs enough to invalidate the comparison, say so instead of comparing.

### 1.2 Full metric set by category

#### Performance (WebPageTest)
Core Web Vitals and loading: **LCP, INP, CLS, TTFB, Fully Loaded Time, Total Page Size, Number of Requests**. Plus test context: **Location, Device, Connection**, and top opportunities or risks flagged in the report.

**Field vs lab data.** This rule is the single authority for chat analyses and the benchmark. A WebPageTest delivery can hold two kinds of data:

- **Field data** is the `Core Web Vitals - CrUX Field Data` section: LCP, CLS, INP and TTFB from real Chrome users, at the 75th percentile over the last 28 days, for the tested URL and device. Report it with the delivery's test date (`Date:`). When the exact period matters, note that it covers the 28 days ending about 2 days before the test.
- **Lab data** comes from one test visit under fixed conditions (location and device in the `From:` header). It is the `Core Web Vitals - Lab Data` section (LCP, CLS, TBT) and the `Performance Results` section (First Byte, Start Render, FCP, Speed Index, Document Complete, Fully Loaded).

Apply these rules:

- LCP, INP, CLS and TTFB come from field data whenever the CrUX section is present.
- If the CrUX section is absent, the delivery has no field data. Say so. A missing section is not a regression or an improvement.
- Use lab values for those metrics only when the user asks for them, or when field data is absent. Always label them as lab results and give their test context.
- INP exists only as field data. Without the CrUX section, report INP as unavailable. Never substitute TBT or any other lab metric.
- TTFB is one metric with two sources: TTFB in the CrUX section is the field value; `First Byte` in Performance Results is the lab value.
- Fully Loaded Time, Total Page Size and Number of Requests (the Fully Loaded `Time`, `Bytes In` and `Requests`) are lab only. Present them as lab test results.
- Never compare a field value with a lab value, within one delivery or across periods. If one period has field data and the other only lab data, say that the periods cannot be compared on that metric.

A WebPageTest delivery also shows a `Security score` grade and Lighthouse scores (Performance, Accessibility, Best Practices, SEO). They are not Security or Accessibility data: Security comes only from HTTP Observatory deliveries, and Accessibility only from WAVE deliveries.

#### Security (HTTP Observatory)
**Grade and Score** (the score starts at 100 and ranges from 0 to 145 with bonuses; A+ is 100 or more; report it as a plain number, never as "out of 100"), **Header configuration, CSP, HSTS, TLS version, Mixed Content, High-level vulnerabilities**.

#### Accessibility (WAVE)
The delivery's `A11y Summary` has six counts. This is the single category list for chat analyses and the benchmark:

- **Issues**: **Errors** (with the item breakdown the delivery lists, such as `Empty form label` or `Empty link`), **Contrast Errors**, and **Alerts** (elements that may cause issues and need review).
- **Context, not issues**: **Features**, **ARIA** and **Structural Elements** count elements present on the page. Never present them as problems.

WAVE reports `Errors` and `Contrast Errors` separately. **Total errors** means Errors plus Contrast Errors; use it for classification (Section 2) and as the headline figure. Note which WCAG level is implicated when stated.

#### Analytics (GA4)
**Sessions, Users, Engaged Sessions, Engagement Rate, Bounce Rate, Average Engagement Time, Key Events (Conversions)**. Note the reporting period and any segments or filters applied in the report.

#### Future report types
Extract by structure and context. Flag explicitly that the report type is new so the user knows interpretation is provisional, and place it in the most relevant category if one clearly applies.

If a required metric is absent from the report, say so (`WPR_AI_Assistant_Instructions.md` Section 5).

---

## 2. Interpretation Benchmarks

Apply these thresholds to give metrics meaning. Classify Performance, Security and Accessibility metrics when reporting, using the tiers each block defines. Do not classify Analytics metrics (see Analytics below).

Each block names its source. Blocks marked **contextual interpretation** have no official source: present them as practical guidance, never as an official standard.

### Core Web Vitals (Google official, 2026)
These thresholds apply to field data at the 75th percentile (Section 1.2). When only lab data is available, say that the classification is based on a single lab test.

| Metric | Good | Needs Improvement | Poor |
|---|---|---|---|
| LCP | ≤ 2.5s | 2.5–4.0s | > 4.0s |
| INP | ≤ 200ms | 200–500ms | > 500ms |
| CLS | ≤ 0.1 | 0.1–0.25 | > 0.25 |
| TTFB | ≤ 800ms | 800ms–1.8s | > 1.8s |

### Page Weight (contextual interpretation, industry practice)
- Total Page Size: under 1.5 MB is lean, 1.5–3 MB is typical, over 3 MB is heavy.
- Number of Requests: under 50 is lean, 50–100 typical, over 100 heavy.

### HTTP Observatory Grades (official grading chart)
Classify by the letter grade the delivery reports. Never recompute the grade from the score.
- A+ / A / A- (score 85 or more): strong security posture.
- B+ / B / B- (score 65–84): acceptable, some hardening needed.
- C+ / C / C- (score 45–64): material gaps, address promptly.
- D+ / D / D- / F (score below 45): urgent remediation.

### WAVE Accessibility (contextual interpretation)
Automated testing finds only part of the WCAG issues, so a WAVE result never proves conformance. The bands apply to total errors (Errors plus Contrast Errors, Section 1.2).
- 0 errors: no errors detected by automated testing. Manual review is still needed to confirm WCAG conformance.
- 1–5 errors: minor, fix in next sprint.
- 6–19 errors: moderate, prioritize.
- 20 or more errors: severe, legal and UX exposure.

### Analytics (GA4)
No universal thresholds exist. Engagement Rate, Bounce Rate and session metrics vary widely by industry and site type. Do not classify them as Good / Needs Improvement / Poor. Interpret them by trend and context, unless the user provides a benchmark.

### Trend magnitude language
The magnitude word follows the relative change:
- Under 5%: **stable**.
- 5% to under 15%: **notable** improvement or regression.
- 15% to under 30%: **significant**.
- 30% or more: **major**.

- **Direction**: a lower LCP, INP, CLS, TTFB or error count is an improvement; a lower score or grade is a regression.
- **Rates** (Engagement Rate, Bounce Rate and other percentages): report the change in percentage points and apply the magnitude word to the relative change, stating both: "+5 pp, a notable 10% increase".
- **Small values in the best tier**: when a metric stays in its best tier in both periods (for example Good for Core Web Vitals), report the absolute change and never call it significant or major. CLS moving from 0.01 to 0.02 is +100% but still Good.

---

## 3. Quantifying Business Impact

Every quantified business impact (conversion, revenue, bounce, trust, cost) names its source. Without an approved source, describe the impact qualitatively. Never invent a figure or present an unattributed one.

**Approved sources for business impact:**
- Google (for Core Web Vitals, conversion, and bounce rate).
- Akamai (for load times and conversion impact).
- Deloitte (for commercial impact of performance).
- IBM Cost of a Data Breach Report (for security).
- Edelman Trust Barometer (for consumer trust).
- WebAIM (for accessibility and population affected).
- Click-Away Pound (for commercial impact of accessibility).
- web.dev Case Studies (web.dev/case-studies) and WPO Stats (wpostats.com) (for company-specific results of performance work).

Case studies describe one company's result, not an industry average. Cite the company, the figure, the source and the year, in this form: "[Company] saw [result] after [change] ([source], [year])." Never generalize a case into "typically lifts X%". Prefer the original study that WPO Stats links to, and prefer recent cases.

**Industry baselines:** HTTP Archive (httparchive.org), including the Web Almanac, shows the state of the web (median page weight, request counts, share of sites passing Core Web Vitals). The WebAIM Million (webaim.org/projects/million) shows accessibility errors on the top million home pages. Use them to compare a site with the web at large, never as evidence of business impact.

If another source is needed, use it only if it is (a) public, (b) industry-recognized, and (c) has a documented methodology. Attribute every source inline, by name, in the sentence that uses it. Do not add a sources section (`WPR_AI_Assistant_Instructions.md` Section 4).

---

## 4. Visualization Playbook

Charts are a first-class deliverable, and retrieval efficiency never reduces visual quality. Be proactive: when a modern chart improves comprehension, produce one. Default to visualizing when any of these apply:

1. **3 or more deliveries exist** for the same report type (trend line).
2. **Comparing metrics across websites, report types, devices, or business units** (grouped bars).
3. **A score has clear tiers** like HTTP Observatory or CWV thresholds (gauge or color-banded bar).
4. **Accessibility breakdown** across categories (horizontal bar or heatmap).
5. **Cross-category executive health overview** (composite or small-multiples view).

A chart is not required for a purely factual answer ("What was my latest LCP?") unless the user asks for one.

### Chart type by question
- **"How is my LCP trending?"** → line chart with Good/Needs Improvement/Poor threshold bands.
- **"Compare mobile vs desktop"** or **"compare my five websites"** → grouped bar chart.
- **"What's my current security posture?"** → gauge or color-banded score indicator.
- **"How has my security posture changed over time?"** → score trend line or before/after comparison.
- **"Where are my accessibility issues?"** → horizontal stacked bar by category.
- **"What changed since last week?"** → before/after comparison with delta annotations.
- **"Give me an executive overview"** → charts wherever they sharpen the synthesis.

For a cross-site HTML benchmark, `WPR_Benchmark_One_Pager.md` takes precedence and its full visual system applies unchanged.

### Delivery format
- **Interactive React artifact** (Recharts) when the user will explore multiple metrics, toggle series, or hover for detail.
- **Static SVG visual** when the chart is a single snapshot inside an executive summary.
- **Inline markdown table** when the data is small (3 or fewer rows and columns) and a chart would be overkill.

### Chart quality standards
- Always label axes and units.
- Include threshold bands (e.g., green/yellow/red for CWV) when benchmarks apply.
- Use a restrained palette: one color for current, muted gray for previous, red/amber/green only for classification.
- Annotate the most important data point (biggest change, current value).
- Title the chart as a conclusion, not a description. "LCP improved 35% in November" beats "LCP over time".

---

*End of WPR_Analysis_Reference.md*
