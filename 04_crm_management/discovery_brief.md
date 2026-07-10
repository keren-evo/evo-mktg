# CRM analytics discovery brief

## Objective

Improve CRM analytics without outrunning the team's actual decision-making pace.

This brief assumes the immediate job is not to finalize the whole New York home healthcare status model. The immediate job is to make reporting more trustworthy, make uncertainty visible, and create a cleaner path for future CRM decisions.

## Current reality

- The CRM is trying to answer too many business questions with overlapping status labels.
- `Authorized` is not the same as `Active`, and current reporting appears to overstate active volume when those concepts are merged.
- Service-line logic, intake logic, terminal outcomes, and patient-level lifecycle are being mixed together.
- There is still enough stability to improve attribution visibility, follow-up discipline, referral flow reporting, and data-quality monitoring right now.

## What can move now

- Lead and referral volume reporting.
- Source, campaign, and referral-source completeness.
- Follow-up overdue watchlists.
- Pre-active leakage watchlists.
- Status contradiction queues.
- KPI readiness labeling in reports and scorecards.

## What should stay blocked or caveated

- True active census.
- Authorized as a census proxy.
- Final discharge reporting.
- Retention and line-of-business reporting that depends on unsettled service-line rules.

## Working contribution model

- Use evidence before redesign.
- Treat draft architecture documents as inputs, not approvals.
- Separate facts, assumptions, open questions, and owner-held decisions.
- Publish small, trusted reporting improvements before proposing larger CRM changes.

## Deliverables created

- Fact register: [fact_register.md](./fact_register.md)
- Glossary: [ny_home_healthcare_glossary.md](./ny_home_healthcare_glossary.md)
- Stakeholder and decision map: [stakeholder_decision_map.md](./stakeholder_decision_map.md)
- Low-risk wins: [low_risk_wins.md](./low_risk_wins.md)
- KPI dictionary: [../01_reporting_system/kpi_dictionary.md](../01_reporting_system/kpi_dictionary.md)
- Metric readiness split: [../01_reporting_system/metrics_readiness.md](../01_reporting_system/metrics_readiness.md)
- Updated daily report: [../01_reporting_system/daily_report.md](../01_reporting_system/daily_report.md)
- Updated weekly report: [../01_reporting_system/weekly_report.md](../01_reporting_system/weekly_report.md)

## Suggested next use

1. Use the updated daily and weekly templates for live reporting.
2. Fill the fact register only with evidence, not opinion.
3. Start the first cleanup queue with missing source, missing campaign, and overdue follow-up.
4. Keep blocked metrics visible as blocked instead of hiding the uncertainty.
