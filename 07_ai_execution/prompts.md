# AI prompt library

Paste only aggregate or de-identified inputs. Never include PHI, credentials, or patient identifiers.

## Weekly decision pack brief
You are drafting a leadership decision pack for NY home healthcare marketing.
Input: the filled weekly scorecard tables (referrals, SOC, cost per referral, cost per SOC by channel, CRM defects, field yield).
Rules:
- Exactly three findings: what is working, what is weak, one reallocation or fix
- Prefer cost per SOC over CPL
- If intake→auth→SOC is weak, say whether it looks marketing vs ops/payer
- Mark directional metrics as caveated
- Keep the whole brief under one page
Output: executive summary, one channel table rewrite if needed, actions with owners.

## Monthly stop / continue / double
Using the monthly trend scorecard, recommend stop / continue / double per channel or initiative.
Require evidence from referrals, SOC, cost per SOC, concentration, and CRM defect trends.
Do not invent census or discharge metrics.

## Anomaly assist
Given this period-over-period export summary, list anomalies only:
- volume spikes/drops
- CPL improving while cost per SOC worsens
- coverage rate drops (source, campaign, referral source)
- field activity up with referrals flat
- aging / overdue spikes
For each anomaly: likely cause hypothesis, what to check next, whether it is marketing or ops.

## CRM defect queue
From this defect count table, produce a prioritized cleanup queue:
unknown source, missing campaign, missing referral source, missing next action, overdue follow-up, stale handoffs, status contradictions.
For each: why it hurts attribution or SOC visibility, owner role, effort (low/med).

## Campaign naming normalize
Rewrite these campaign names to match taxonomy:
channel / initiative / geo / creative.
Return old → new mapping. Do not invent channels outside the canonical picklist.

## Facility one-pager
Draft a one-page leave-behind for a NY home healthcare liaison visiting a [hospital/SNF/ALF/MD office].
Include: who we serve, service area, how to refer, what happens after referral, contact.
Tone: practical, not hype. No clinical overclaim. No PHI examples.

## Follow-up email variants
Write three short follow-up emails for a [discharge planner / case manager / MD office / MLTC contact] after a liaison visit.
Goal: make the referral path obvious. Include subject lines. Keep each under 120 words.

## Video concept (referral relationship)
Create 3 short video concepts for strengthening referral relationships (not consumer virality).
For each: hook, 20–40s outline, CTA, who it is for (liaison leave-behind vs partner webinar).
No patient stories with identifiable detail.

## Funnel drop diagnosis
Where is the biggest drop between Activity → Referral → Intake → Auth → SOC?
Explain likely cause, whether marketing owns the fix, and the smallest next action.
Use only the numbers provided.

## Growth-readiness system check
Review this initiative as one connected system:
- website traffic and lead capture
- Meta/Facebook/Instagram tracking
- CRM attribution and workflow visibility
- referral / field flow
- leadership reporting
Explain what is connected, what is broken, what to fix first. Prefer hygiene and taxonomy before redesign.
