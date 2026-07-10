# NY home healthcare glossary

This glossary is for analytics and CRM interpretation, not legal or clinical documentation. Every term here exists because it changes how a metric should be read.

| Term | Plain-English meaning | Where it shows up in CRM work | Why it matters for reporting | Common reporting mistake |
| --- | --- | --- | --- | --- |
| Lead | A contact captured before meaningful referral work is underway. | Lead creation, source tagging, campaign tagging, early outreach. | This is the top of the funnel. | Counting all leads as referral opportunities. |
| Qualifying | The stage where staff are checking whether the person is real, reachable, and worth moving into referral work. | Outreach, contact attempts, early triage. | Separates raw demand from workable demand. | Treating "in progress" as a clean referral stage when it still includes qualification noise. |
| Referral | A person actively being worked toward care, but not yet confirmed active with the agency. | Episode or status logic, intake opening, follow-up. | This is the main pre-service pipeline. | Mixing referral volume with active-patient volume. |
| Intake | The operational work required to move a referral toward service. | Intake object, documents, NYIA, payer steps, coordination. | Intake bottlenecks explain why referrals do not become active. | Treating intake status as the master patient lifecycle. |
| Authorization | Payer approval for a specific service. | Authorization record, start and end dates, approved hours, LOB. | It is important for readiness and risk, but it is not the same thing as census. | Reporting authorized records as active patients. |
| SOC | Start of care. The first confirmed service date. | Intake completion, patient activation logic, service-line activation. | This is often the cleanest line between pre-service and active service. | Using anticipated SOC or payer approval as if service has already started. |
| Anticipated SOC | Planned start date before service is confirmed. | Intake tracking, scheduling readiness. | Useful for stall detection. | Counting anticipated starts as active service. |
| Active | A patient the agency is actually responsible for servicing. | Episode status, service-line logic, coordinator reporting. | Core driver of census and operations reporting. | Using the word loosely when the team has not agreed on the entry rule. |
| Non-Authorized | A patient or service line still active operationally but missing current authorization coverage. | Ops risk queues, renewal follow-up. | Shows exposure and cleanup need. | Treating it as automatically dropped or discharged. |
| Dropped Off Referral | A person who exited before becoming an active patient. | Referral terminal state, outcome tracking. | This is pre-active leakage. | Mixing it with discharge or failed service lines. |
| Discharged | A patient who was previously active and then left service. | Terminal episode state, outcome tracking, discharge date. | This is retention and churn reporting. | Using it for cases that never became active. |
| Outcome | Structured reason for a drop or discharge event. | Terminal picklist, outcome reporting. | Makes attrition analysis possible. | Using free text or mixed meanings that cannot be rolled up cleanly. |
| LOB | Line of business. The service type or program track involved. | LTC, custodial, private pay, NHTD, OPWDD, short-term care. | LOB determines routing, risk, and valid comparisons. | Assuming one person equals one service line. |
| Gold LOB | The core long-term service lines that should drive primary patient reporting. | Long-term care, custodial, private pay, and similar core programs. | Helps keep census and sales reporting focused on the main business. | Letting short-term or outsourced lines inflate core totals. |
| Short-Term Care | Temporary care that may run in parallel with the main long-term lifecycle. | Skilled or short-term routing, outsourced cases, temporary service. | Useful for operations, but often not a clean fit for the main census story. | Counting short-term only cases as long-term active patients. |
| Third-Party Referral | A case routed to another agency rather than retained as a Link-serviced patient. | Skilled referrals, outsourced work, partner routing. | It matters for referral handling, not patient census. | Counting it as retained active volume. |
| Medicaid Ticket | A parallel eligibility or application track. | Medicaid object or workflow, deferred or approved states. | It can explain delays without redefining patient status. | Treating Medicaid stages as the main lifecycle. |
| NYIA | A gate or review step that can block progress before service starts. | Intake hold logic, scheduling, authorization readiness. | NYIA delays can create false pipeline optimism. | Leaving cases in generic "in progress" without exposing the hold reason. |
| Hold | A temporary pause on progress that should not be mistaken for closure. | Intake pauses, waiting periods, patient availability issues. | Useful for aging analysis and queue management. | Hiding paused cases inside general in-progress counts. |
| Census | The count of patients the agency should consider truly active. | Leadership dashboards, staffing, revenue planning. | This is one of the most sensitive metrics in the system. | Using authorized count as census. |

## How to use this file
- If a stakeholder uses one of these terms loosely, pause and restate the term in plain English before using it in a metric.
- If a report relies on a term that does not yet have owner sign-off, mark the metric as directional or blocked.
- If a new term appears often in CRM conversations, add it here before turning it into a KPI.
