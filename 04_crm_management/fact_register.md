# CRM fact register

This file separates what is known from what is assumed so analytics work can move without pretending the CRM model is already settled.

## Confirmed facts
- An approved proposal existed for a broader growth-readiness system connecting website traffic, Facebook/Instagram activity, CRM integration, and leadership reporting.
- The originally expected working lane leaned more toward website analytics, social and Meta tracking, attribution, and dashboards than CRM status design alone.
- After a conversation with Hillel, the working focus shifted into CRM-first investigation.
- The current role is expected to improve marketing visibility, CRM accuracy, attribution discipline, and leadership-ready reporting.
- Nexus CRM uses a person or episode-style record that spans first contact, referral work, authorization, active service, and terminal outcomes.
- The current system is mixing multiple business questions into too few status fields.
- Discovery found a gap between roughly `1,960` "authorized" records and roughly `1,200-1,300` true active census.
- Authorization does not reliably mean active service.
- Current `Episode.status` values include `New`, `Lead`, `Active`, `Converted`, `On Hold`, `Dropped`, and `Discharged`.
- Current `Episode.leadStage` values include `None`, `New`, `In Progress`, `Dropped Off`, and `Converted`.
- `Authorization.baseStatus` is currently a free-text string, which creates data integrity risk.
- Legacy patient-level statuses such as `pre-intake`, `closed`, `authorized`, and `in-progress` are still affecting interpretation.
- One service line can change without ending the whole patient relationship.
- No production CRM changes should be treated as approved until the status framework is signed off.

## Working assumptions
- New York is the reference workflow. Other markets should follow after New York is stable.
- The episode-level record is the best candidate for the master lifecycle layer.
- The cleanest reporting rollup is still `Referral -> Active -> Discharged`, even if operations need more detail underneath.
- True active census should require more than authorization alone. The current recommended default is `ACTIVE + valid authorization + confirmed SOC`.
- Returning former patients should usually enter through a new episode rather than reopening old terminal records.
- Short-term or outsourced care should not inflate long-term patient counts or core growth reporting.
- Daily and weekly reporting should use trusted metrics first, with caveats where the business meaning is still unstable.

## Open questions
- What is the final threshold for `Active`: confirmed SOC or cleared-to-start?
- What are the final allowed values for `ReferralOutcome` or discharge reasons?
- Is the failed NYIA wait period `180 days`, `6 months`, or something else?
- Does Nexus model one episode per patient or one episode per line of business?
- Which three objects currently share the `LeadStatus` picklist?
- What is the source of truth for active census validation: CRM, EVV, billing, or a hybrid check?
- What is the final rule for `CDPAP` records after the sunset cohort cleanup?
- When a patient has multiple open lines of business, how should the primary line be chosen for reporting?
- What is the final grace period for expired authorization when service is still active?

## Decisions owned by someone else

### Joel and operations
- What each lifecycle state means in real operations.
- What counts as active service.
- How NYIA, holds, reactivation, and drop reasons should behave.
- How to treat mixed cases such as one active line and one dropped line.

### Avi and CRM implementation
- What the object model can support without workarounds.
- How picklists, validation rules, automations, and recalculation hooks should be built.
- How to export baseline data and map legacy values safely.

### Leadership
- When the framework is signed enough to move from analysis into implementation.
- What level of certainty is required before dashboards are treated as decision-grade.
- Whether Phase 1 read-only audit work can continue before broader status decisions are finalized.

### Angelo, intake, ops, and frontline users
- Which follow-up rules are practical in day-to-day use.
- Which dashboard views matter most to sales, intake, and operations.
- Where the current workflow breaks down in real usage rather than in theory.

## Implications for analytics
- Attribution coverage, referral flow, follow-up gaps, and pre-active leakage can be measured now.
- Census, conversion to active, and discharge reporting should not be treated as clean KPIs until definitions are signed.
- Draft architecture notes are useful inputs, but they are not evidence on their own.
- The current CRM artifacts are the present phase of the work, not the whole approved project.
- CRM cleanup should ultimately reconnect to website tracking, Meta/Facebook/Instagram attribution, lead capture visibility, and leadership dashboard reporting.

## Source docs
- [00_source/keren-overkill.md](../00_source/keren-overkill.md)
- [00_source/joel-pipeline.md](../00_source/joel-pipeline.md)
- [00_source/avi-sheet.md](../00_source/avi-sheet.md)
- [.cursor/rules.md](../.cursor/rules.md)
