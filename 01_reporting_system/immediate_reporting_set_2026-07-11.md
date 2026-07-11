# Immediate reporting set

Date pulled: July 11, 2026  
Source: live Nexus CRM `report.run` queries against saved reports

## Executive summary

- Lead volume is measurable right now from the existing saved reports.
- Source completeness is weak in both last month and this month-to-date.
- Campaign attribution is effectively unusable in the current saved lead reports because the campaign field is blank on every returned lead.
- There is already a meaningful pre-active workflow backlog and a very large status-contradiction queue.
- Referral-side source reporting is only partially usable from the current saved report inventory and needs either paged export or a purpose-built referral report.

## Lead counts

| Period | Lead count |
| --- | ---: |
| Last month | 394 |
| This month to date | 112 |
| Today | 7 |

## Lead count by current source field

Note: the saved lead reports expose `Referral Source`. A separate top-of-funnel `Lead Source` report was not identified in the current saved report inventory.

### Last month

| Source | Count |
| --- | ---: |
| Blank | 191 |
| Referral | 138 |
| Marketer | 43 |
| Facility | 16 |
| Email | 4 |
| Billboard | 1 |
| Phone | 1 |

### This month to date

| Source | Count |
| --- | ---: |
| Blank | 51 |
| Referral | 35 |
| Marketer | 16 |
| Facility | 8 |
| Phone | 2 |

## Missing data rates

| Metric | Last month | This month to date |
| --- | ---: | ---: |
| Missing source rate | 48.5% | 45.5% |
| Missing campaign rate | 100.0% | 100.0% |

## Lead stage mix

### Last month

| Stage | Count |
| --- | ---: |
| Dropped Off | 193 |
| Converted | 136 |
| In Progress | 38 |
| New | 27 |

### This month to date

| Stage | Count |
| --- | ---: |
| Converted | 59 |
| New | 27 |
| In Progress | 16 |
| Dropped Off | 10 |

## Immediate watchlists

| Watchlist | Count | Meaning |
| --- | ---: | --- |
| Untagged leads | 1 | Current lead records missing expected tagging state |
| Untouched pre-active records | 224 | Pre-active records sitting in lead, pre-intake, or in-progress states |
| Dropped intake watchlist | 17 | Long-term dropped intakes still worth review |
| Status contradiction queue | 7,322 | Records where patient status and related status logic conflict |

## Status contradiction example

One sampled contradiction pattern shows:
- patient status = `Authorized`
- lead stage = `Converted`
- current long-term LOB = `Active`
- authorization status missing on the returned record

This is exactly the kind of mixed-status logic that makes downstream reporting hard to trust.

## Referral-side note

The current saved report inventory includes a very large `Marketer's Enrollment Pipeline` report with a total of `16,675` rows. It clearly contains referral-source data, but the exact source mix is not yet safe to publish from this first pass because the report exceeds one page and needs paged extraction or a smaller purpose-built report.

Directional signal from the first page suggests:
- facility-sourced referrals dominate
- marketer-sourced referrals are second
- blank referral source still exists

Treat that as directional only until the full referral report is pulled cleanly.

## Main JD implications

- The strongest immediate value is in attribution hygiene and reporting discipline, not deeper status redesign.
- Missing source is already large enough to distort marketing visibility.
- Missing campaign on all returned lead records means campaign ROI cannot be trusted from the current CRM lead reports.
- Pre-active follow-up and dropped-intake queues are large enough to justify immediate cleanup and accountability reporting.

## Caveats

- The lead reports available in CRM are saved as `Last Month` and `This Month`, not a true rolling last-30-days view.
- `Referral Source` is the visible source field in the saved lead reports used here.
- Referral-source counts for the large active referral pipeline still need a complete paged pull.
