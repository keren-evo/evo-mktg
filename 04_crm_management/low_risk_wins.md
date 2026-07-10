# Low-risk wins

These are the improvements that can raise reporting quality and CRM usefulness without forcing a full lifecycle redesign first.

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
1. Missing source and campaign cleanup queue.
2. Overdue follow-up watchlist.
3. Referral-source completeness check.
4. Metric-readiness labeling in daily and weekly reports.
5. Contradiction queue for status cleanup.

## Wins to avoid for now
- Full status-model redesign.
- Decision-grade active census reporting.
- Final discharge or retention analysis.
- Any dashboard that hides caveats behind a clean-looking number.
