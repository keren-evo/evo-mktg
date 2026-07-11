# Attribution and taxonomy rules

One taxonomy across ads, CRM, field logs, and reporting. Shadow trackers are an efficiency tax—do not create parallel naming systems.

Supports the growth-readiness chain: website → Meta/Facebook/Instagram → lead capture → referral tracking → CRM → leadership reporting. Stage language follows [funnel_definitions.md](../01_reporting_system/funnel_definitions.md).

## Taxonomy acronyms

Use these expansions in CRM picklists, reports, and campaign names so tags stay readable.

| Acronym | Expansion | Where it appears in taxonomy |
| --- | --- | --- |
| ALF | Assisted living facility | Source type `alf` |
| Auth | Authorization (payer/plan approval) | Funnel stage; not a channel |
| CM | Case manager | Contact role on field logs; source type `case_manager` |
| CPL | Cost per lead | Digital efficiency; not primary outcome |
| CPA / cost per SOC | Cost per acquisition / cost per start of care | Primary channel comparison |
| CRM | Customer relationship management (Nexus) | System of record for tags |
| GA | Google Analytics | Digital measurement input |
| Geo | Geography / service area | Taxonomy layer |
| HHC | Home healthcare | Campaign naming (e.g. `nyc_hhc_...`) |
| HIPAA | Health Insurance Portability and Accountability Act | Hygiene constraint on what CRM stores and shares |
| LOB | Line of business | Downstream ops; not a marketing channel |
| MD | Medical doctor / physician | Source type `physician`; contact role |
| MLTC | Managed Long Term Care | Channel `plan_mltc`; source type `mltc_plan` |
| NYIA | New York Independent Assessor | Intake hold; can stall pre-SOC |
| SLA | Service level agreement | Marketing → intake handoff timing |
| SNF | Skilled nursing facility | Source type `snf` |
| SOC | Start of care (first confirmed billable visit) | Marketing outcome; cost per SOC |
| UTM | Urchin Tracking Module (campaign URL tags) | Digital attribution: `utm_source`, `utm_medium`, `utm_campaign`, `utm_content`, `utm_term` |
| CPC | Cost per click | Common `utm_medium` for paid search |

Broader clinical/ops terms: [ny_home_healthcare_glossary.md](../04_crm_management/ny_home_healthcare_glossary.md).

## Master taxonomy

Every marketing record should resolve to these layers:

| Layer | Purpose | Examples |
| --- | --- | --- |
| Channel | How demand was generated | `paid_search`, `paid_social`, `display`, `email`, `website`, `field_liaison`, `facility_hospital`, `physician`, `plan_mltc` (Managed Long Term Care), `community_event`, `other` |
| Source | Named origin account or property | Hospital name, SNF (skilled nursing facility), ALF (assisted living facility), MD (physician) office, case manager (CM), MLTC plan, Meta, Google, organic web |
| Campaign | Initiative / offer / flight | `nyc_hhc_brand_2026q3` (HHC = home healthcare), `brooklyn_snf_outreach_july` |
| Geo | Catchment (geography / service area) | Borough, county, or service area code |
| Creative / tactic | Optional creative or leave-behind ID | Ad set name, one-pager version, video concept ID |

### Channel picklist (canonical)

Use these exact values in CRM and reporting rolls:

1. `paid_search`
2. `paid_social`
3. `display`
4. `email`
5. `website`
6. `field_liaison`
7. `facility_hospital`
8. `physician` (MD offices / groups)
9. `plan_mltc` (Managed Long Term Care plans)
10. `community_event`
11. `other`

`unknown` / blank is a **defect**, not a channel. Count it weekly; do not optimize against it as if it were a segment.

### Source-type picklist (referral accounts)

| Source type | Expansion / typical accounts |
| --- | --- |
| `hospital` | Discharge planning / case management units |
| `snf` | SNF = skilled nursing facility |
| `alf` | ALF = assisted living facility |
| `physician` | MD = medical doctor offices / groups |
| `case_manager` | CM = case manager (independent or agency) |
| `mltc_plan` | MLTC = Managed Long Term Care / managed care plans |
| `community` | Faith, senior center, event partners |
| `digital_property` | Web, Meta, Google (for digital-origin leads) |
| `other` | Everything else, sparingly |

## Required CRM fields (Nexus)

At create (or first marketing touch), require:

| Field | Rule |
| --- | --- |
| Lead Source / Channel | Required; must match channel picklist |
| Campaign Name | Required when channel is paid, email, or named initiative |
| Referral Source | Required for referral-stage records; link to account when possible |
| Owner | Required; liaison or marketing owner |
| Stage | Required; current funnel/CRM stage |
| Next action | Required for open records |
| Next action due | Required when next action is set |
| First touch | Set once; never overwrite |
| Last touch | Update on meaningful subsequent touches |

### Optional but recommended
- Geo / service area
- Creative or collateral ID
- Handoff timestamp (marketing → intake)
- Handoff status

## Attribution rules

1. Every lead must have channel + (campaign when campaign-eligible).
2. Every referral must have a referral source (account or named source).
3. Never manually overwrite original / first-touch source.
4. Digital: UTM `source` / `medium` / `campaign` / `content` map to channel, campaign, creative.
5. Field: every touch logs facility/account, contact role, outcome, owner, geo.
6. Same campaign name string in ad platforms and CRM.
7. Separate consumer/caregiver digital traffic from referral-partner traffic when both exist.
8. Cost allocation for cost per referral / cost per SOC uses this taxonomy only.

## UTM conventions

```text
utm_source   = platform or partner (google, meta, newsletter)
utm_medium   = channel family (cpc, paid_social, email, referral)
utm_campaign = campaign ID matching CRM Campaign Name
utm_content  = creative / variant ID
utm_term     = keyword (paid search only)
```

Broken or missing UTMs are same-day defects on the daily pulse.

## Handoff rules (marketing → intake)

| Signal | Definition | Reporting use |
| --- | --- | --- |
| Handoff time | Timestamp when marketing marks ready for intake | SLA and aging |
| Handoff status | Accepted / returned / stalled | Leakage and accountability |
| Stale open | Open past SLA with no stage move or next action | Weekly CRM defect |

Stale open pipeline is a visible metric, not a feeling.

## Common defects (weekly count)

- Missing channel / source
- Missing campaign on campaign-eligible records
- Missing referral source on referrals
- Duplicate leads
- First-touch overwrite
- Incorrect campaign string vs ads
- Field activity without account/outcome
- Open record with blank next action

## Success test

Every SOC can be traced to a channel and, ideally, a referral source—without a hero spreadsheet rebuild.
