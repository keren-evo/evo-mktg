# Stakeholder decision map

Use this file when a reporting question turns into a process or CRM-design question. The goal is to identify who owns the meaning, who owns the build, and whether analytics can still move before the final decision lands.

## Core roles

| Role | Primary responsibility | Typical questions they should own |
| --- | --- | --- |
| Keren / analytics and CRM reporting | Reporting logic, attribution trust, KPI framing, risk visibility. | Can this metric be reported now? What caveat is needed? What cleanup backlog should exist? |
| Joel / operational truth | Real-world lifecycle meaning and edge-case behavior. | What does `Active` mean? When is a case dropped versus discharged? What should happen in mixed LOB cases? |
| Avi / CRM implementation | Schema, picklists, automations, recalculation logic, migration safety. | Can Nexus support this cleanly? Where should the field live? What can be validated or automated? |
| Leadership | Sign-off, phase gating, and decision-grade reporting thresholds. | Is the framework settled enough for rollout? Which metrics are trusted enough for staffing or growth decisions? |
| Intake and ops users | Day-to-day workflow truth and practical usability. | Does this status flow match real work? Which queues matter? Which fields will actually be maintained? |
| Sales and growth users | Source quality, follow-up discipline, and referral handling. | Which definitions support channel performance and pipeline accountability? |

## Recurring issue map

| Issue | Business-meaning owner | System-change owner | Main report consumers | Can reporting move now? |
| --- | --- | --- | --- | --- |
| Lead vs qualifying vs referral boundary | Joel and sales/growth | Avi | Sales, growth, leadership | Yes, directionally. Use clear caveats. |
| Definition of `Active` | Joel and leadership | Avi | Leadership, ops, analytics | No, not for decision-grade KPI use. |
| Authorized vs active | Joel and ops | Avi | Leadership, ops | Yes for risk visibility, no for census reporting. |
| Dropped off vs discharged | Joel and ops | Avi | Leadership, ops, analytics | Only directionally until terminal logic is signed. |
| Referral outcome values | Joel | Avi | Leadership, analytics | No for clean reason-mix reporting. |
| Source and campaign coverage | Analytics and growth | CRM admins or Avi | Leadership, growth | Yes. This should move now. |
| Follow-up expectations and SLA | Sales, intake, and ops | Avi if automation is needed | Frontline teams, analytics | Yes. Track as workflow discipline. |
| Primary LOB logic | Joel and ops | Avi | Ops, leadership | Only with caveat. |
| Medicaid ticket handling | Joel and Medicaid team | Avi | Intake, ops | Yes, as a parallel workflow view. |
| Dashboard trust threshold | Leadership | Avi for implementation, analytics for caveats | Leadership | Yes, if metrics are labeled by readiness. |

## How to use this map
- If the question is about meaning, route it to the business-meaning owner.
- If the question is about fields, picklists, validation, or automation, route it to the system-change owner.
- If the answer would change staffing, budget, or census interpretation, do not skip leadership sign-off.
- If reporting can move now, publish the metric with an explicit confidence or caveat note instead of waiting for the whole CRM redesign.

## Decision rule for analytics work
- Do not turn an owner-held decision into a silent assumption inside a dashboard.
- If a metric depends on an unresolved owner decision, either block it or downgrade it to directional use.
