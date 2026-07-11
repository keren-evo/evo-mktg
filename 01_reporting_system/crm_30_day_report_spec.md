# CRM 30-day report spec

This is the first report to pull once CRM access is working. It is intentionally tied to the main job description, not to the full status-redesign effort.

## How this fits the approved project

This is the CRM slice of the broader approved growth-readiness proposal. It is a first pass meant to stabilize CRM visibility before reconnecting the data to website tracking, Facebook/Instagram activity, lead capture, and leadership dashboard reporting.

## Report purpose

Use the past 30 days to answer:
- what volume is coming in
- where it is coming from
- how complete attribution is
- where follow-up is breaking
- which status buckets are unsafe for decision-making

## Keep the scope narrow

This report is for:
- analytics
- campaign tracking
- referral-source visibility
- attribution quality
- follow-up discipline

This report is not for:
- true active census
- final discharge analysis
- long-term lifecycle redesign
- line-of-business retention modeling

## Fields to export if available
- record ID
- created date
- updated date
- owner or assigned user
- lead source
- campaign name
- referral source
- current status
- lead or referral stage
- next follow-up date
- last contact date
- notes or outcome field if exportable without PHI risk

## Questions the report should answer

### Volume
- How many leads were created in the past 30 days?
- How many referrals were created in the past 30 days?
- How did volume shift week to week?

### Attribution
- What percent of records have a lead source?
- What percent have a campaign name?
- What percent have a referral source?
- Which sources are producing the most volume?
- Which campaigns are missing usable attribution?

### Workflow
- How many records have overdue follow-up?
- Which owners have the largest overdue queues?
- Which statuses are being used as catch-all buckets?

### Reporting trust
- Which current status buckets look too mixed to use as KPIs?
- Is `Authorized` being used in a way that can mislead reporting?
- Are there contradictions between top-level status and practical workflow?

## First output format

Use the first pass to produce:
- a short executive summary
- a KPI scorecard
- a source and campaign table
- a referral-source table
- a follow-up risk section
- a note on status-bucket trust issues

## If live pull is still blocked

Fallback options:
- a CSV or spreadsheet export from Avi or IT
- a manual report export from the CRM UI
- a screen-share walkthrough where the needed filters and columns are captured
