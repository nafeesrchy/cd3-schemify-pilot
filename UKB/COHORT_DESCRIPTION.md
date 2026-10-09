# UK Biobank (UKB) — Cohort Description

*Standard pre-schemify brief, per `COHORT_DESCRIPTION_TEMPLATE.md` one level up. Written 2026-09-28, from the raw UK Biobank Showcase dictionary files (`raw_data/`), the CD3 team's own cross-cohort tracking spreadsheets, and UK Biobank's public/academic documentation — deliberately independent of any schemify conversion work, so it stands as cohort knowledge on its own.*

## 0. At a glance

| Field | Value |
|---|---|
| Cohort name / acronym | UK Biobank (UKB) |
| Recruitment mechanism / governing body | Population-based volunteer cohort, recruited via NHS patient registers at 22 assessment centres across England, Wales and Scotland; run by the UK Biobank charity |
| Enrollment period | 2006–2010 (recruitment window; CD3's own tracker rounds this to 2006–2011) |
| Current size (N participants) | 503,317 recruited at baseline (source: UK Biobank's own "Our participants" page, section 9) |
| Age at enrollment (range) | 40–69 (24% aged 40–49, 34% aged 50–59, 42% aged 60–69 at recruitment) |
| Sex (%) | 54% female, 46% male (per NHS records) |
| Ethnicity breakdown | 94.6% White; the remainder spans all other ethnic groups (UK Biobank's own published figure — see section 9) |
| Follow-up waves (count, cadence) | 4 in-person assessment-centre contacts (section 2) plus several independent sub-study/questionnaire/linkage streams (section 5) — **not** a simple single-track "baseline + N resurveys" design |
| TRE / data access model | Own Trusted Research Environment; participant-level data never leaves it (section 8) |
| CD3 schemify status | Not started — this document is the pre-schemify brief |
| Cross-cohort tracker row | `General information/cohort data table.xlsx`, sheet "Summary Table -large", row "UKBiobank (UKB)"; sheet "Cohort info on proposal", row "UK Biobank (UKB)" |

## 1. What the cohort is

UK Biobank recruited 503,317 adults aged 40–69 between 2006 and 2010 through NHS patient registers, with the explicit design goal of a large, deeply-phenotyped, linkage-enabled resource for research into the causes of major diseases of later life. Participants attended an assessment centre at recruitment (touchscreen questionnaire, verbal interview, physical measures, biological sampling) and have since been invited back for further in-person visits, online follow-up questionnaires, and a growing set of sub-studies (accelerometer wear, COVID-19 serology/symptom tracking, repeat online cognitive testing). The cohort is linked to national health records (hospital admissions, cancer and death registrations, primary care in participating regions) and has extensive genomic, proteomic and metabolomic data on some or all participants. Official documentation: UK Biobank Showcase (`https://biobank.ndph.ox.ac.uk/showcase/`) and `https://www.ukbiobank.ac.uk/about-our-data/`.

Within CD3, UK Biobank is tracked as one of the consortium's larger, better-documented resources — the team's own metadata-availability review (`General information/Cohort Summary_Data Harmonization.xlsx`) rates it "full variable-level documentation" via the Showcase schema export, with the caveat "can't access the structural metadata [directly] — via the website Showcase instead." CD3-relevant data per the team's own linkage/data-summary notes (`General information/Cohort info on LoS.xlsx`): online questionnaires, anthropometry, genetics, biomarkers, activity monitors, and health linkages (hospital, cancer, death). In progress or planned per the same notes: enhanced cancer staging/grade/morphology/treatment data for England/Wales/Scotland (1975–2021, expected 2025), tumour genomics from the 100,000 Genomes Project, a digital histopathology imaging pilot, medication dispensing data, and breast/bowel cancer screening programme linkage.

## 2. Timeline and waves

Two genuinely different things get called "waves" in UK Biobank, and conflating them is the first place a data-modeling exercise goes complex unnecessarily: the **in-person assessment-centre contacts** below are one specific repeat-measurement scheme among several — section 5 has the full list (diet questionnaire rounds, COVID sub-studies, accelerometer seasons, and more each run on their own independent schedule).

| Wave / contact | Date range | Mode | What was collected | N invited / participated | Source |
|---|---|---|---|---|---|
| Initial assessment visit | 2006–2010 | Clinic (22 assessment centres) | Recruitment consent, touchscreen questionnaire, verbal interview, physical measures, biological sampling — the bulk of the participant-grain dictionary | 503,317 recruited | UK Biobank, "Our participants" (official, section 9) |
| First repeat assessment | 2012–2013 | Clinic | Subset re-invited; repeats a portion of the baseline measures | ~20,000 attended (figures of 20,323–20,348 are quoted across different published variables/analyses; UK Biobank has not published one single canonical total for this wave) | Fry et al. and related published UK Biobank analyses (section 9) |
| Imaging visit | Piloted 2014 (~7,000 scanned); main phase from 2016 | Clinic (4 dedicated imaging centres) | Brain, cardiac, abdominal, DXA and carotid ultrasound imaging, plus a repeat of many baseline measures | Reached its 100,000-participant target; milestone announced 15 July 2025. Recruitment is continuing beyond that target | UK Biobank news release, "100,000 volunteers provide science with look inside the body," 15 Jul 2025 (section 9) |
| First repeat imaging visit | Launched 2022; ongoing, expected completion 2029 | Clinic | Repeat imaging on a subset of the imaging cohort, ≥2 years after their first imaging visit | Target 60,000 of the 100,000 imaged; ~20,000 attended as of the most recent published figures (not yet complete) | UK Biobank news release (as above) and published repeat-imaging cohort-profile literature (section 9) |
| Diet questionnaire (5 rounds) | Recruitment tail-end (clinic, partial) + 4 online cycles, Feb 2011–Jun 2012 | Clinic (partial) + web | 24-hour dietary recall, repeated up to 5 times | Most participants were **not** offered the clinic round — it was introduced only late in recruitment; no official round-by-round N is published | `raw_data/instances.txt`, `insvalue.txt` |
| Online follow-up questionnaires | Ongoing, multiple rounds since recruitment | Web | Mental health, digestive health, diet, work, pain, sleep, food preferences, and more — UK Biobank's largest single non-imaging domain by field count | Self-selected responders per questionnaire round; varies by topic | `raw_data/field.txt`, `category.txt` |
| Linked health records | Continuously updated | Administrative linkage | Hospital admissions (HES), cancer registrations, death registrations, primary care (subset) | Whole cohort, updated on a rolling basis | `raw_data/record_table.txt` |

Note on precision: UK Biobank does not publish one single authoritative table giving an exact N for every wave. Section 10 flags the most reliable way to pin these numbers down exactly, if an exact figure is later needed (rather than the literature/news-release estimates used here).

## 3. Data dictionary anatomy

UK Biobank publishes its dictionary as the **Showcase schema export**: a set of tab-separated tables (`https://biobank.ndph.ox.ac.uk/ukb/scdown.cgi?fmt=txt&id=N`), available locally as 18 files in `raw_data/`. Row counts below were counted directly from those files (2026-09-28):

- **`field.txt`** — 11,821 rows, one per `field_id`. This is the primary variable inventory. Its `item_type` column splits it: `0` = **Data** (11,271 rows — ordinary values, the realistic conversion scope), `20` = **Bulk** (424 rows — pointers to external files: imaging, raw genetic data, not simple values), `30` = **Records** (112 rows — stub flags announcing a participant has rows in a separate linked-record table, section 6), `10` = 14 rows of undocumented meaning (section 10). `main_category` joins to `category.txt`; `encoding_id` joins to `encoding.txt`; `instance_id` joins to `instances.txt` (section 5).
- **`category.txt`** (410 rows) + **`catbrowse.txt`** (362 parent→child edges) — the topic hierarchy (section 4). Confirmed a strict tree: every category has exactly one parent, so category names/paths are unambiguous.
- **`encoding.txt`** (858 rows) names every code list a field can reference; the actual code→label pairs live in six further tables split by value type: `esimpint.txt` (18,078 rows, flat integer codes), `esimpstring.txt` (439,346 rows, by far the largest file — flat string-coded lists such as drug names or free-text-derived codes), `esimpreal.txt` (17), `esimpdate.txt` (18), `esimptime.txt` (3) for flat lists; `ehierint.txt` (28,900 rows) and `ehierstring.txt` (46,927 rows) for hierarchical coding trees (e.g. ICD-10, ICD-9, OPCS-4 procedures, occupation codes, clinical Read/CTV3 codes).
- **`instances.txt`** (12 rows) + **`insvalue.txt`** (33 rows) — describe every repeat-measurement scheme (section 5).
- **`record_table.txt`** (35 rows) + **`record_column.txt`** (417 rows) — describe the linked-record tables reachable only through a stub flag in `field.txt` — a different grain entirely (section 6).
- **`recommended.txt`** (1,975 rows) and **`related.txt`** (9,280 rows) are secondary: interface hints and prose cross-references between fields, not primary variable sources.
- **`fieldsum.txt`** (11,646 rows) is a near-duplicate of `field.txt`'s own `field_id`/`title`/`item_type` columns — a cross-check, not a distinct source.

If working from a newer copy than the local `raw_data/` files, refresh from `https://biobank.ndph.ox.ac.uk/ukb/schema.cgi` (the table index) — UK Biobank updates the Showcase export on an ongoing basis as new fields and data releases land.

## 4. Category / domain map

UK Biobank's own `catbrowse.txt`/`category.txt` category tree has **8 true top-level roots** (categories that are never a child of another category). Field counts below are **Data-typed fields only** (`item_type=0`), counted directly from `field.txt` against each root's full sub-tree, 2026-09-28.

| Root domain | Immediate sub-domains (Data-typed fields each) | Data-typed fields, total | Notes |
|---|---|---|---|
| Population characteristics | *(fields sit directly on this category — no further split)* | 39 | Basic recruitment/administrative characteristics |
| Health outcomes | COVID-19 sub-studies (174); Externally sourced health outcomes (2,468) | 2,642 | "Externally sourced" is mostly hospital/death/cancer-registry-derived outcome flags, organized largely as ICD-chapter "first occurrence" groups |
| Cardiac image-derived phenotype classifications | 6 sub-categories | 0 | An alternative regrouping view only — every field it would contain already sits under Imaging below; contributes no fields of its own |
| Assessment centre | Recruitment (25); Touchscreen (396); Cognitive function (134); Verbal interview (36); Physical measures (263); Eye measures (414); **Imaging (3,865)**; Biological sampling (10); Procedural metrics (76) | 5,219 (1,354 excluding Imaging) | The dictionary's largest root by far; Imaging alone is ~74% of it |
| Biological samples | Blood assays (962); Saliva assays (0); Sample inventory (0); Urine assays (16) | 978 | "Saliva assays" and "Sample inventory" currently hold no Data-typed fields under them |
| Additional exposures | Local environment (48); Physical activity measurement / accelerometer (209); Cardiac monitoring (106) | 363 | |
| Online follow-up | Social interactions and focus (143); Sleep (186); Mental well-being (210); Health and well-being (157); Cognitive function online (77); Diet by 24-hour recall (473); Digestive health (57); Experience of pain (132); Food and other preferences (154); Mental health (143); Work environment (101) | 1,833 | Second-largest root; "Diet by 24-hour recall" alone outsizes any other single sub-domain here |
| Genomics | 8 sub-categories | 197 | |

These 8 roots together account for all 11,271 Data-typed fields in the dictionary (39+2,642+0+5,219+978+363+1,833+197 = 11,271). Bulk (424) and Records (112) items, plus the 14 undocumented `item_type=10` rows, are flagged via `field.txt`'s own `item_type` column rather than living outside this category tree — they sit inside these same 8 roots (mostly Imaging, for Bulk) but are not Data-typed values.

## 5. Repeated-measurement / instancing model

This is the section most worth reading before any conversion work starts on this cohort — UK Biobank's dictionary defines **11 distinct instancing dictionaries** (`instances.txt`), not one. A field's `field.txt` row states `instanced` (does it repeat at all) and, if so, `instance_id` (*which* of these schemes governs it) — two different fields both flagged `instanced=1` can repeat under completely different schedules.

| instance_id | What it groups | Indices (`insvalue.txt`) | Cardinality |
|---|---|---|---|
| 2 | **The four in-person assessment-centre visits** — what people usually mean by "UK Biobank waves" | 0=init (2006–10), 1=rep1 (2012–13), 2=img (2014+), 3=irep1 (2019+) | 4, ordinal, non-equal spacing |
| 1 | Diet questionnaire rounds | 0=clinic (2009–10, partial), 1–4=web1–web4 (2011–12) | 5, ordinal |
| 12 | COVID-19 serology sample waves | 0–5 = w1–w6 | 6, ordinal |
| 27 | COVID-19 symptom questionnaire returns | 0–8 = s1–s9 | 9, ordinal |
| 93 | Accelerometer wearing | 0=main study, 1–4=seasonal repeats 1–4 | 5, ordinal |
| 154 | COVID-19 lateral-flow device tests | 0=1st test, 1=repeat test | 2, ordinal |
| 178 | Online cognitive assessment run | 0=2014, 1=2021 | 2, ordinal |
| 604 | Vaccination events | no fixed index (`insvalue.txt` has no rows for it) | variable, per-participant event count |
| 693 | Grouping for items on the same case report | no fixed index | variable |
| 9000001 | Death registry reports | no fixed index | variable, per-participant event count |
| 9000002 | Cancer registry reports | no fixed index | variable, per-participant event count |
| 0 | Dummy null instance | — | not real data — a referential-integrity placeholder |

Two things worth deciding deliberately before any conversion work starts, rather than discovering mid-way:

- **Multi-select fields add a second repeat layer.** `arrayed=1` fields (e.g. "which of the following conditions has a doctor told you that you have") can hold several codes *within* a single instance — independent of, and stacking with, the instancing above.
- **Real UK Biobank data extracts (inside the TRE) are wide CSV, one column per field-visit** — e.g. `54-0.0`, `54-1.0`, `54-2.0`, `54-3.0` for a field repeating across the four assessment-centre visits — not a single column holding a list of visits. Any schema representation of repeat measures should be chosen with this real extract shape in mind from the start; retrofitting it later means redoing every already-converted repeating field.

## 6. Non-participant-grain data

35 linked-record tables (`record_table.txt`), each one row per *event*, not one row per *participant* — a different grain from everything in sections 4–5:

| Group | Tables | Grain |
|---|---|---|
| HES (hospital inpatient) | 7 (`hesin` core, critical care, delivery, diagnoses, maternity, operations, psychiatric) | one row per hospital episode/diagnosis/procedure |
| Death register | 2 (`death`, `death_cause`) | one row per death record/cause |
| GP (primary care) | 3 (`gp_clinical`, `gp_registrations`, `gp_scripts`) | one row per GP event |
| COVID-19 | 4 (`covid19_misc`, plus England/Scotland/Wales test-result tables) | one row per test/result |
| Vaccination | 1 (`covid19_vaccination`) | one row per vaccination event |
| OMOP (standardized clinical model) | 16 | one row per clinical event, OMOP-vocabulary coded |
| Olink (proteomics assay batches) | 2 (`olink_control`, `olink_data`) | one row per assay run |

These 35 tables are reachable from `field.txt` only through 112 "stub" fields (`item_type=Records`) that merely flag a participant has rows in one of them — none of the 417 real columns inside them (`record_column.txt`) appear in `field.txt` itself. Any of this data brought into a schema needs its own table(s) at the matching event grain — it should never be folded into a participant-grain table it doesn't belong in.

## 7. Recommended schemify scope

The complexity-avoidance section — a phased recommendation, not a decision, meant to be put to the steward at intake rather than assumed:

1. **Start with participant-grain survey/assay/outcome data only** — the 7 non-empty domains outside Imaging (Population characteristics, Health outcomes, Assessment centre minus Imaging, Biological samples, Additional exposures, Online follow-up, Genomics): 39+2,642+1,354+978+363+1,833+197 = **7,406 of the dictionary's 11,271 Data-typed fields**.
2. **Exclude Imaging (3,865 Data-typed fields) and Cardiac image-derived phenotype classifications (0 fields — a pure regrouping view) from a first pass.** Imaging alone is roughly half the size of the reduced 7,406-field scope again, and mostly complex derived image phenotypes rather than simple survey items.
3. **Exclude Bulk (424, external file pointers) and Records (112, stub flags into the event-grain tables in section 6) items** — neither is a plain value to encode.
4. **Decide the repeat-measurement representation (section 5) once, deliberately, up front** — informed by the real wide-CSV extract shape — rather than picking it implicitly on whichever field happens to be converted first.
5. **Treat the 35 linked-record tables (section 6) as a distinct, later-phase scope decision**, not an afterthought — if they come into scope, plan them at their own event grain from the start.
6. **Expect a multi-sitting effort regardless of exact scope** — even the reduced 7,406-field scope is roughly two orders of magnitude larger than a small single-sheet cohort dictionary.

## 8. Data governance and access

No UK Biobank participant-level data leaves its own Trusted Research Environment (TRE) — any toy/fixture data used downstream must be authored from the dictionary's own stated ranges and code lists, never sampled from real extracts.

UK Biobank defines no single dataset-wide missing-value sentinel. Per-field non-response codes (e.g. `-1` "Do not know", `-3` "Prefer not to answer", `-7` "None of the above") are real, source-documented, and vary by field/encoding — an intake process will need to propose, or ask the steward for, a generic fallback sentinel for cells with no field-specific code, since the source dictionary itself doesn't supply one dataset-wide.

## 9. Sources consulted

- `raw_data/field.txt`, `category.txt`, `catbrowse.txt`, `encoding.txt`, `instances.txt`, `insvalue.txt`, `record_table.txt`, `record_column.txt`, and the remaining Showcase export files — read and counted directly, 2026-09-28.
- CD3 team's own cross-cohort tracking: `General information/cohort data table.xlsx` (sheets "Summary Table -large" and "Cohort info on proposal"), `General information/Cohort Summary_Data Harmonization.xlsx`, `General information/Cohort info on LoS.xlsx` — read 2026-09-28.
- UK Biobank, "Our participants" — `https://www.ukbiobank.ac.uk/about-our-data/our-participants/` — official baseline recruitment count (503,317), demographics (age bands, 54% female, 94.6% White ethnicity). Consulted 2026-09-28.
- UK Biobank, "The UK Biobank Repeat Imaging Project" — `https://www.ukbiobank.ac.uk/taking-part/participant-opportunities/imaging-project/the-uk-biobank-repeat-imaging-project/` — repeat-imaging phase description, 60,000 target. Consulted 2026-09-28.
- UK Biobank news release, "100,000 volunteers provide science with look inside the body" (15 July 2025) — `https://www.ukbiobank.ac.uk/news/record-breaking-human-imaging-project-crosses-the-finish-line/` — imaging pilot (2014, ~7,000), main phase (2016+), 100,000-participant milestone, repeat-imaging launch (2022) and expected completion (2029). Consulted 2026-09-28.
- UK Biobank Showcase, Data-Field 53 ("Date of attending assessment centre") — `https://biobank.ndph.ox.ac.uk/ukb/field.cgi?id=53` — cross-check: 501,938 participants, 646,251 total records across its 4 defined instances combined (consistent with the per-wave estimates above, which sum to ~646,000). Consulted 2026-09-28.
- Published UK Biobank cohort-profile and methods literature (e.g. "Cognitive Test Scores in UK Biobank," PLOS One, and the touchscreen dietary questionnaire evaluation in PMC) — used for the first-repeat-assessment (2012–13) attendance figures, since UK Biobank's own participant-facing pages do not state a single total for that wave. Consulted 2026-09-28.

## 10. Open questions for the steward

- **Exact per-wave attendance figures.** UK Biobank does not publish one single canonical table of N per assessment-centre visit; section 2's rep1/img/irep1 figures are drawn from academic literature and news releases, not one authoritative source. If an exact figure is required, the most reliable route is UK Biobank's own `field.txt` `num_participants`/`item_count` for a field collected at every visit (e.g. field 53, "Date of attending assessment centre"), cross-tabulated by instance from a real extract inside the TRE — not something derivable from the public dictionary alone.
- **The repeat-measurement representation (section 5)** — which shape to model repeating fields in should be settled once, informed by the real wide-CSV extract format, before any instanced field is converted.
- **Whether/when the 35 linked-record tables (section 6) come into scope**, and if so, whether they belong in the same package as the participant-grain data or a separate one entirely.
- **The 14 `field.txt` rows with `item_type=10`** are undocumented in the Showcase schema tables themselves — worth checking the Showcase's own per-field pages or asking UK Biobank directly before scoping them in or out.
