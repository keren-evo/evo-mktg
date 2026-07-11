# Lead and referral flow

Use this file to analyze the pre-SOC funnel. Keep patient-census questions out unless the Active definition is signed.

Business funnel (decision language): Activity → Referral → Intake → Auth → SOC → Retention. See [funnel_definitions.md](../01_reporting_system/funnel_definitions.md).

This is the lead and referral layer of the growth-readiness system. Connect campaign, website, referral, and CRM flow rather than treating pre-SOC movement as CRM-only.

## Working CRM path

```text
Lead -> Qualifying -> Referral -> Intake / Auth work -> SOC -> Active
```

Map CRM stages to the business funnel in funnel_definitions.md. Prefer **SOC** over **Active** for marketing outcome when the SOC date is reliable.

## Guardrails
- `Active` remains a caution area for analytics until signed.
- `Authorized` is readiness, not census and not SOC.
- Anticipated SOC is stall detection only.
- Use this file mainly for movement before confirmed service.

## Safe flow checks
| Stage or signal | Volume | Confidence | Notes |
| --- | --- | --- | --- |
| Leads created |  | High |  |
| Qualified or workable leads |  | Medium | Depends on local workflow usage. |
| Referrals created |  | High |  |
| Follow-up overdue |  | High |  |
| Missing next action |  | High | Defect metric. |
| Pre-SOC / pre-active leakage |  | Medium | Watchlist metric. |
| Marketing → intake handoffs |  | Medium | Needs handoff timestamp usage. |

## Directional conversion checks
| Path | Volume | Conversion | Caveat |
| --- | --- | --- | --- |
| Lead → Referral |  |  | Qualification logic may vary by user. |
| Referral → Intake |  |  | Ops capacity and eligibility. |
| Intake → Auth |  |  | Often payer / NYIA / docs—not pure marketing. |
| Auth → SOC |  |  | Scheduling and staffing can dominate. |
| Referral → SOC |  |  | Preferred marketing outcome path. |
| Referral → Active |  |  | Active definition may still be unsigned. |

## Problem areas
- Stage:
- Cause (marketing vs ops vs payer):
- Owner:

## Fixes
- Improve:
- Clean up:
- Escalate decision:
