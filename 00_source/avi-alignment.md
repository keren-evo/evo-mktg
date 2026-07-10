# Link Homecare CRM Alignment Meeting Summary

**Meeting:** Keren Lacadin and Avi Rosenholtz
**Date:** July 10, 2026
**Duration:** 1 hour, 33 minutes
**Primary purpose:** Align Keren’s CRM-status work with the current technical and operational reality, simplify the execution approach, and determine the most useful next steps. 

## Executive Summary

The meeting was a constructive project reset, not a rejection of Keren’s work. Avi said he was impressed by Keren’s capability, initiative, organization, and use of tools, but the work had expanded too quickly into detailed architecture, Asana tasks, AI-generated structures, and an interactive platform before the current workflow and proposed status model were sufficiently understood.

The agreed direction is to start with what already exists: **Joel’s two mockups and Avi’s current-to-proposed status spreadsheet**. Keren should use those materials to understand the present lifecycle, confirm the proposed changes, identify only the remaining questions, and then support the mapping of existing records into the new structure.

The work should initially be simple and business-readable. Detailed UI design, automation, dashboards, technical tickets, decision platforms, and project-management systems should follow only after the status structure and migration requirements are clear.

---



## 1. Why the meeting happened

Hillel and Leah asked Avi to meet with Keren because there was a mismatch between the volume and structure of the work being produced and where the CRM status project actually stood.

Keren’s original understanding was that the project would focus on:

- website setup,
- social media and campaign tracking,
- analytics,
- and improved campaign attribution.

The focus then shifted toward fixing the CRM status structure first. While exploring the CRM and attempting to export data, Keren encountered ambiguous Salesforce-era labels, inconsistent status logic, and unreliable reporting buckets.

Avi wanted to:

- understand how Keren thinks and works,
- review what she had produced,
- align her work with the actual project stage,
- reduce unnecessary complexity,
- and help her contribute in a way that creates faster project movement.

---



## 2. Shared assessment of the CRM



### The CRM itself is robust

Both agreed that the CRM contains significant functionality and many useful data points. Avi explained that many unnecessary fields had already been removed during the move from Salesforce, and that much of the remaining underlying structure exists for legitimate operational reasons.

The main problem is not necessarily that the technical foundation is invalid. The problem is that the higher-level presentation and operational workflow have not yet been simplified enough for end users.

### The end-user experience is unclear

Keren observed that an enrollment specialist can see many data points but may still be unable to answer:

> What am I supposed to do next?

Avi strongly agreed.

The system may technically contain the necessary information, but the status structure, screens, reports, and workflow presentation do not consistently translate that information into clear operational action.

### Reporting and exports are not yet trustworthy enough

Keren raised the concern that pulling a status bucket for:

- census reporting,
- campaigns,
- follow-up,
- or operational analysis

does not necessarily return the population the label appears to represent.

This is especially important when a proposed status such as **Active** could include records that are authorized, pending, inactive, or otherwise not truly receiving service.

Avi’s response was that these concerns should become direct questions against the proposed model:

- Will the proposed status structure support accurate reporting?
- Will it allow Keren to produce reliable exports?
- Will records labeled Active actually represent the intended population?
- What additional fields are needed when a single status no longer tells the full story?

---



## 3. Salesforce legacy and the unified-record opportunity

The former Salesforce workflow used separate objects during lead conversion. Because of that design, separate lead and patient status systems had some technical justification.

The custom CRM now uses a more unified record structure. Avi explained that maintaining two separate status systems to describe where one person is in the lifecycle may no longer be necessary.

A simple starting point would be to place the existing statuses into one continuous structure:

### Existing lead-side statuses

- New
- In Progress
- Dropped Off
- Converted



### Existing post-conversion or patient-side statuses

- Pre-Intake
- In Progress
- Authorized
- Dropped Off
- Closed

From there, the team can decide:

- which statuses should remain,
- which should be renamed,
- which should be combined,
- which should be removed,
- and which require additional data to preserve their historical meaning.

Avi emphasized that the first task is not to design the final ideal architecture. It is to clearly document **where the system is today** and compare that with what is being proposed.

---



## 4. Status logic discussed



### Top-level status is the immediate focus

The current project is primarily about simplifying the **top-level patient lifecycle statuses**.

Other statuses already exist beneath that level, especially for individual lines of business. Those should not automatically be treated as patient-level statuses.

### Dropped Off versus Discharged

Avi clarified the intended distinction:

- A lead or referral that never became active should be **Dropped Off**.
- A person who became active and later stopped receiving service should be **Discharged**.

This distinction was recognized as central to the revised model.

### Service lines operate separately

A person can have multiple lines of business at the same time. One service line may be:

- interested,
- in progress,
- active,
- dropped,
- expired,
- or authorized,

while another service line is in a different state.

The overall patient status and the individual LOB statuses therefore cannot be treated as the same thing.

### A universal Dropped Off bucket may lose history

Avi noted that consolidating multiple old Dropped Off states into one status could make the status itself less descriptive.

The new status may no longer indicate:

- whether the person dropped during the lead stage,
- whether an intake had already been opened,
- how far the person progressed,
- or whether the person had ever been active.

That may be acceptable, but supporting fields or historical data will be needed to tell the complete story in reporting.

### Removing statuses can affect existing dependencies

Legacy statuses may already be referenced by:

- reports,
- list views,
- dashboards,
- filters,
- workflows,
- automations,
- and other technical processes.

The team must decide whether to make a direct change or take a safer phased approach. Status removal is not simply a label change; it may affect everything built around the values.

### Exact mappings remain incomplete

The broad direction is reasonably clear, but detailed migration rules remain unresolved, including:

- what happens to Pre-Intake,
- how Converted maps,
- how old Dropped Off records should be interpreted,
- how Closed records should be classified,
- and which records need manual review.

---



## 5. New York and Florida scope

Keren described New York as the more complicated operation. Avi refined that statement:

- New York is not necessarily inherently more complicated.
- It is much more deeply embedded in the CRM.
- New York has used the system operationally for many years.
- Florida has only a basic scaffold and is still being built into the CRM.

The immediate focus on New York is therefore driven by maturity, historical usage, and embedded dependencies—not necessarily by the business model being objectively more complex.

---



## 6. Review of Keren’s Cursor and GitHub work

Keren created a repository using her EVO email and published an interactive workspace through GitHub Pages.

The workspace was intended to:

- show current and proposed CRM structures,
- visualize the lifecycle,
- make the flow easier for leadership to understand,
- allow users to click through statuses,
- explain definitions,
- and capture comments against individual items.

Avi found the work impressive and technically interesting. However, the repository is not yet in the company GitHub organization. He said it should eventually be moved into EVO’s organization repositories.

### How Keren built the context

Keren used several sources to inform the workspace:

- EVO Bot responses describing the patient lifecycle,
- exported educational material about New York home care,
- CRM screenshots,
- manual exploration of patient records,
- Schema Manager review,
- Joel’s proposed mockups,
- prior leadership conversations,
- and her own strategic and CRM knowledge.

She also opened the CRM inside Cursor’s browser.

However, Cursor was not directly retrieving CRM data through an API. Much of its understanding came from:

- screenshots,
- visible page content,
- prompts,
- and the supporting materials Keren supplied.

Avi noted that EVO’s CRM repositories and other internal technical materials could eventually provide Cursor with more reliable context.

---



## 7. Review of the interactive decision workspace

Keren explained that the interactive platform was not intended to change the CRM automatically. It was meant to serve as a leadership and decision-support guide.

It included:

- current versus proposed flows,
- lifecycle diagrams,
- definitions,
- suggested statuses,
- comment areas,
- and automatic comment saving after users entered their names.

Avi’s assessment was:

- there is a lot of good work in it,
- it is technically usable,
- but it introduces too much friction,
- and even a technical user might not want to use it for the present decision.

Joel’s mockups already provide a visual starting point. The immediate need is not a more sophisticated commenting platform; it is a simple way to surface the actual decisions and unresolved questions.

The interactive workspace could still become useful later, but it is currently fine-tuning rather than the foundation of the work.

---



## 8. Avi’s central feedback: reduce what is surfaced

Avi described a common problem for technical people:

- Technical users see thousands of relevant details.
- Because the details matter, they want to expose all of them.
- Business stakeholders will not process all of those details.
- The job is to identify the small number of decisions that require stakeholder consensus.
- The remaining complexity should be handled internally or under the hood.

His framing was effectively:

> Surface the ten details leadership needs to decide; manage the other 9,990 details within the technical and implementation process.

The problem with the current workspace was not that the details were wrong. It was that too many valid details were being surfaced too early and to the wrong audience.

---



## 9. Avi’s feedback on sequencing

Avi advised the following sequence:

1. Understand the current process deeply.
2. Put the present status structure on paper.
3. Compare it with the proposed structure.
4. Ask clarifying questions.
5. Incorporate the answers.
6. Ask follow-up questions where needed.
7. Reach a clear objective.
8. Only then design solutions, implementation structures, visuals, or automation.

Keren had moved too quickly toward:

- glossary approval,
- detailed architecture,
- schema mapping,
- baseline audits,
- Asana tasks,
- interactive visuals,
- and implementation logic.

Those outputs may eventually be useful, but some were premature because they were based on incomplete operational understanding.

---



## 10. “Understand” before “audit”

Keren described one task as auditing the patient lifecycle and running distribution baselines.

Avi repeatedly asked what that meant in plain English.

The intended purpose was to understand:

- how records are currently labeled,
- how patient statuses interact with LOB statuses,
- how records with multiple LOBs behave,
- how status buckets are exported,
- and whether reports reflect the actual workflow.

Avi recommended reframing the work as:

> Understand how the patient lifecycle currently operates.

That may involve:

- a walkthrough with Avi,
- a discussion with Joel,
- a conversation with Ezra,
- reviewing existing records,
- and only later documenting the findings.

Several detailed Asana tasks may actually represent one foundational task: **understand the current lifecycle and the operational story behind it.**

---



## 11. Plain language requirement

Avi highlighted that task descriptions such as:

- “run distribution baselines,”
- “map Nexus objects to auto queries,”
- or similar technical wording

do not clearly communicate the business purpose.

Tasks and questions should instead say what is actually needed, such as:

- understand how the patient lifecycle works,
- document current statuses,
- identify what each status means,
- determine where each current status should map,
- or identify which reports depend on a status.

This improves communication with operations and leadership and reduces the appearance that the entire system is being technically challenged before its business use is understood.

---



## 12. Review of Asana

Keren initially created a small set of tasks, but the project expanded as she explored:

- CRM governance,
- glossary definitions,
- stage sign-off,
- baseline audits,
- schema mapping,
- edge cases,
- short-term workflows,
- and implementation planning.

The detailed Asana structure came from a combination of:

- Cursor,
- ChatGPT,
- Copilot,
- Asana AI,
- standard CRM improvement logic,
- meeting notes,
- and imported documents.

Avi identified this as an example of a key AI risk:

- AI can rapidly produce large amounts of plausible work.
- Many tasks may individually make sense.
- The total system may still be overwhelming or poorly sequenced.
- High output does not automatically create project velocity.

Keren agreed that Asana was not the best environment for resolving the present status decisions.

---



## 13. Use of AI agents

Keren demonstrated several Copilot agents, including project-management and execution agents originally created for the analytics and social-media work.

She explained that dedicated agents help by:

- preserving EVO-specific context,
- providing guardrails,
- and preventing unrelated personal or project contexts from mixing.

Avi questioned whether separate conversational agents provide enough additional value compared with using a well-contextualized ChatGPT or Claude project. He recognized the value of dedicated agents for automated recurring tasks but remained undecided about their advantage for general discussion and analysis.

Keren said she currently prefers ChatGPT and Claude for many tasks but used Copilot because it was available inside the company’s Microsoft environment.

No final decision was made about the best AI platform or agent structure.

---



## 14. Recommended project-management approach

Avi recommended starting with a much simpler personal tracking sheet.

The initial sheet should be owned primarily by Keren and should track:

- what she needs to understand,
- what questions require answers,
- what inputs are needed from other people,
- what decisions are pending,
- and what actions follow.

A need for input from Joel does not automatically mean Joel should receive an Asana task. Keren may own the task of obtaining the answer through:

- email,
- Teams,
- a meeting,
- a direct question,
- or another suitable method.

Whether the work eventually belongs in:

- Asana,
- a CRM ticket,
- a shared spreadsheet,
- Teams,
- a web platform,
- or another system

is a secondary optimization. The process should first work in a simple form before being automated or formalized.

Avi compared this to designing a process with pen and paper before building systems around it.

---



## 15. Materials now considered the project baseline

Avi identified the immediate source materials as:

1. **Joel’s two mockups**
2. **Avi’s current-to-proposed status spreadsheet**
3. Existing knowledge of the current CRM statuses and LOB statuses

He believed there was already substantial agreement around the broad direction.

The next task is to examine those materials and determine:

- what is already agreed,
- what remains unclear,
- what questions need answers,
- and what must be decided before execution.

The whole “stage definitions and sign-off” section should likely become one consolidated task rather than many granular tasks.

---



## 16. Suggested sign-off method

Avi suggested that status confirmation might be handled through a concise final email containing:

- the proposed structure,
- what appears to be agreed,
- the remaining outstanding questions,
- and a request for confirmation.

That email could result in:

- written approval,
- corrections,
- or another meeting if necessary.

This is preferable to assigning many granular approval tasks to leadership and waiting for each one to be completed separately.

---



## 17. Three major implementation efforts identified

Once the status framework is confirmed, the work will likely separate into three larger efforts:

### 1. Status and data alignment

- Change the status values.
- Map existing records into the new structure.
- Preserve important historical meaning.
- Determine which records can be migrated automatically.
- Identify which records require manual review.



### 2. User interface

- Develop a UI that stakeholders agree on.
- Make statuses and next actions understandable.
- Present the correct level of detail to users.
- Avoid creating unnecessary friction.



### 3. Dependent systems

Review everything currently built around the status values, including:

- reports,
- dashboards,
- list views,
- workflows,
- queues,
- automations,
- filters,
- and operational processes.

These dependencies must be addressed end-to-end so the new structure does not break existing operations.

---



## 18. Technical work management

Avi explained that EVO’s CRM ticketing system is being expanded.

The technical team is beginning to run more of its detailed shop work through the CRM ticketing system rather than Asana.

This means:

- Asana may not be the right place for granular technical implementation tasks.
- Business decisions and technical execution may need different management channels.
- Keren may later receive access to or guidance on using the technical ticketing system.
- The exact project-management architecture can be determined as the work becomes clearer.

---



## 19. Important terminology correction

Avi corrected the acronym used during the discussion:

- It is spelled **NYIA**, not NIA or “Naya.”

He was not completely certain of the expanded phrase during the call, but the spelling correction was explicit.

---



## 20. Relationship and performance feedback

Avi repeatedly emphasized that his comments were intended as alignment rather than criticism.

He said:

- Keren had been placed in a difficult and ambiguous situation.
- Her work demonstrated strong capability.
- Her initiative and organization were valuable.
- The interactive GitHub work was technically impressive.
- She could contribute significantly to moving the project forward.
- She should not allow his suggestions to suppress her own thinking.

He used a “manager’s paradox” analogy: someone building a complex system must spend most of their attention solving thousands of internal problems, while an outsider can more easily notice visible flaws. His intent was to help Keren direct her capability toward the work that would produce the greatest project velocity.

Keren said the conversation was the most comfortable she had experienced since joining the effort and expressed appreciation for the feedback and clarity.

---



## 21. Agreed immediate next steps



### Avi

- Send Keren the current-to-proposed status spreadsheet.
- Be available for questions and clarification.
- Consider providing better technical context through EVO’s CRM repositories.
- Show Keren the developing CRM ticketing system.
- Continue the conversation in a follow-up meeting, potentially Monday.
- Help connect Keren’s work to the technical and operational sides of the project.



### Keren

- Review the discussion and rethink the execution structure.
- Start from Joel’s mockups and Avi’s spreadsheet.
- Simplify the project into current state, proposed state, and outstanding questions.
- Avoid expanding the detailed Asana framework at this stage.
- Develop a small personal tracking sheet rather than assigning many tasks to others.
- Seek clarification directly from Avi, Joel, Ezra, or other relevant stakeholders.
- Identify whether the proposed statuses support accurate reporting and exports.
- Prepare a focused confirmation or sign-off communication.
- Show Avi the revised direction during the next meeting.
- Continue using her own judgment rather than mechanically following every suggestion.



### Repository and tools

- The GitHub repository should eventually be moved into EVO’s organization.
- Internal CRM repositories may provide more accurate context than screenshots.
- Technical work may eventually be tracked in the CRM ticketing system rather than Asana.

---



## 22. Remaining open questions

The meeting did not finalize the following:

1. What is the exact approved top-level lifecycle?
2. How should every existing lead and patient status map into it?
3. What should happen to Pre-Intake records?
4. How should Converted be handled?
5. How should historical Dropped Off and Closed records be divided?
6. What data must accompany a consolidated Dropped Off status?
7. When exactly should a record be considered Active?
8. How will the new structure prevent non-active records from being reported as active?
9. How should multiple LOBs influence the overall patient status?
10. Which reports, list views, workflows, and automations depend on the existing values?
11. Which mappings are safe to automate and which require manual review?
12. What should the final UI look like?
13. Which decisions belong to operations, leadership, or IT?
14. What project-management and communication tools should be used after the process is clear?
15. How should current records be migrated without breaking operational history or reporting?

---



## Bottom Line

The project should now move from a large AI-generated execution environment to a tightly controlled alignment process:

```text
Understand the current lifecycle
→ Compare current and proposed statuses
→ Confirm what is already agreed
→ Surface only unresolved questions
→ Obtain confirmation
→ Map existing data
→ Design the UI
→ Review reports, list views, workflows, and automations
→ Execute through the appropriate technical system
```

Keren’s existing work remains valuable as an internal knowledge base and future implementation resource. The immediate priority, however, is to extract from it only the small number of decisions and questions needed to move the status project forward.