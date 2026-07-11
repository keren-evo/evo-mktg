# Low-risk wins

These are the improvements that can raise reporting quality and CRM usefulness without forcing a full lifecycle redesign first.

These wins are the current CRM-phase improvements inside the broader approved growth-readiness project. The point is to clean the CRM and reporting layer so it can reconnect cleanly to website, Google Analytics, Meta/Facebook/Instagram, lead capture, and leadership dashboards.

| Win | Why it is safe now | Expected value | Effort | Dependency |
| --- | --- | --- | --- | --- |
| Build a weekly missing-source cleanup queue | Source completeness is observable today. | Better attribution trust and cleaner channel reporting. | Low | Access to source fields. |
| Build a weekly missing-campaign cleanup queue | Campaign coverage is observable today. | Better CPL, CPA, and ROI interpretation. | Low | Campaign-tagging rules. |
| Add referral-source completeness checks | Referral-source coverage does not depend on final active-census logic. | Better doctor, partner, and community-source visibility. | Low | Agreement on required referral-source field. |
| Publish overdue follow-up watchlists | Workflow discipline can be measured before lifecycle redesign. | Reduces pre-active leakage and improves accountability. | Low | Next-follow-up field usage. |
| Publish a contradiction queue | Conflicting status combinations are visible even before final rules are signed. | Gives Avi and ops a focused cleanup list. | Medium | Query or export access. |
| Label metrics by readiness in reports | This is a reporting practice change, not a CRM rebuild. | Prevents bad decisions from unstable numbers. | Low | None. |
| Separate authorized counts from active-patient reporting | This is a framing fix first, not a schema change. | Reduces false confidence in census and ops numbers. | Low | Leadership agreement on caveat language. |
| Track pre-active leakage explicitly | Loss before service is already a real business problem. | Better source-quality and handoff insight. | Medium | Agreed leakage logic for watchlist use. |
| Freeze manual overwrites of original source where possible | Attribution protection is a narrow governance improvement. | Preserves first-touch trust. | Medium | Process enforcement or CRM permissions. |
| Create a baseline snapshot pack | Baselines can be collected before the final redesign. | Gives the team a before-and-after reference. | Low | Export access. |

## Suggested first sequence
1. Freeze funnel + taxonomy ([funnel_definitions.md](../01_reporting_system/funnel_definitions.md), [tracking_rules.md](../05_attribution/tracking_rules.md), [crm_required_fields.md](./crm_required_fields.md)).
2. Missing source and campaign cleanup queue (unknown source = defect).
3. Overdue follow-up and missing next-action watchlists.
4. Referral-source completeness check.
5. Metric-readiness labeling in daily, weekly, and monthly reports.
6. Contradiction queue for status cleanup.
7. Dual-engine cost-per-SOC comparison once SOC extract is directional-trusted.

## Wins to avoid for now
- Full status-model redesign.
- Decision-grade active census reporting.
- Final discharge or retention analysis.
- Any dashboard that hides caveats behind a clean-looking number.
