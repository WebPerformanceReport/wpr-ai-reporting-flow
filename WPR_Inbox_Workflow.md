# WPR_Inbox_Workflow.md

This file defines how to reliably retrieve, validate, and analyze WebPerformance Report deliveries from a connected inbox. It supports two connectors: **Gmail** (default) and **Outlook / Microsoft 365**. It complements `WPR_AI_Assistant_Instructions.md` and must be followed for all inbox interactions inside this Project.

The goal is to provide a structured workflow that avoids hallucinations, incomplete searches, missing reports, or misinterpretation of API responses, regardless of which email connector is active.

---

# 1. Core Principles

All inbox interactions must follow the WebPerformance Report Project logic, independent of connector:

1. Subject-first retrieval
2. Strict pattern validation
3. Folder or label priority
4. HTML subject normalization
5. Step-by-step confirmation
6. Safe and explicit search queries
7. Controlled multi-report analysis

The assistant must never infer or guess report content without confirming subjects first.

---

# 2. Connector Detection

The active connector determines which search syntax and pagination rules apply.

**Default connector: Gmail.**

If the user has not specified a connector, assume Gmail and proceed with Gmail rules (Section 4).

Switch to Outlook rules (Section 5) only when one of the following is true:
- The user explicitly says they use Outlook, Microsoft 365, or a Microsoft inbox.
- The connected integration is identified as Microsoft Graph or Outlook.
- A Gmail search returns an error and the user confirms they are on Outlook.

Once the connector is identified for a session, apply it consistently. Do not switch mid-session unless the user requests it.

---

# 3. Mandatory Retrieval Workflow

The following seven steps apply regardless of connector. Connector-specific syntax is in Sections 4 and 5.

## Step 1 — Search the inbox

Search using the folder, label, or category configured for WebPerformance Report deliveries. Apply the connector-specific syntax from Section 4 or 5.

If the primary filter returns an error, fall back to a subject-keyword search:
- Search for emails whose subject contains "WebPerformance Report".

---

## Step 2 — Retrieve subjects only (no analysis yet)

Extract for each result:
- subject
- date received
- message ID (if available)
- snippet

Do not read the full email body at this stage.

---

## Step 3 — Normalize subjects

Subjects returned by email APIs may contain encoded characters. Decode before validating:

- `&#124;` becomes `|`
- `&#39;` becomes `'`
- All other HTML entities must be decoded.

Normalization is mandatory before pattern validation.

---

## Step 4 — Validate subjects using official patterns

Only subjects that match the official WebPerformance Report patterns may proceed to analysis.

Valid patterns:

```
WebPerformance Report Day #X | WebPageTest
WebPerformance Report Day #X | HTTP Observatory
WebPerformance Report Day #X | Wave
WebPerformance Report Day #X | GA4

WebPerformance Report Week #X | WebPageTest
WebPerformance Report Week #X | HTTP Observatory
WebPerformance Report Week #X | Wave
WebPerformance Report Week #X | GA4

WebPerformance Report Month #X | WebPageTest
WebPerformance Report Month #X | HTTP Observatory
WebPerformance Report Month #X | Wave
WebPerformance Report Month #X | GA4
```

Subjects that do not match these patterns must be ignored.

---

## Step 5 — Sort and classify

Organize valid subjects by:
- Report type (WebPageTest, HTTP Observatory, Wave, GA4)
- Period (Day, Week, Month)
- Numeric index (ascending)

Sorting is required before any multi-report comparison.

---

## Step 6 — Retrieve full email content only after validation

Retrieve the full body only for subjects confirmed as valid WebPerformance Report deliveries.

---

## Step 7 — Extract metrics and analyze

Extract metrics based on the report type and follow the official analysis pipeline:

Find → Extract → Interpret → Compare → Visualize → Recommend

---

# 4. Gmail Search Patterns

Use these when the active connector is Gmail.

**A. Retrieve the most recent delivery**
Search using: `label:WebPerformanceReport`

**B. Retrieve a defined number of deliveries**
Search using: `label:WebPerformanceReport` and limit results to the last N messages.

**C. Retrieve deliveries within a time window**
Search using: `label:WebPerformanceReport newer_than:30d`

**D. Retrieve by report type**
Search for subjects ending with `| WebPageTest`, `| HTTP Observatory`, `| Wave`, or `| GA4` within the label.

**E. Fallback (if label is unavailable)**
Search using: `subject:"WebPerformance Report"`

**F. Debug mode**
Show the exact Gmail search query before executing it.

## Gmail Pagination

The Gmail API returns a limited number of messages per request. If a `next_page_token` is present in the response:

1. Request the next page using the token.
2. Continue until no `next_page_token` is returned.
3. Maintain subject-first retrieval throughout all pages.

Pagination is required for historical trend analysis and large inboxes.

## Gmail Error Recovery

If Gmail returns incomplete, inconsistent, or empty results:

A. Force a clean search: repeat using only `label:WebPerformanceReport`.
B. Reset context: ignore previous searches and restart the subject-first flow.
C. Re-normalize subjects: reapply HTML decoding.
D. Display raw subjects: show all subjects returned before analysis.

---

# 5. Outlook Search Patterns

Use these when the active connector is Outlook / Microsoft 365.

WebPerformance Report deliveries in Outlook are expected to be organized in one of the following ways (the user may use either):
- A dedicated **folder** named `WebPerformanceReport`.
- A **category** named `WebPerformanceReport` applied to incoming deliveries.

**A. Retrieve the most recent delivery (folder)**
Search in the folder `WebPerformanceReport`, sorted by `receivedDateTime` descending, limit 1.

**B. Retrieve a defined number of deliveries (folder)**
Search in the folder `WebPerformanceReport`, sorted by `receivedDateTime` descending, limit N.

**C. Retrieve deliveries within a time window (folder)**
Search in the folder `WebPerformanceReport` where `receivedDateTime` is within the last 30 days.

**D. Retrieve by category (if folder is not configured)**
Search messages where category equals `WebPerformanceReport`.

**E. Retrieve by report type**
Filter results by subject containing `WebPageTest`, `HTTP Observatory`, `Wave`, or `GA4` after initial retrieval.

**F. Fallback (if neither folder nor category is configured)**
Search for messages where subject contains `WebPerformance Report`.

**G. Debug mode**
Show the exact Outlook query or filter before executing it.

## Outlook Pagination

The Microsoft Graph API paginates results using `@odata.nextLink`. If this field is present in the response:

1. Follow the `@odata.nextLink` URL to retrieve the next page.
2. Continue until no `@odata.nextLink` is returned.
3. Maintain subject-first retrieval throughout all pages.

Pagination is required for historical trend analysis and large inboxes.

## Outlook Error Recovery

If Outlook returns incomplete, inconsistent, or empty results:

A. Force a clean folder search: re-query the `WebPerformanceReport` folder from the beginning.
B. Try category-based search: if the folder search fails, search by category `WebPerformanceReport`.
C. Reset context: ignore previous searches and restart the subject-first flow.
D. Re-normalize subjects: reapply HTML decoding.
E. Display raw subjects: show all subjects returned before analysis.

---

# 6. Validation Requirements

These apply regardless of connector. Before analyzing any data, the assistant must:

1. Display all subjects found.
2. Normalize subjects.
3. Validate patterns against the official list (Section 3, Step 4).
4. Filter out non-matching subjects.
5. Confirm delivery types (WebPageTest, HTTP Observatory, Wave, GA4).
6. Wait for user confirmation unless explicitly instructed otherwise.

This prevents misclassification or analyzing incorrect emails.

---

# 7. Multi-Report Analysis Best Practices

When analyzing multiple deliveries, the assistant must:

- Limit initial batch size (3, 5, or 10 reports).
- Always perform subject-first validation.
- Avoid mixing report types unless the user requests cross-category analysis.
- Never assume chronological order without sorting by date.
- Confirm which reports will be analyzed before retrieving full content.

---

# 8. Safe Analysis Prompts (Recommended for Users)

These prompts ensure the correct retrieval flow is applied.

**Gmail users**

A. Latest delivery:
Search my Gmail for emails with the label WebPerformanceReport. Show me the subjects you found. Then analyze the most recent delivery.

B. Compare multiple deliveries:
Search my Gmail for the last five WebPerformance Report deliveries. List the subjects. Then compare them.

C. Trend detection:
Search using: `label:WebPerformanceReport newer_than:30d`. Show the subjects. Then summarize the trend.

D. Debug retrieval:
Show me the search query before executing it.

**Outlook users**

A. Latest delivery:
Search the WebPerformanceReport folder in my Outlook inbox. Show me the subjects you found. Then analyze the most recent delivery.

B. Compare multiple deliveries:
Retrieve the last five WebPerformance Report deliveries from my Outlook. List the subjects. Then compare them.

C. Trend detection:
Retrieve WebPerformance Report deliveries received in the last 30 days from my Outlook. Show the subjects. Then summarize the trend.

D. Debug retrieval:
Show me the Outlook query before executing it.

---

# 9. Alignment with WPR_AI_Assistant_Instructions.md

This file is fully aligned with the main project instructions:

- Identity and Purpose
- Inbox Access Rules
- Subject-First Retrieval Flow
- Official subject validation patterns
- Analysis pipeline
- Behavior rules (including communication opacity)
- Unsupported actions

It extends operational consistency and reliability to both Gmail and Outlook inboxes.

---

*End of WPR_Inbox_Workflow.md*
