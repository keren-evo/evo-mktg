# Metrics readiness

Use this file before filling any report, scorecard, or dashboard. The point is to separate trusted reporting from metrics that are still blocked by business-definition or CRM-model uncertainty.

## Safe to report now

### Attribution hygiene
- `lead_source_coverage`
  - Meaning: percent of new leads with a populated source field.
  - Why it is safe: this is a data-completeness question, not a lifecycle-definition question.
- `campaign_coverage`
  - Meaning: percent of new leads with a populated campaign field when campaign tagging is expected.
  - Why it is safe: missing campaign data is directly observable.
- `referral_source_coverage`
  - Meaning: percent of referral records with a usable referral-source value.
  - Why it is safe: this supports channel visibility even if downstream statuses are messy.

### Flow visibility before active service
- `new_leads`
  - Meaning: raw inbound lead count by day or week.
  - Why it is safe: use creation-date logic only.
- `new_referrals`
  - Meaning: records newly entering referral work.
  - Why it is safe: it is useful as an intake-volume signal even if the lifecycle model is still being refined.
- `follow_up_overdue`
  - Meaning: records missing the next expected follow-up or sitting past the due date.
  - Why it is safe: this is a workflow hygiene metric.
- `pre_active_leakage`
  - Meaning: records that appear to exit before confirmed active service.
  - Why it is safe: use it directionally to show where work is being lost before service starts.

### Data quality and exception monitoring
- `lead_stage_missing`
  - Meaning: open referral-style records with blank or unusable sub-status.
  - Why it is safe: this is a completeness exception report.
- `contradictory_status_queue`
  - Meaning: records showing conflicting combinations such as drop-like states with active-like indicators.
  - Why it is safe: the contradiction itself is observable even if the final business rule is not.

## Use with caveat
- `referral_in_progress_count`
  - Caveat: current labels may still mix qualifying, intake, and hold scenarios.
- `authorized_pipeline_count`
  - Caveat: authorization is real, but it should not be read as patient census.
- `referral_to_active_conversion`
  - Caveat: only use directionally until `Active` has a signed definition.
- `dropped_referral_trend`
  - Caveat: use only after checking whether "dropped" is being used consistently at the patient, intake, and service-line layers.

## Blocked until definitions or cleanup are settled
- `true_active_census`
  - Blocker: final `Active` definition and source-of-truth validation are not signed.
- `active_authorized_rate`
  - Blocker: current authorized counts include stale, pre-SOC, expired, and non-census cohorts.
- `discharge_rate`
  - Blocker: the line between `Dropped Off` and `Discharged` is not yet stable enough to trust trend reporting.
- `discharge_reason_mix`
  - Blocker: outcome values are not finalized.
- `line_of_business_retention`
  - Blocker: service-line logic and primary-LOB rules still need owner decisions.
- `census_by_coordinator`
  - Blocker: it depends on the same unresolved active-census definition.

## Reporting rules
- Daily reports should lead with safe metrics now.
- Weekly reports can include "use with caveat" metrics, but only if the caveat is stated in plain English.
- Blocked metrics may appear only in a "not decision-ready" section or in a discovery note.
- If a metric can trigger budget, staffing, or operational changes, do not present it as trusted unless it is in the safe group.

## Immediate reporting set
- Lead count by source
- Referral count by referral source
- Missing source rate
- Missing campaign rate
- Missing referral source rate
- Follow-up overdue count
- Pre-active leakage watchlist
- Status contradiction watchlist
