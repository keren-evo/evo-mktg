# KPI dictionary

Use this file with [metrics_readiness.md](./metrics_readiness.md) and [funnel_definitions.md](./funnel_definitions.md). A KPI belongs in leadership reporting only if its business meaning is stable enough for a decision.

This dictionary covers the CRM, referral, digital, and field layers of the growth-readiness system. Pair CRM KPIs with website, Google Analytics, Meta/Facebook/Instagram, and leadership dashboard metrics as those layers reconnect.

## North-star KPIs

| KPI | Plain-English definition | Primary use | Cadence | Readiness | Notes |
| --- | --- | --- | --- | --- | --- |
| Referrals created | Count of records that entered referral work in the period. | Demand visibility. | Daily, weekly, monthly | Safe | Volume, not active-patient proxy. |
| SOC count | Confirmed starts of care in the period. | True marketing outcome. | Weekly, monthly | Directional until extract is validated | Prefer confirmed SOC over anticipated SOC. |
| Cost per referral | Spend or field cost ÷ referrals. | Efficiency by channel. | Weekly, monthly | Safe when cost and referral source are tagged | Requires taxonomy discipline. |
| Cost per SOC | Spend or field cost ÷ SOC. | Primary channel comparison. | Weekly, monthly | Directional until SOC trusted | Do not optimize to CPL alone. |
| Referral → SOC conversion | Share of referrals that reach confirmed SOC. | Funnel quality. | Weekly, monthly | Directional | State Active/SOC caveat when using Active as proxy. |

## Safe KPIs

| KPI | Plain-English definition | Primary use | Cadence | Readiness | Notes |
| --- | --- | --- | --- | --- | --- |
| Leads created | Count of new lead records created in the period. | Top-of-funnel volume. | Daily, weekly | Safe | Break down by source and campaign when available. |
| Lead source coverage | Percent of new leads with a valid source value. | Attribution hygiene. | Daily, weekly | Safe | Missing values trigger cleanup. |
| Campaign coverage | Percent of campaign-eligible leads with a campaign value. | Campaign measurement trust. | Daily, weekly | Safe | Missing campaign data reduces ROI confidence. |
| Referral source coverage | Percent of referral records with a valid referral-source value. | Referral-channel visibility. | Daily, weekly | Safe | Doctor, facility, partner, plan visibility. |
| Follow-up overdue count | Number of open records with overdue next steps. | Workflow discipline and leakage risk. | Daily, weekly | Safe | Operational alert metric. |
| Pre-active leakage watchlist | Count of records leaving before confirmed active service / SOC. | Funnel risk visibility. | Weekly | Safe | Watchlist and trend, not final terminal-outcome truth. |
| Status contradiction watchlist | Count of records with conflicting statuses or lifecycle signals. | Data quality and audit prioritization. | Daily, weekly | Safe | Cleanup need, not business outcome volume. |
| Missing next-action count | Open marketing/intake records with blank next step. | Handoff and CRM discipline. | Daily, weekly | Safe | Defect metric. |
| Digital spend | Paid media spend in period by channel. | Input for CPL / cost per SOC. | Daily, weekly | Safe | From ad platforms. |
| Field activity count | Logged liaison touches / visits / events. | Effort visibility. | Daily, weekly | Safe | Effort, not result. |

## Directional KPIs

| KPI | Plain-English definition | Primary use | Cadence | Readiness | Notes |
| --- | --- | --- | --- | --- | --- |
| Referral in progress | Open referral workload currently being worked. | Intake capacity and aging. | Daily, weekly | Caveat | Labels may mix qualifying, hold, and active referral work. |
| Authorized pipeline | Records with valid-looking authorization coverage. | Readiness and risk visibility. | Weekly | Caveat | Do not present as active census or SOC. |
| Referral-to-active conversion | Share of referrals that become active. | Growth and intake effectiveness. | Weekly, monthly | Caveat | Only with active-definition caveat; prefer SOC when available. |
| Dropped referral trend | Referrals leaving before service begins. | Leakage trend. | Weekly, monthly | Caveat | Depends on consistent drop terminology. |
| Intake → Auth conversion | Share of intake records reaching auth. | Ops / payer bottleneck signal. | Weekly, monthly | Caveat | Distinguish marketing vs ops failure. |
| Auth → SOC conversion | Share of authorized records reaching SOC. | Scheduling / capacity signal. | Weekly, monthly | Caveat | Often non-marketing. |
| Field referral yield | Referrals ÷ field touches (or unique sources contacted). | Liaison effectiveness. | Weekly, monthly | Caveat | Needs consistent activity logging. |
| Source concentration | Share of referrals from top N facilities/sources. | Concentration risk. | Monthly | Caveat | High concentration is a risk flag. |

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
- Daily reports should mostly use safe KPIs plus activity/spend outliers.
- Weekly decision packs lead with referrals, hygiene, leakage, and cost signals; include SOC / cost per SOC when directional caveat is stated.
- Monthly packs add trends, concentration, stop/continue/double.
- Blocked KPIs belong in discovery work, not decision-making scorecards.
