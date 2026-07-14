# WPR AI Reporting Flow

Open-source instructions for turning WebPerformance Report deliveries into conversational digital intelligence using Claude and ChatGPT.

Turn your report history into digital intelligence.

WPR AI Reporting Flow is a conversational intelligence layer built on top of WebPerformance Report.

It allows users to interact with their historical reports using natural language and generate executive-ready insights across multiple dimensions:

* Performance
* Security
* Accessibility
* Analytics

Instead of manually reviewing reports one by one, users can ask questions, compare periods, benchmark websites, identify trends, and generate executive summaries using their complete reporting history.

---

## What is WPR AI Reporting Flow?

WPR AI Reporting Flow is not a chatbot.

It is not a dashboard with AI on top.

It is a specialized digital analyst that uses WebPerformance Report data as its source of truth.

By combining historical reports with Claude Projects, WPR AI Reporting Flow helps teams transform monitoring data into actionable intelligence.

Examples:

* Which of my websites has the biggest performance risk?
* Did my Core Web Vitals improve consistently during the last month?
* Which dimension requires immediate attention: performance, security, or accessibility?
* Generate an executive benchmark across all my monitored websites.
* What changed during the last reporting period?

---

## How It Works

1. Create a Claude Project.
2. Upload the WPR AI Reporting Flow instruction files.
3. Connect the inbox where WebPerformance Report deliveries are received.
4. Start asking questions.

Setup time is typically less than 5 minutes.

---

## Quick Start

1. Create a Claude Project.
2. Upload the following files:

   * `WPR_Claude_Instructions.md`
   * `WPR_Inbox_Workflow.md`
   * `WPR_Benchmark_One_Pager.md`
3. Set up your inbox (see Inbox Setup below).
4. Connect the inbox where WebPerformance Report deliveries are received.
5. Start asking questions about your websites.

Typical setup time: 5–10 minutes.

---

## Inbox Setup

For reliable retrieval, configure your inbox to automatically organize WebPerformance Report deliveries before connecting it to the Claude Project.

### Gmail

1. In Gmail, create a label named `WebPerformanceReport` (no spaces).
2. Create a filter:
   * **Subject contains**: `WebPerformance Report`
   * **Action**: Apply label `WebPerformanceReport` and skip the inbox (optional, keeps it organized).
3. Apply the filter to existing messages so historical reports are also labeled.

Once the label exists, WPR AI Reporting Flow will use it as the primary search scope, which is faster and more accurate than searching by subject alone.

**Post-Analysis Labeling (Optional but Highly Recommended)**

After analyzing a WebPerformance Report, you can request the Claude Project to apply the `WebPerformanceReport` label to mark it as processed. This keeps your inbox organized and prevents re-analyzing the same reports. Simply ask: "Label this report with WebPerformanceReport."

### Outlook / Microsoft 365

1. Create a folder named `WebPerformanceReport` in your mailbox.
2. Create a rule:
   * **Condition**: subject contains `WebPerformance Report`
   * **Action**: move the message to the `WebPerformanceReport` folder.
3. Run the rule on existing messages to include historical reports.

Alternatively, create a category named `WebPerformanceReport` and assign it via rule if you prefer to keep messages in your main inbox.

**Post-Analysis Labeling (Optional but Highly Recommended)**

After analyzing a WebPerformance Report, you can request the Claude Project to apply the `WebPerformanceReport` category or move it to the folder to mark it as processed. This keeps your inbox organized and prevents re-analyzing the same reports. Simply ask: "Label this report with WebPerformanceReport."

---

## Conceptual Architecture

```text
WebPerformance Report
        ↓
   Report Deliveries
        ↓
        Inbox
        ↓
   Claude Project
        ↓
     WPR AI Reporting Flow
        ↓
 Executive Insights
        ↓
    Decisions
```

WPR AI Reporting Flow does not replace WebPerformance Report.

It extends the value of historical reports by transforming them into conversational digital intelligence. Users can analyze trends, compare websites, generate executive benchmarks, and uncover insights across Performance, Security, Accessibility, and Analytics through natural language interactions.

---

## Requirements

### Claude

A Claude account with Project support.

### WebPerformance Report

At least one active WebPerformance Report.

The more report history available, the more valuable the analysis becomes.

---

## Supported Report Types

Current:

* Performance Reports
* Security Reports
* Accessibility Reports
* Analytics Reports

Planned:

* Search Console Reports
* Ecommerce Reports
* Sustainability Reports
* SEO Reports
* Additional WPR report types

---

## Example Questions

### Performance

* Which website improved the most during the last 30 days?
* Show performance trends across all monitored websites.
* Identify recurring performance issues.

### Security

* Has my security posture improved over time?
* Which websites have the highest security risk?
* Show security trends across reporting periods.

### Accessibility

* Which websites have the highest accessibility risk?
* Compare accessibility results across all monitored websites.
* Identify recurring accessibility issues.

### Analytics

* Which website shows the strongest engagement trends?
* Compare analytics performance across reporting periods.
* Generate a high-level analytics summary.

### Executive Insights

* Generate an executive benchmark of all monitored websites.
* Rank my websites by overall digital health.
* Create a board-ready summary for leadership.
* Identify the most urgent issues across all dimensions.

---

## Why WPR AI Reporting Flow?

Most monitoring platforms focus on collecting data.

WPR AI Reporting Flow focuses on understanding data.

It combines:

* Historical reports
* Contextual analysis
* Industry standards
* Executive-oriented communication
* Natural language interaction

to help organizations move from observation to action.

---

## Who Is It For?

* Digital Managers
* Ecommerce Teams
* Product Managers
* Engineering Leaders
* Marketing Teams
* Consultants
* C-Level Executives

Anyone who needs evidence-based decisions without manually reviewing dashboards and technical reports.

---

## Relationship with WebPerformance Report

WPR AI Reporting Flow depends on WebPerformance Report.

It uses the reports generated and delivered by WPR as its source of truth.

Without report history, there is no historical intelligence.

Without context, there are no meaningful insights.

WPR AI Reporting Flow extends WebPerformance Report from automated reporting into conversational digital intelligence.

---

## About WebPerformance Report

WebPerformance Report is the first Report Engine designed to transform technical data into clear, actionable reports delivered automatically to the right people.

Its mission is to create a global culture of digital performance by making performance, security, accessibility, analytics, and future digital dimensions easier to understand and act upon.

Reports. Decisions. Results.

https://www.webperformancereport.com

---

## License

MIT License
