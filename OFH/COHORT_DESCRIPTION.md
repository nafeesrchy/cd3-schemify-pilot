# Our Future Health (OFH) — Cohort Description

*Standard pre-schemify brief, per `COHORT_DESCRIPTION_TEMPLATE.md` one level up. Written 2026-09-28, from the raw OFH data dictionary, codings, and questionnaire-logic files (`raw_data/`), Our Future Health's own public website, and the CD3 team's own cross-cohort tracking spreadsheets — deliberately independent of the `json_schema/` conversion package that already exists for this cohort, so that this document stands as cohort knowledge on its own. A sibling pilot's own progress notes (MWS's `PROGRESS.md`) describe OFH as "not started" — that turns out to be stale; a substantial package already exists (§0, §10). Where this document's findings differ from CD3's own tracker, that is flagged rather than silently reconciled.*

## 0. At a glance

| Field | Value |
|---|---|
| Cohort name / acronym | Our Future Health (OFH) |
| Recruitment mechanism / governing body | Open volunteer sign-up (any UK resident aged 18+), supplemented by invitation letters sent by NHS England; run by Our Future Health, a public–charity–private collaboration funded in part by UK Research and Innovation, life sciences companies, and disease-related charities, working closely with the NHS |
| Enrollment period | Recruiting on a rolling basis; CD3's own tracker gives two different start years (2022 in one sheet, 2023 in another) and no OFH page consulted states one directly (§10). Ultimate target: "up to five million" participants |
| Current size (N participants) | **802,998** completed the baseline questionnaire, per OFH's own published data release 6 (19 March 2024) — CD3's own tracker figure of 1,500,000 is the programme's long-term recruitment target, not the current recruited count (§10) |
| Age at enrollment (range) | 18+, no stated upper bound; the real observed distribution in release 6 runs from 18 to 80+, concentrated at ages 50–69 (45.2% of participants) |
| Sex (%) | 56.2% female, 43.7% male, 0.0% (389 people) intersex/other/prefer not to answer (release 6 figures) |
| Ethnicity breakdown | 80.6% White British, plus a detailed 16-category breakdown (§9); Asian ≈5.7% (matches CD3's own tracker figure exactly); Black ≈1.6%; Mixed 1.8% |
| Follow-up waves (count, cadence) | One baseline questionnaire only, so far. The TRE's data holdings refresh every 3 months, and OFH describes a re-contactable "translational research platform" as one of its two main research resources — but neither is a scheduled resurvey wave yet (§2) |
| TRE / data access model | A real, accredited Trusted Research Environment (TRE) is the default access route today, governed by an Access Board, the ONS Five Safes framework, UK GDPR, and ISO 27001 accreditation (external assessor: Dionach Ltd); other TREs can also be accredited to host the data (§8) |
| CD3 schemify status | A substantial `json_schema/` package already exists — 26 tables spanning participant, questionnaire, clinic and lipid measurements, geography reference data, 10 linked-NHS administrative tables, and 3 genomic datasets. This document is written independently of that package's own record, as cohort knowledge in its own right, the same way the UKB and MWS briefs were |
| Cross-cohort tracker row | `General information/cohort data table.xlsx`, sheet "Summary Table -large", rows "Our Future Health (OFH)"; sheet "Cohort info on proposal", row "Our Future Health (OFH)"; sheet "working table", row "Our Future Health (OFH)" |

## 1. What the cohort is

Our Future Health is a UK-wide volunteer health research programme aiming to bring together up to five million adults, to build one of the largest and most detailed pictures of the nation's health ever assembled — helping researchers find new ways to prevent, detect, and treat disease earlier. It is a public–charity–private collaboration, funded in part by UK Research and Innovation, life sciences companies, and disease-related charities, and works closely with the NHS.

Any UK resident aged 18 or over can join directly online; NHS England also sends invitation letters to eligible adults, which participants can opt out of receiving. Joining involves three steps: signing a consent form (5–15 minutes), completing an online lifestyle and health questionnaire (30–45 minutes, split across sections that don't need to be finished in one sitting, with no question mandatory), and attending a clinic appointment for a blood sample and physical measurements including blood pressure (15–30 minutes). Since December 2023, participants who complete the questionnaire and give a blood sample have received a £10 voucher.

As of the most recent published data release (release 6, 19 March 2024), 802,998 people had completed the baseline questionnaire, of whom 66,520 (8.3%) also had genotyping array data available. The baseline questionnaire itself has been fielded in two versions — version 1, completed by 6.4% of participants, and version 2, completed by the remaining 93.6% — with materially different question sets for reporting health history specifically (§3, §5).

**Within CD3:** the team's own metadata-availability review (`General information/Cohort Summary_Data Harmonization.xlsx`, "Metadata Availability") already independently identifies OFH's five-way structure — Participant, Questionnaire, Clinical, Genetic, NHS Linked — rating it "good amount of information," available as an Excel download plus website, though noting "no single-file data dictionary" and keyword search rather than a browsable index. The same review records OFH's access route as its "Own TRE," distinct from UK-LLC. A companion sheet ("Metadata compatibility") notes the questionnaire's socioeconomic, lifestyle, family, and health domains are documented with exact wording, making the dictionary and coding file usable together for variable discovery and value-level coding.

## 2. Timeline and waves

| Wave / contact | Date range | Mode | What was collected | N invited / participated | Source |
|---|---|---|---|---|---|
| Baseline consent, questionnaire, and clinic visit | Rolling recruitment since ~2022 (ongoing) | Online consent + online questionnaire + in-person clinic appointment | Registration/consent metadata and demographics (14 vars); the baseline questionnaire itself (359 vars, §3–§4); clinic measurements including blood pressure (34 vars); point-of-care lipid profile from the blood sample (19 vars) | 802,998 completed baseline questionnaire (release 6, 19 Mar 2024); target up to 5,000,000 | OFH "Characteristics" doc v5; OFH data dictionary |
| Genotyping array | Processed after the clinic visit, same recruitment window | Laboratory assay on the blood sample | 686,416 genotyped variants per participant | 66,520 (8.3%) as of release 6 | OFH data dictionary, `genetic_data` sheet; "Characteristics" doc |
| Imputed genotype data | Computed from the genotyping array | Computational derivation | 159,587,100 imputed variants per participant | Not stated as a separate participant count — a derived dataset, not a new data-collection contact | OFH data dictionary, `genetic_data` sheet |
| Linked NHS health records | Continuously updated | Administrative linkage | 10 distinct linked datasets spanning cancer pathways/registry/treatment, A&E attendances (two eras), inpatient episodes, outpatient appointments, primary-care medicines, and deaths (England & Wales) — full detail in §6 | Whole linked subset of the cohort | OFH data dictionary, `linked_nhse_health_records` sheet |
| TRE data refresh | Every 3 months | Administrative | New data added to the TRE on a rolling cadence | Whole cohort | OFH, "Researchers" page (§9) |
| Future re-contact / translational research platform | Not yet scheduled | Re-contact for further studies | Described as one of OFH's two main research resources, but no defined recall wave exists yet in anything consulted | Not applicable yet | OFH, "Researchers" page (§9) |

A note on precision: OFH's own public "Characteristics" document is the single most precise and current source consulted for this brief — it states the exact release number (6) and exact release date (19 March 2024) it describes, unlike any UKB or MWS page consulted for those cohorts' briefs. CD3's own tracker's "1,500,000" figure describes the programme's long-term recruitment target, not the current recruited count, and should not be read as the current N (§10).

## 3. Data dictionary anatomy

OFH's dictionary is structurally different from both UK Biobank's flat Showcase export and MWS's per-wave spreadsheet: it is explicitly relational. A README sheet inside the workbook itself states its own purpose and documents a real participant identifier, `PID`, that "all datasets link via" — every table is designed from the outset to join back to a single participant record, unlike MWS (where no such field appears to exist at all — an open question there) and unlike UK Biobank's stub-field mechanism, which only partly bridges participant- and event-grain data.

The dictionary — `our_future_health_data_dictionary_v14.xlsx` (v14) — has a README plus 7 data sheets, three of which each bundle several distinct logical entities under one shared column layout (`entity`, `name`, `type`, `primary_key_type`, `coding_name`, `is_sparse_coding`, `is_multi_select`, `referenced_entity_field`, `relationship`, `folder_path`, `title`, `units`, `description`):

| Sheet | Entities held | Variables | What it holds |
|---|---|---|---|
| `participant` | `participant` | 14 | Registration and consent metadata, demographics |
| `questionnaire` | `questionnaire` | 359 | Self-reported baseline questionnaire (§4) |
| `clinic_measurements` | `clinic_measurements` | 34 | In-clinic physical measurements |
| `poct_lipid_profile` | `poct_lipid_profile` | 19 | Point-of-care lipid panel from the blood sample |
| `participant_geographies` | `country_region` (4), `lsoa` (3), `msoa` (3), `intermediate_zones` (3) | 13 | Geographic reference/lookup entities for England, Wales, Scotland, and Northern Ireland |
| `linked_nhse_health_records` | 11 entities (§6) | 568 | NHS England (and England & Wales, for deaths) administrative linkage data |
| `genetic_data` | Genotype array data (15), Imputed genotype data (13), Genetic ancestry data (3) | 31 | Genomic data descriptions — a different column layout (`Dataset`, `entity`, `file`, `vcf_field`, and others) from every other sheet |

Across all sheets: 14 + 359 + 34 + 19 + 13 + 568 + 31 = **1,038 documented variables** — a total that, unlike UKB and MWS, spans four genuinely different grains at once (participant, event, geography lookup, and genomic sample) rather than being scoped narrowly to participant-grain survey data (§6).

Two companion files sharpen this further. `our_future_health_codings_v14.xlsx` (v14, ≈15MB) carries its own README plus one coding sheet per dictionary sheet — the `lsoa` coding sheet alone has 35,673 rows, matching England and Wales's real count of Lower Layer Super Output Areas, and the `linked_nhse_health_records` coding sheet has 328,833 rows, reflecting the size of the coded terminologies (ICD-10, OPCS-4, BNF, and similar) those NHS datasets use. `Our Future Health Baseline Questionnaire Logic v2.2.xlsx` (v2.2) is a dedicated branching-logic specification with five section sheets (`section1`–`section5`) plus an overview sheet — giving this cohort something neither UKB nor MWS has: a machine-readable skip-logic file, rather than logic that has to be inferred from a PDF questionnaire.

## 4. Category / domain map

Unlike MWS's sheets, the raw dictionary's own `questionnaire` entity carries no internal category column — its 359 variables sit as one flat list. The five-section structure OFH's own "Characteristics" document describes (about you, work and education, lifestyle, family health history, health history) is the natural grouping, and the Logic workbook's five section sheets appear to correspond to it, though this document does not confirm the exact section-to-sheet mapping.

| Category (proposed) | Variables |
|---|---|
| Questionnaire metadata (version, completion) | 4 |
| About you / household | 21 |
| Work and education | 15 |
| Lifestyle | 117 |
| Family health history | 74 |
| Medical / health history | 128 |
| **Total** | **359** |

This six-way split matches the questionnaire entity's total exactly, and — cross-checked against the existing `json_schema/` package for this cohort — is the same split that package already adopted, apparently independently arrived at from the same public documentation this brief consulted.

A decision worth making deliberately, before intake: this split is not stated anywhere in the raw dictionary itself — it is a proposal, not a fact the source states. Whether to adopt these same six categories, or restructure them to better mirror CD3's own target domains (as CD3's own prior-pilot experience recommends doing relative to the MWS categories' shape) is exactly the kind of question this document should put to the steward rather than assume. OFH's six-way split and MWS's eight-domain recruitment-wave split don't obviously line up one-to-one, and reconciling them — or deciding deliberately not to — is an intake decision, not something to default into.

## 5. Repeated-measurement / instancing model

OFH's repeat structure looks nothing like either UKB's or MWS's, for one central reason: it already has a real, dictionary-documented participant identifier tying every entity together.

| Repeat structure | Triggered by | Cardinality | Notes |
|---|---|---|---|
| Cross-entity linking via `PID` | Every dictionary entity | Not applicable | All 26 real entities across all four grains (§6) link back to a single participant record via `PID` — the opposite situation from MWS, where the absence of any such key is flagged as the single largest open risk in that cohort's own brief |
| Questionnaire version (v1 vs v2) | Which version a participant was fielded | 2 versions; 6.4% v1 / 93.6% v2 | Materially different question sets for reporting health history specifically — the closest OFH analogue to MWS's per-wave questionnaire-version schemes |
| Multi-select ("tick all that apply") fields | The dictionary's own `is_multi_select` column flags these directly | Not separately counted for this document | Unlike UKB and MWS, OFH's dictionary states explicitly, per field, whether it is multi-select — a structural advantage worth using directly rather than inferring from question wording |
| Future re-contact / translational studies | Not yet defined | Not yet defined | Described as one of OFH's two main research resources, but nothing consulted defines an actual recall wave's structure |

Two things worth deciding deliberately before conversion starts, rather than discovering them partway through:

- **Confirm exactly how the Logic workbook's five section sheets map onto the questionnaire's five named public sections, and onto the existing package's six category files**, before treating any one of the three as authoritative on its own — this document found them consistent in total count, but did not verify a sheet-by-sheet correspondence.
- **Decide how the questionnaire's v1/v2 variation gets represented in the schema** — a single unioned shape, two distinct sub-schemas, or something else — since the two versions genuinely diverge in health-history reporting rather than being simple supersets of one another, per OFH's own published note.

## 6. Non-participant-grain data

Unlike MWS (where none of this is reachable from the dictionary at all) and UK Biobank (reachable only through 112 stub flags), OFH's dictionary documents its non-participant-grain data directly and fully, at three distinct additional grains.

### Linked NHS administrative data (event grain) — 11 entities, 568 variables

| Entity | What it holds | Variables |
|---|---|---|
| `nhse_eng_canpat` | Cancer pathways data | 12 |
| `nhse_eng_canreg_pattumour` | Cancer treatment data, tumour-level | 49 |
| `nhse_eng_canreg_pre1995` | Cancer registry, tumours diagnosed 1 Jan 1985 – 31 Dec 1994 | 9 |
| `nhse_eng_canreg_treat` | Cancer data by treatment event, tumour from 1 Jan 1995 | 22 |
| `nhse_eng_ecds` | Major A&E attendances, England, on/after 1 Apr 2020 | 167 |
| `nhse_eng_ed` | Major A&E attendances, England, 1 Apr 2007 – 31 Mar 2020 | 91 |
| `nhse_eng_inpat` | Inpatient hospital episodes, England | 108 |
| `nhse_eng_outpat` | Outpatient appointments, England, from 1 Apr 2003 | 55 |
| `nhse_eng_primcare_meds` | Primary-care dispensed medicines, England, from 1 Apr 2018 | 33 |
| `nhse_engwal_deaths` | Death registration / mortality, England & Wales | 20 |
| `participant_nhs_linked` | Flags participants successfully linked to an NHS number | 2 |

### Geography reference / lookup data — 4 entities, 13 variables

| Entity | What it holds | Variables |
|---|---|---|
| `country_region` | Country / region: England, Wales, Scotland, Northern Ireland | 4 |
| `lsoa` | Lower Layer Super Output Areas, England & Wales | 3 |
| `msoa` | Middle Layer Super Output Areas, England & Wales | 3 |
| `intermediate_zones` | Intermediate Zones, Scotland (Scotland's LSOA/MSOA equivalent) | 3 |

### Genomic data (sample grain) — 3 entities, 31 variables

| Entity | What it holds | Variables |
|---|---|---|
| Genotype array data | 686,416 genotyped variants per participant | 15 |
| Imputed genotype data | 159,587,100 imputed variants per participant | 13 |
| Genetic ancestry data | Inferred via a Global Ancestry Estimation workflow (Genomics Ltd) | 3 |

None of these three additional grains has a confirmed Northern Ireland small-area geography equivalent — the dictionary's own geography entities cover England, Wales, and Scotland only, which is worth flagging given OFH's own representativeness note describes weighting results back to all four UK nations, Northern Ireland included (§8, §10).

## 7. Recommended schemify scope

The complexity-avoidance section — a phased recommendation, not a decision, meant to be put to the steward at intake rather than assumed.

1. **Start with the participant-grain resources the dictionary documents fully and cleanly**: `participant` (14 vars), `questionnaire` (359 vars across its natural six-way split, §4), `clinic_measurements` (34 vars), `poct_lipid_profile` (19 vars) — 426 variables total, all joinable via the dictionary's own `PID`.
2. **Confirm the questionnaire's category/domain split with the steward before converting.** The six-way split already used elsewhere in CD3 (§4) is a reasonable starting proposal, but hasn't been confirmed against CD3's own target-schema shape the way MWS's categories were.
3. **Treat the geography-lookup tables (13 vars, §6) as reference/dimension data**, not participant-grain — small, stable, and low-risk to include early, but modeled as lookup tables joined by area code rather than folded into the participant table.
4. **Defer the 11-entity, 568-variable linked NHS administrative data (§6) to a distinct, later-phase decision.** Even though the dictionary documents it fully, it is the single largest slice of this cohort's dictionary, and spans data of wildly different scale per entity (from 2 to 167 variables).
5. **Defer the genomic data (31 variables across 3 entities, plus the enormous imputed-variant file itself) to its own distinct phase** — a fundamentally different kind of data (per-variant, not per-question) that neither UKB's nor MWS's brief needed to grapple with directly.
6. **Decide how the questionnaire's v1/v2 variation is represented (§5) before converting the questionnaire entity**, since the two versions genuinely diverge rather than being simple supersets.
7. **Expect a large, multi-sitting effort regardless of exact scope** — even the reduced 426-field participant-grain slice is comparable in size to MWS's entire finished 252-field, three-table package, and the full 1,038-field dictionary is larger still.

## 8. Data governance and access

OFH provides participating researchers with a real, accredited Trusted Research Environment (TRE) as the default access route — a materially different situation from MWS, which has none yet, and closer in kind (though independently built) to UK Biobank's own TRE model. Access requires researcher registration (credential and training checks), a signed data-governance agreement, and Access Board approval of the specific research study before any data can be viewed; approved access is time-limited to the approved study period, and no data may be removed from the TRE except research results. Other TREs can also become accredited to host de-identified OFH data, assessed against ISO 27001, the ONS Five Safes framework, and UK GDPR by an external assessor, Dionach Ltd. New data is added to the TRE on a rolling three-month cycle.

The dictionary does not appear, from what was reviewed for this document, to state a single dataset-wide missing-value sentinel — the `is_sparse_coding` column suggests some fields use a distinct sparse-coding convention, but its exact meaning was not confirmed here. An intake process will need to establish this directly from the coding file or ask the steward, rather than assume UKB's or MWS's own missingness conventions carry over.

OFH's own published note on representativeness states plainly that the cohort, being volunteer-recruited, is not expected to be fully representative of the UK population, and that OFH plans to publish sampling weights (derived from recruitment-partner and UK Census data) to allow weighting results back to the UK, England, Scotland, Wales, and Northern Ireland populations — worth keeping in mind for any downstream analysis guidance CD3 provides alongside a converted schema.

## 9. Sources consulted

- `raw_data/our_future_health_data_dictionary_v14.xlsx` (v14) — read directly, including its own README sheet, 2026-09-28.
- `raw_data/our_future_health_codings_v14.xlsx` (v14) — sheet structure and row counts read directly, 2026-09-28.
- `raw_data/Our Future Health Baseline Questionnaire Logic v2.2.xlsx` (v2.2) — sheet structure read directly, 2026-09-28.
- `raw_data/Our Future Health Baseline Questionnaire v1.pdf` — noted as the real paper/PDF form of the questionnaire; not read line-by-line for this document.
- Our Future Health, "Characteristics of Our Future Health participants," document version 5, describing TRE data release 6 (released 19 March 2024) — linked from CD3's own tracker (`https://a.storyblok.com/f/228028/x/458ef91045/our_future_health_cohort_characteristics_v5.pdf`) — exact participant counts, demographics, socioeconomic and lifestyle summary statistics, the representativeness note. Consulted 2026-09-28.
- Our Future Health, homepage — `https://ourfuturehealth.org.uk/` — programme overview, "up to five million" target, recruitment steps. Consulted 2026-09-28.
- Our Future Health, "Taking part" — `https://ourfuturehealth.org.uk/get-involved/taking-part/` — recruitment mechanism (open sign-up plus NHS England invitation letters), consent/questionnaire/clinic steps and timings, £10 voucher scheme. Consulted 2026-09-28.
- Our Future Health, "Researchers" — `https://ourfuturehealth.org.uk/get-involved/researchers/` — TRE as default access route, 3-month data-release cadence, currently available data types, key protocol documents. Consulted 2026-09-28.
- Our Future Health, "How we make data available for research" — `https://ourfuturehealth.org.uk/protecting-your-data/how-we-make-data-available-for-research/` — Access Board approval process, TRE accreditation for external environments, Dionach Ltd, the Five Safes framework. Consulted 2026-09-28.
- Our Future Health, "About us" — `https://ourfuturehealth.org.uk/about-us/` — funding model, governance. Consulted 2026-09-28.
- CD3 team's own cross-cohort tracking: `General information/cohort data table.xlsx` (sheets "Summary Table -large", "Cohort info on proposal", "working table", "OFHCondition Category 1M 2M 3M"), `General information/Cohort Summary_Data Harmonization.xlsx` (sheets "Metadata Availability", "Metadata compatibility"). Read 2026-09-28.
- The existing `json_schema/` package's own category files, read only to cross-check variable counts against the raw dictionary (§4, §6) — not used as a source of cohort facts, consistent with this document's pre-schemify framing.

## 10. Open questions for the steward

- **What is OFH's actual enrollment start date?** CD3's own tracker gives two different years (2022 in one sheet, 2023 in another); no OFH page consulted states one directly.
- **CD3's own tracker's "Current Size" figure of 1,500,000 is the programme's long-term target, not the current recruited count** (802,998 as of release 6) — worth correcting in the tracker itself so future readers don't conflate the two.
- **How does the Logic workbook's five section sheets map onto the questionnaire's five named public sections, and onto the existing package's six category files?** Not confirmed directly in this document.
- **Does the dictionary's `is_sparse_coding` convention define a missing-value/sentinel scheme, or something else entirely?** Needs checking directly against the coding file, or asking the steward, before intake assumes either interpretation.
- **How does a participant's record join to the geography lookup tables** (`country_region`/`lsoa`/`msoa`/`intermediate_zones`)? Presumably via a small-area code on the participant or questionnaire record, but this document did not confirm the exact join field.
- **Why do the dictionary's geography entities cover only England, Wales, and Scotland**, when OFH's own representativeness note describes weighting results back to Northern Ireland as well? Is Northern Ireland small-area data simply not yet in the dictionary, or handled differently?
- **Whether/when the 568-variable linked NHS administrative data and the genomic data should come into CD3's own schemify scope** — both are already fully documented in the source dictionary, unlike the equivalent gaps flagged for UKB and MWS, so the blocker here is a scope decision, not a documentation gap.
