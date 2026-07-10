# KPI dictionary

Use this file with [metrics_readiness.md](./metrics_readiness.md). A KPI belongs in leadership reporting only if its business meaning is stable enough for a decision.

## Safe KPIs

| KPI | Plain-English definition | Primary use | Cadence | Readiness | Notes |
| --- | --- | --- | --- | --- | --- |
| Leads created | Count of new lead records created in the period. | Top-of-funnel volume. | Daily, weekly | Safe | Break down by source and campaign when available. |
| Referrals created | Count of records that entered referral work in the period. | Intake demand visibility. | Daily, weekly | Safe | Use as volume, not as active-patient proxy. |
| Lead source coverage | Percent of new leads with a valid source value. | Attribution hygiene. | Daily, weekly | Safe | Missing values should trigger cleanup. |
| Campaign coverage | Percent of campaign-eligible leads with a campaign value. | Campaign measurement trust. | Daily, weekly | Safe | Missing campaign data reduces channel ROI confidence. |
| Referral source coverage | Percent of referral records with a valid referral-source value. | Referral-channel visibility. | Daily, weekly | Safe | Use for doctor, partner, and community-source visibility. |
| Follow-up overdue count | Number of open records with overdue next steps. | Workflow discipline and leakage risk. | Daily, weekly | Safe | Good operational alert metric. |
| Pre-active leakage watchlist | Count of records leaving before confirmed active service. | Funnel risk visibility. | Weekly | Safe | Use as a watchlist and trend, not as final terminal-outcome truth. |
| Status contradiction watchlist | Count of records with obviously conflicting statuses or lifecycle signals. | Data quality and audit prioritization. | Daily, weekly | Safe | Shows cleanup need, not business outcome volume. |

## Directional KPIs

| KPI | Plain-English definition | Primary use | Cadence | Readiness | Notes |
| --- | --- | --- | --- | --- | --- |
| Referral in progress | Open referral workload currently being worked. | Intake capacity and aging. | Daily, weekly | Caveat | Current labels may mix qualifying, hold, and active referral work. |
| Authorized pipeline | Records with valid-looking authorization coverage. | Readiness and risk visibility. | Weekly | Caveat | Do not present as active census. |
| Referral-to-active conversion | Share of referrals that become active. | Growth and intake effectiveness. | Weekly, monthly | Caveat | Only use after stating the active-definition caveat. |
| Dropped referral trend | Referrals leaving before service begins. | Leakage trend. | Weekly, monthly | Caveat | Depends on consistent use of drop terminology. |

## Blocked KPIs

| KPI | Why blocked | What must be settled first |
| --- | --- | --- |
| True active census | The active definition is still contested. | Final `Active` rule and source-of-truth check. |
| Active authorized rate | Authorized counts are not a reliable active-patient proxy. | Stale and non-census cohorts must be resolved. |
| Discharge rate | Terminal logic is not yet clean enough. | Final split between `Dropped Off` and `Discharged`. |
| Discharge reason mix | Outcome values are not finalized. | Signed terminal-outcome picklist. |
| Active by coordinator | It depends on true census logic. | Same prerequisite as true active census. |
| LOB retention | Line-of-business state rules are still unresolved. | Primary-LOB and service-line definitions. |

## How to use this dictionary
- Daily reports should mostly use safe KPIs.
- Weekly reports may include directional KPIs when the caveat matters to the decision.
- Blocked KPIs belong in discovery work, not decision-making scorecards.
