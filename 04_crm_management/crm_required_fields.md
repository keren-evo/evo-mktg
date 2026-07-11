# CRM required fields and handoffs

Operational companion to [tracking_rules.md](../05_attribution/tracking_rules.md) and [lead_flow.md](./lead_flow.md). Goal: CRM is the spine for marketing accountability, not a spreadsheet graveyard.

## Object model (working)

| Object | Role |
| --- | --- |
| Referral source account | Hospital, SNF, ALF, MD office, case manager, MLTC plan, community partner |
| Owner | Liaison / field marketer / digital owner |
| Lead / referral record | Demand unit with channel, campaign, source, stage, next action |
| Activity log | Field or digital touch tied to account + outcome |
| Handoff event | Marketing → intake timestamp and status |

## Required at create

- Channel (canonical picklist)
- Owner
- Stage
- Next action + due date (if open)
- Campaign (when campaign-eligible)
- Referral source (when at referral stage)

## Hygiene product (weekly defects)

Treat these as a product backlog, not occasional cleanup:

1. Unknown / blank channel or source
2. Missing campaign on paid or named initiatives
3. Missing referral source on referrals
4. Missing next action on open records
5. Overdue follow-ups
6. First-touch overwrites detected
7. Status contradictions
8. Stale handoffs (accepted SLA breached)

Publish counts on the weekly decision pack. Unknown source is never a valid channel segment.

## Handoff SLA (working default)

| Step | Expectation | Metric |
| --- | --- | --- |
| Marketing marks ready for intake | Timestamp set | Handoff volume |
| Intake accepts or returns | Status set within agreed SLA | Accept / return rate |
| Open past SLA | Appears on stale queue | Stale open count |

Adjust SLA hours only with ops agreement; document the signed value in the stakeholder decision map.

## HIPAA-aware hygiene

- Marketing CRM holds the minimum needed for attribution and follow-up.
- Do not paste PHI into ad platforms, AI prompts, dashboards shared broadly, or chat summaries.
- Prefer account-level and aggregate reporting in leadership packs.
- Credentials and patient identifiers stay out of repo docs and report narratives.

## Low-risk enforcement sequence

1. Required-field checks on new creates
2. Weekly missing-source / missing-campaign queues
3. Overdue and missing next-action watchlists
4. Freeze first-touch overwrites where permissions allow
5. Only then consider structural status-model redesign

See [low_risk_wins.md](./low_risk_wins.md).
