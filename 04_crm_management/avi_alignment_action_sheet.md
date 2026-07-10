# Avi alignment action sheet

This is the simplified working sheet that comes out of the July 10 alignment with Avi. It is meant to replace overbuilt execution structures with a small, plain-language operating sheet.

## Main JD focus

The original job focus was:
- website setup
- social media and campaign tracking
- analytics
- improved campaign attribution

The working CRM contribution should support that JD by making exports, reporting, and attribution more trustworthy. It should not drift into full CRM redesign before the business meaning is clear.

## Immediate objective

Understand how the current patient and referral lifecycle works well enough to answer:
- what the current statuses mean
- what the proposed statuses are trying to fix
- what is already agreed
- what is still unresolved
- whether the proposed structure will support reliable reporting and exports

## Current state to document

### Current lead-side statuses
- New
- In Progress
- Dropped Off
- Converted

### Current patient-side statuses
- Pre Intake
- In Progress
- Authorized
- Dropped Off
- Closed

### Current line-of-business reality
- LOB statuses are separate from patient-level status.
- One person can have multiple service lines in different states at the same time.
- Current reports may mix patient-level and LOB-level meaning.

## Proposed direction to compare against

### From Avi's spreadsheet
- Lead `New` -> `Lead`
- Lead `In Progress` -> `Qualifying`
- Lead `Dropped Off` -> `Lead Dropped Off`
- Patient `In Progress` -> `Referral In Progress`
- Patient `Authorized` -> `Active`
- Patient `Dropped Off` -> `Dropped Off`
- Patient `Closed` -> `Discharged`

### From Joel's mockup
- Simplified top-level flow:
  - `Referral`
  - `Active`
  - `Discharged`
- Key rule:
  - if the person never became active, they should land in `Dropped Off Referral`
  - if the person became active and later left service, they should land in `Discharged`

## What seems broadly agreed
- The top-level lifecycle should be simpler.
- `Dropped Off` and `Discharged` should not mean the same thing.
- LOB status and patient-level status should not be treated as the same layer.
- Reporting will need supporting fields or history, not just one top-level status.
- The first task is to compare current state to proposed state, not to design the final ideal system.

## Outstanding questions
- What is the exact approved top-level lifecycle?
- What happens to `Pre Intake`?
- What happens to `Converted`?
- How should old `Dropped Off` and `Closed` records be split?
- When exactly does a record count as `Active`?
- What supporting fields are required if one consolidated `Dropped Off` status loses detail?
- Which reports, filters, workflows, list views, and automations depend on the old values?
- Which records can be mapped automatically and which need manual review?

## What you need to understand
- How current records are labeled in real usage.
- How patient-level status interacts with LOB status.
- How multiple open LOBs behave on one person.
- How status buckets are exported today.
- Which existing reports are safe enough to use and which are misleading.

## Questions to take to people

### Avi
- Share the current-to-proposed status spreadsheet.
- Confirm the current status values that are still live in production.
- Clarify which reports and automations are known to depend on the old values.
- Clarify how data exports are best pulled right now.

### Joel
- Confirm the business meaning of each current status.
- Confirm the intended difference between referral drop-off and discharge.
- Confirm how `Active` should be understood operationally.

### Ezra or ops users
- Show how users decide what to do next inside the CRM.
- Show where LOB-level detail changes the patient-level story.
- Show where current screens or reports create confusion.

## 30-day CRM pull for the main JD

The first 30-day pull should focus on the main job, not the whole lifecycle redesign.

### Pull these if available
- leads created
- referrals created
- lead source
- campaign name
- referral source
- owner or assigned user
- created date
- last updated date
- next follow-up date
- current top-level status
- current lead or referral sub-status

### Use the pull to answer
- How many leads came in over the past 30 days?
- Which sources and campaigns are producing volume?
- How complete is source and campaign attribution?
- Which referral sources are active?
- Where are follow-ups being missed or delayed?
- Which status buckets are too messy to trust for reporting?

### Do not use the first 30-day pull to overclaim
- true active census
- clean discharge rates
- line-of-business retention
- any KPI that assumes `Authorized` equals `Active`

## Current blocker

- Live CRM extraction is currently blocked because the stored login in `.cursor/rules.md` is being rejected by the CRM auth endpoint as invalid.
- Until access works, the best fallback is a recent 30-day CRM export or a refreshed login path from Avi or IT.

## Next output after access is fixed

- one 30-day CRM report focused on:
  - lead volume
  - source and campaign coverage
  - referral-source visibility
  - follow-up gaps
  - status-bucket trust issues
