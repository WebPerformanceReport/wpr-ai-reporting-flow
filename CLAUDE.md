# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What This Repository Is

WPR AI Reporting Flow is a set of instruction files for creating conversational analysts on top of WebPerformance Report email deliveries. This repository contains instruction sets for multiple AI Assistant platforms (Claude, ChatGPT, etc.). There is no build system, runtime, or application code. Changes here are changes to AI Assistant project behavior.

---

## File Roles

| File | Role |
|---|---|
| `WPR_AI_Assistant_Instructions.md` | Primary AI Assistant Project instructions (Claude, ChatGPT, etc.). Defines identity, analysis pipeline, metrics, benchmarks, visualization rules, output structure, and behavior constraints. Always active. |
| `WPR_Inbox_Workflow.md` | Inbox retrieval mechanics for Gmail (default) and Outlook/Microsoft 365. Subject-first workflow, connector detection, validation patterns, pagination, and error recovery. |
| `WPR_Benchmark_One_Pager.md` | Activated only when the user requests a multi-site HTML benchmark. Overrides the general output format with a fixed HTML document structure. |

---

## Architecture

```
WebPerformance Report emails (Gmail or Outlook)
        ↓
  WPR_Inbox_Workflow.md          ← connector detection, retrieval, subject validation
        ↓
  WPR_AI_Assistant_Instructions.md     ← analysis pipeline, benchmarks, output format
        ↓
  WPR_Benchmark_One_Pager.md     ← activated for cross-site HTML reports
        ↓
  Executive insights (chat or HTML file)
```

### Report categories and their inbox subject suffixes

| Category | Subject suffix | Source tool |
|---|---|---|
| Performance | `\| WebPageTest` | WebPageTest |
| Security | `\| HTTP Observatory` | HTTP Observatory |
| Accessibility | `\| Wave` | WAVE |
| Analytics | `\| GA4` | Google Analytics 4 |

Valid subject patterns:
```
WebPerformance Report Day #X | <tool>
WebPerformance Report Week #X | <tool>
WebPerformance Report Month #X | <tool>
```

### Benchmark output

`WPR_Benchmark_One_Pager.md` instructs Claude to generate a **single self-contained HTML file** saved to `/mnt/user-data/outputs/`. File naming convention:
```
benchmark_[client_slug]_[dimensions_slug]_week_[N].html
```
Dimension slugs: `perf_sec_a11y_ga4` (4D), `perf_sec_a11y` / `perf_sec_ga4` / `perf_a11y_ga4` / `sec_a11y_ga4` (3D), `perf_sec` / `perf_a11y` / `perf_ga4` / `sec_a11y` / `sec_ga4` / `a11y_ga4` (2D), `perf` / `sec` / `a11y` / `ga4` (1D).

---

## Key Constraints Embedded in the Instructions

- **Clean response surface**: Do not expose implementation details (connector names, thread IDs, message IDs, retrieval steps) in user-facing responses. Reference data by report name, not by its inbox origin. The goal is an executive-grade UX, not raw plumbing.
- **No data fabrication**: if a metric is missing, say so. Never fill in absent values.
- **Output order for multi-category analysis**: Performance → Security → Accessibility → Analytics.
- **CrUX over lab data**: field data (Chrome User Experience Report) is the primary source for performance metrics. Lab data is only used on explicit request.
- **HTML visual system**: dark palette anchored to `#0B0E1A`, fonts Fraunces + Inter + JetBrains Mono via Google Fonts, max wrapper 1100px.
- **Benchmark default language**: English. Only changes if the user specifies otherwise.

---

## Editing Guidelines

- These are instruction files for a Claude Project, not source code. "Correctness" means behavioral accuracy, not compilation.
- When editing benchmarks in `WPR_AI_Assistant_Instructions.md` Section 5, verify against the official Google Core Web Vitals thresholds for the current year.
- When adding a new report type, update: `WPR_AI_Assistant_Instructions.md` (Section 2 table, Section 2 routing, Section 4 metrics), `WPR_Inbox_Workflow.md` (Step 4 patterns, Step 5 sort list, Gmail Pattern D, Outlook Pattern E, Section 6 step 5), and `WPR_Benchmark_One_Pager.md` (Section 2 dimensions input, Section 4 dimensional logic, Section 5.4.3–5.4.4, Section 8 slugs).
- The benchmark HTML visual system spec lives entirely in `WPR_Benchmark_One_Pager.md` Section 7. Palette, typography, and spacing are defined there; do not duplicate them elsewhere.
