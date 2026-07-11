# Funnel definitions (SOC north star)

Lock these definitions with leadership once. Do not re-debate them in weekly reporting. If a definition is disputed, record the disagreement and owner in [stakeholder_decision_map.md](../04_crm_management/stakeholder_decision_map.md) and keep the metric directional or blocked until signed.

Cross-check term language with [ny_home_healthcare_glossary.md](../04_crm_management/ny_home_healthcare_glossary.md) and readiness with [metrics_readiness.md](./metrics_readiness.md).

## Shared funnel

```text
Activity -> Referral -> Intake -> Auth -> SOC -> Retention
```

| Stage | Plain-English definition | What it is | What it is not |
| --- | --- | --- | --- |
| Activity | Marketing effort: visits, calls, events, ads, emails, field touches. | Effort / input | Result |
| Referral | Named patient or referral entering referral work from a source. | Real demand signal | Active census |
| Intake | Ops work to move a referral toward service (docs, eligibility, coordination). | Capacity / process stage | Proof of service |
| Auth | Payer or plan authorization for the relevant service. | Readiness / risk signal | Census or SOC |
| SOC | Start of care: first confirmed billable visit / service start. | True marketing outcome | Anticipated SOC or auth-only |
| Retention | Episode completion, recert, or continued service where relevant. | Source quality over time | Vanity volume |

## Primary scorecard

Measure and compare channels on the same basis:

1. Spend (digital) or fully loaded field hours (liaison / referral development)
2. Referrals
3. SOC
4. Cost per referral
5. Cost per SOC
6. Stage-to-stage conversion (referral → intake → auth → SOC)

**Rule:** CPL alone is not decision-grade. A cheap lead that dies at auth is waste.

## Working CRM path vs business funnel

Nexus and internal language may still use Lead → Qualifying → Referral → Active. Map them to the business funnel above:

| CRM / ops language | Business funnel stage | Reporting stance |
| --- | --- | --- |
| Lead / Qualifying | Pre-referral activity / early demand | Safe as volume + hygiene |
| Referral | Referral | Safe as intake demand |
| Intake work | Intake | Safe as process visibility |
| Authorization coverage | Auth | Directional for readiness; never as census |
| Anticipated SOC | Pre-SOC planning | Stall detection only |
| Confirmed SOC / first service | SOC | Preferred marketing outcome when field is reliable |
| Active | Post-SOC census | Blocked or directional until Active definition is signed |
| Dropped Off Referral | Pre-SOC leakage | Safe as watchlist / trend with drop-usage caveat |
| Discharged | Retention / churn after active service | Blocked until terminal logic is signed |

## Decision rule for leadership packs

- Budget, territory, messaging, and CRM process recommendations should cite **referrals and cost per SOC** when SOC is reliable enough.
- If SOC is not yet trustworthy in CRM extracts, report referral volume + pre-SOC leakage + hygiene as safe, and label SOC / Active conversion as directional or blocked.
- Never present authorized pipeline as active census or as SOC.

## Sign-off checklist

Leadership should confirm:

- [ ] SOC = first confirmed service date (not anticipated SOC, not auth date)
- [ ] Primary channel comparison metric = cost per SOC (with field hours costed equivalently)
- [ ] Unknown / blank source is a defect, not a valid channel
- [ ] Auth is readiness, not census
- [ ] Active census remains blocked until the Active rule is signed

**Owner for sign-off:** Marketing leadership + ops definition owner (see stakeholder map).
