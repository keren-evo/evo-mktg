# Data quality checklist

Keep reporting trust high while the CRM model is still being clarified. Unknown / blank source is a defect, not a channel. Align with [crm_required_fields.md](../04_crm_management/crm_required_fields.md) and [tracking_rules.md](../05_attribution/tracking_rules.md).

## Daily
- Missing lead source / channel?
- Unknown-source defect count moved?
- Missing campaign on campaign-eligible records?
- Missing referral source?
- Duplicate leads?
- Broken UTMs?
- Missing owner?
- Overdue follow-up?
- Missing next action?
- Contradictory statuses?
- Same-day fixes logged on the daily pulse?

## Weekly
- Lead source coverage drift?
- Campaign coverage drift?
- Referral source coverage drift?
- Unknown-source defect rate declining?
- Pre-SOC leakage increase?
- Referral aging or stalled follow-up?
- Stale marketing → intake handoffs?
- Channel naming inconsistencies vs taxonomy?
- Field activity logs missing account or outcome?

## Directional only checks
- Authorized pipeline jump? (not census)
- SOC extract vs anticipated SOC mix-up?
- Referral-to-SOC or referral-to-active swing?
- Dropped referral spike?
- CPL improving while cost per SOC worsens?

## Red flags
- Sudden lead or referral drop
- Broken attribution
- Rising overdue follow-up count
- Authorized count presented as active census or SOC
- Shadow trackers created outside master taxonomy
- PHI appearing in exports shared for AI or dashboards
