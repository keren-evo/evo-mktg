# Metrics readiness

Use this file before filling any report, scorecard, or dashboard. Separate trusted reporting from metrics still blocked by business-definition or CRM-model uncertainty.

Align stage language with [funnel_definitions.md](./funnel_definitions.md). This file covers CRM, referral, digital, and field reporting inside the growth-readiness system. It should connect back to website analytics, Google Analytics, Meta/Facebook/Instagram activity, and leadership dashboards.

## Safe to report now

### Attribution hygiene
- `lead_source_coverage` — percent of new leads with a populated source field.
- `campaign_coverage` — percent of new leads with a populated campaign field when tagging is expected.
- `referral_source_coverage` — percent of referral records with a usable referral-source value.
- `missing_next_action` — open records with blank next step / next action.

### Flow visibility before SOC
- `new_leads` — raw inbound lead count by day or week (creation date only).
- `new_referrals` — records newly entering referral work.
- `follow_up_overdue` — records missing the next expected follow-up or past due.
- `pre_active_leakage` — records that appear to exit before confirmed active service / SOC (watchlist / trend).
- `field_activity_count` — logged liaison touches, visits, events.
- `digital_spend` — paid media spend by channel from ad platforms.

### Data quality and exception monitoring
- `lead_stage_missing` — open referral-style records with blank or unusable sub-status.
- `contradictory_status_queue` — conflicting combinations such as drop-like states with active-like indicators.
- `unknown_source_defect_count` — blank or "unknown" source treated as a defect, not a channel.

## Use with caveat
- `referral_in_progress_count` — labels may still mix qualifying, intake, and hold.
- `authorized_pipeline_count` — real readiness signal; not census, not SOC.
- `soc_count` — use when confirmed SOC date is extractable; never substitute anticipated SOC.
- `cost_per_referral` — safe only when channel/source tagging and cost allocation match the taxonomy.
- `cost_per_soc` — primary comparison metric; caveat until SOC extract is validated.
- `referral_to_soc_conversion` — preferred over referral-to-active when SOC is available.
- `referral_to_active_conversion` — directional until `Active` has a signed definition.
- `dropped_referral_trend` — check consistent "dropped" usage first.
- `intake_to_auth_conversion` / `auth_to_soc_conversion` — often ops or payer bottlenecks; say so.
- `field_referral_yield` — needs consistent activity logging.
- `source_concentration` — monthly risk signal.

## Blocked until definitions or cleanup are settled
- `true_active_census` — final `Active` definition and source-of-truth not signed.
- `active_authorized_rate` — authorized counts include stale, pre-SOC, expired, and non-census cohorts.
- `discharge_rate` — `Dropped Off` vs `Discharged` not stable.
- `discharge_reason_mix` — outcome values not finalized.
- `line_of_business_retention` — service-line and primary-LOB rules need owner decisions.
- `census_by_coordinator` — depends on unresolved active-census definition.

## Reporting rules
- Daily reports lead with safe metrics and same-day hygiene fixes.
- Weekly decision packs may include caveat metrics only with plain-English caveats.
- Monthly packs add trends, concentration, and stop / continue / double.
- Blocked metrics appear only in "not decision-ready" or discovery notes.
- If a metric can move budget, territory, staffing, or process, do not present it as trusted unless it is safe (or directional with an explicit caveat for SOC/CPA).

## Efficiency rule
If a report does not change a budget, territory, message, or CRM process decision, stop producing it.

## Immediate reporting set
- Lead count by source
- Referral count by referral source and by channel
- Digital spend and field activity
- Missing source / campaign / referral-source rates
- Unknown-source defect count
- Follow-up overdue and missing next-action counts
- Pre-active leakage watchlist
- Status contradiction watchlist
- Cost per referral by channel (when tagged)
- SOC and cost per SOC by channel (directional until validated)
