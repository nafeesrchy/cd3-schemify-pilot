# Million Women Study (MWS) — Cohort Description

*Standard pre-schemify brief, per `COHORT_DESCRIPTION_TEMPLATE.md` one level up. Written 2026-09-28, from the raw MWS data dictionary and questionnaire PDFs (`raw_data/`), the Cancer Epidemiology Unit's own public study website, and the CD3 team's own cross-cohort tracking spreadsheets — deliberately independent of the `json_schema/` conversion package that already exists for this cohort, so that this document stands as cohort knowledge on its own, the same way it would if written before that package existed. Where this document's findings differ from the existing package's own notes, that is flagged rather than silently reconciled.*

## 0. At a glance

| Field | Value |
|---|---|
| Cohort name / acronym | Million Women Study (MWS) |
| Recruitment mechanism / governing body | Recruited by post alongside invitations to attend the NHS Breast Screening Programme, at 66 participating centres across England and Scotland; run by the Cancer Epidemiology Unit (CEU), University of Oxford, within the Nuffield Department of Population Health |
| Enrollment period | 1996–2001 |
| Current size (N participants) | 1.32 million recruited (CEU's own published figure, matching CD3's tracker exactly) |
| Age at enrollment (range) | Not stated as a simple age range by CEU; participants were "about one in four of all women born between 1935 and 1950 in the UK," which spans roughly ages 46–66 across the 1996–2001 recruitment window. CD3's own tracker rounds this to 50–64 |
| Sex (%) | 100% female — a women's health study by design |
| Ethnicity breakdown | ~99% White (CD3 tracker figure only — not stated on any CEU page consulted; see §10) |
| Follow-up waves (count, cadence) | 5 postal resurveys confirmed on CEU's own site — 3-year, 8-year, 12-year, 15-year, and 20-year — sent to all surviving participants roughly every 3–5 years, plus continuous NHS-record linkage (§2) |
| TRE / data access model | No accredited TRE yet exists; access today is by a paid Open Access Data application (Data Use Agreement, ~£2,500 GBP) or a formal Collaboration Agreement, with CEU stating publicly that it is "working towards" an accredited TRE (§8) |
| CD3 schemify status | A `json_schema/` package already exists for this cohort (see `json_schema/PROGRESS.md`), covering the baseline, 3-year, and 8-year waves. This document is written independently of that package's own conversion record — as cohort knowledge in its own right, the same way the UKB brief was written before any conversion began |
| Cross-cohort tracker row | `General information/cohort data table.xlsx`, sheet "Summary Table -large", rows "Million Women's Study" / "Million Women's Study (MWS)"; sheet "Cohort info on proposal", row "Million Women's Study (MWS)" |

## 1. What the cohort is

The Million Women Study is one of the largest prospective studies of women's health in the world: 1.32 million UK women were recruited between 1996 and 2001 and have been followed for health outcomes ever since. Women were sent the recruitment questionnaire along with their invitation to attend the NHS Breast Screening Programme, at 66 participating centres across England and Scotland — about one in four of all women born in the UK between 1935 and 1950 joined. The study was originally set up to give reliable evidence on the risks of different types of menopausal hormone therapy, but was designed from the outset to also examine many other lifestyle, environmental, and genetic factors affecting women's health as they age — smoking and oral contraceptive use starting young, rising obesity, and diet among them. It is run by the Cancer Epidemiology Unit (CEU) in Oxford's Nuffield Department of Population Health, led by Professor Gillian Reeves and Associate Professor Sarah Floud, and has been funded mainly by Cancer Research UK and the Medical Research Council.

Participants gave permission at recruitment for continuing follow-up. Electronic linkage using each woman's NHS number provides what CEU describes as "virtually complete" follow-up for deaths, cancer registrations, and hospital admissions. Roughly three years after the baseline questionnaire, and at further intervals of about three to five years after that, participants have been sent postal re-survey questionnaires — CEU's own site links real PDF copies of the 3-year, 8-year, 12-year, 15-year, and 20-year re-survey questionnaires. Some sub-samples have also received additional postal or online surveys, or been approached for related sub-studies: around 52,000 women gave a 10ml blood sample (plasma and buffy coat) through the related "Disease Susceptibility in Women" study, on which CEU states only limited genotyping information is currently available; a small number of participants have also been interviewed about retirement lifestyles for a related study, "Changes to Lifestyle in Retirement." CEU's data-sharing pages describe the study's own ongoing work as centred on cancer, heart disease, stroke, dementia, and other neurodegenerative and mental-health conditions, and note a recent addition — linkage to England's Mental Health Services Dataset — specifically to improve dementia case-finding beyond what hospital admission records alone capture.

**Within CD3:** the team's own metadata-availability review (`General information/Cohort Summary_Data Harmonization.xlsx`, "Metadata Availability") records MWS as having "a good amount of basic information," rating variable-level metadata completeness as "Baseline and Basic Information" only — consistent with what CEU's own public Data Showcase (§3) actually exposes online, and narrower than the fuller six-sheet dictionary the team obtained directly for this pilot. The same review lists MWS's UK-LLC status as "onboarding yet," and a companion sheet records the team's intended harmonization approach for this cohort as "questionnaire-based," comparing dictionary fields directly against the real questionnaire wording and response options.

## 2. Timeline and waves

| Wave / contact | Date range | Mode | What was collected | N invited / participated | Source |
|---|---|---|---|---|---|
| Recruitment questionnaire | 1996–2001 | Postal, alongside NHS Breast Screening Programme invitation, at 66 centres in England and Scotland | Basic demographics, recruitment lifestyle and related variables, self-reported health at recruitment | **1.32 million** | CEU, "Summary of available data" (§9) |
| 3-year re-survey | ~3 years after baseline | Postal | Repeat of selected recruitment variables, dietary variables, wellbeing/social/occupational factors | **869,000** | CEU, "Summary of available data" (§9) |
| 8-year re-survey | ~8 years after baseline | Postal | Repeat of selected recruitment variables, dietary variables; wellbeing/social/occupational factors listed with an estimated availability of Q2 2025 as of CEU's page | **688,000** | CEU, "Summary of available data" (§9) |
| 12-year re-survey | Not stated on the pages consulted | Postal | Not detailed on any CEU page consulted — a real questionnaire PDF exists and is linked from the study site, but its content and N are not in CEU's published "Summary of available data" table | Not stated | CEU, "Recruitment and data collection" (real PDF exists; content undocumented — §10) |
| 15-year re-survey | Not stated on the pages consulted | Postal | Same as above; CEU's site footnotes that one question (Q30) was sourced from an external "Question Bank" item on income | Not stated | Same as above |
| 20-year re-survey | Not stated on the pages consulted | Postal | Same as above | Not stated | Same as above |
| Linked NHS outcome data | Continuously updated; officially cut at 31 December 2020 in CEU's current published summary | Administrative linkage via NHS number | Deaths by cause (ICD-10); cancer registrations by site (ICD-10) and morphology (ICD-O); hospital admissions, diagnoses and procedures (ICD-10, OPCS-4) | Whole cohort | CEU, "Summary of available data" (§9) |
| Disease Susceptibility in Women (blood sample sub-study) | Not stated | Blood draw, one-off | 10ml blood sample (plasma + buffy coat); only limited genotyping currently available | ~52,000 | CEU, "Data Access Policy" (§9) |

A note on precision: this table corrects and considerably extends the internal dictionary's own account. The six-sheet Excel dictionary the CD3 team obtained directly for this pilot (§3) covers only three of these waves — recruitment, 3-year, and 8-year — and CD3's own proposal notes vaguely describe "4 follow up questionnaires," which undercounts what CEU's own site actually documents: five re-survey waves exist (3, 8, 12, 15, and 20-year), each with a real questionnaire PDF linked from the study's own website, but only the first two have any content described in CEU's published "Summary of available data" table. Whether dictionaries comparable to the existing six-sheet workbook exist for the 12-, 15-, and 20-year waves is an open question for the steward (§10).

## 3. Data dictionary anatomy

MWS's documentation exists in two distinct forms, at two different levels of public availability — worth understanding before treating either one as the complete picture.

**A public online Data Showcase** (`datashare.ndph.ox.ac.uk/mws/`), browsable by anyone, modelled visibly on the same style of showcase UK Biobank publishes. As of its own "summary generated" date of 11 April 2023, it exposes only two categories: "Participant information" (7 items) and "Recruitment questionnaire" (59 items) — 66 items in total, covering the recruitment wave only. None of the resurvey waves are represented in the public Showcase at all. Its own legal notice restricts reproducing its content beyond what is needed to describe it here.

**A fuller, hand-maintained Excel workbook** — `millionwomenstudydatadictionary-v1-21.xlsx` (v1.21, dated 05/11/2024) — obtained directly from CEU rather than from the public Showcase, with six sheets covering three waves:

| Sheet | Variables | Wave | What it holds |
|---|---|---|---|
| `Basic information` | 7 | Recruitment | Core demographic fields |
| `Recruitment variables` | 38 | Recruitment | Socioeconomic, anthropometric, behavioural, reproductive/hormonal, breast health, gynaecological surgery |
| `Self-reported health at recruit` | 20 | Recruitment | Baseline medical history and the remainder of breast health |
| `3-year resurvey` | 135 | 3-year | The bulk of the 3-year follow-up questionnaire |
| `Dietary data at 3-year resurvey` | 14 | 3-year | Derived nutrient/food-group daily intakes for the same wave |
| `8-year resurvey` | 38 | 8-year | The entire 8-year follow-up questionnaire — no separate dietary sheet exists for this wave |

All six sheets share the same internal layout: title and version on rows 1–2, a sheet label on row 3, the real header on row 4 (field name split into short/long forms, description, a valid-range column split into from/to, and a per-questionnaire-version availability block), version-year ranges on row 7, and data starting on row 8. Code lists are packed into a single cell as newline-separated `code=label` pairs rather than one row per code. Across all six sheets, 65 + 149 + 38 = **252 variables**.

Neither the public Showcase nor this fuller workbook documents the 12-, 15-, or 20-year resurveys at all, even though CEU's own site confirms all three exist as real, distinct questionnaires (§2). A third kind of source fills part of that gap for the three waves the workbook does cover: the real questionnaire PDFs linked from CEU's own site (`raw_data/mws-Q1.pdf`, `mws-Q3.pdf`, `mws-Q8.pdf` locally) — the actual paper questionnaires, useful for verifying any skip or routing logic directly against the printed wording rather than relying on the dictionary's own notes alone.

## 4. Category / domain map

MWS's dictionary has no single flat category tree the way UK Biobank does — each wave is its own questionnaire with its own set of topic categories, drawn directly from the sheets listed in §3. Laid out here in the same style CD3 uses for the UKB brief, rather than as a nested tree diagram:

### Recruitment wave — 8 categories, 65 variables

| # | Category | Variables |
|---|---|---|
| 1 | Demographics | 5 |
| 2 | Socioeconomic | 3 |
| 3 | Anthropometric | 3 |
| 4 | Behavioural | 5 |
| 5 | Reproductive / Hormonal | 21 |
| 6 | Breast Health | 3 |
| 7 | Gynaecological Surgery | 6 |
| 8 | Medical History | 19 |

### 3-year resurvey — 12 categories, 149 variables

| # | Category | Variables |
|---|---|---|
| 1 | Demographics | 2 |
| 2 | Medical History | 21 |
| 3 | Reproductive / Hormonal | 7 |
| 4 | Medications | 20 |
| 5 | Behavioural | 9 |
| 6 | Anthropometric | 7 |
| 7 | Early Life | 8 |
| 8 | Parental Mortality | 12 |
| 9 | Family History | 27 |
| 10 | Socioeconomic | 15 |
| 11 | Wellbeing / Sleep | 7 |
| 12 | Dietary | 14 |

### 8-year resurvey — 7 categories, 38 variables

| # | Category | Variables |
|---|---|---|
| 1 | Demographics | 2 |
| 2 | Medical History | 16 |
| 3 | Gynaecological Surgery | 2 |
| 4 | Reproductive / Hormonal | 4 |
| 5 | Behavioural | 9 |
| 6 | Anthropometric | 2 |
| 7 | Family History | 3 |

A steward decision worth making deliberately, before any INTAKE interview: CD3's own memory of a prior pilot notes that a new cohort's categories should be proposed in a shape that mirrors CD3's own target schema — the seven domains of Demographics, Socioeconomic, Anthropometric, Behavioural, Reproductive/Hormonal, Medical History, and Screening — rather than derived straight from the source's own sheet names. MWS's own dictionary already happens to name most of its recruitment-wave categories close to that shape, which is a convenient starting point, but the 3-year and 8-year waves introduce several categories (Medications, Early Life, Parental Mortality, Family History, Socioeconomic, Wellbeing/Sleep, Dietary) that don't map onto those seven domains at all — whether those become new top-level domains, or get folded under existing ones, is exactly the kind of proposal this document should put to the steward rather than assume.

## 5. Repeated-measurement / instancing model

MWS's repeat structure is fundamentally different in shape from UK Biobank's single wide-format instancing model, and deserves separate thinking rather than transplanting UKB's approach.

| Repeat structure | Triggered by | Cardinality | Shares shape with |
|---|---|---|---|
| Cross-wave resurvey structure | A fixed calendar schedule from baseline (roughly 3, 8, 12, 15, 20 years), not a participant action | 6 known contacts (recruitment + 5 resurveys), though only 3 have any documented content (§2, §3) | Nothing else in this cohort — each wave is naturally its own table, not an instance column on one shared table |
| Within-wave conditional/skip routing | A trigger question's answer (e.g. "have you ever had any children?") | Enumerable per wave directly from the questionnaire PDFs — a real, bounded set of `if`/`then` relationships, not an open-ended scheme | UK Biobank's structural-skip concept, though MWS's version is small enough to enumerate exhaustively per wave rather than model abstractly |
| Per-wave questionnaire-version scheme | Which printed version of that wave's questionnaire a participant received | Recruitment: 3 named versions; the two documented resurveys: 4 and 2 numeric version codes respectively | UK Biobank's per-field availability flags, in miniature — determines which fields carry a source-documented "not on this questionnaire version" code |
| Multi-select ("tick all that apply") fields | None — these are just checkbox-style items with only a `1=Yes` code documented, no `2=No` | Present across all three documented waves | UK Biobank's `arrayed=1` fields, though the risk here is different: an unticked box can't be told apart from a genuinely unrecorded field, not genuine multi-value repetition |

Two things worth deciding deliberately before conversion work starts, rather than discovering them partway through:

- **No participant-identifier field appears to exist in the dictionary at all**, in any of the six sheets obtained — this is worth confirming directly with CEU rather than assumed, since without one, there is no way to join a participant's row in one wave's table to their row in another, and any schema representation of the cross-wave structure needs to be chosen knowing that constraint up front.
- **The 12-, 15-, and 20-year resurveys are real, confirmed waves with no dictionary yet in hand.** Deciding how repeat measurement will be represented should account for the likelihood that this shape will need to extend to at least three more waves later, rather than being designed narrowly around only the three currently documented.

## 6. Non-participant-grain data

None of MWS's linked administrative data is reachable from either the public Showcase or the six-sheet dictionary — unlike UK Biobank, where linked-record tables are at least named via stub fields inside the main dictionary. Per CEU's own "Summary of available data" page and Data Access Policy, the wider cohort includes:

| Source | Grain | Reachable from the dictionary? |
|---|---|---|
| Deaths, by cause (ICD-10) | One row per death record | No |
| Cancer registrations, by site (ICD-10) and morphology (ICD-O) | One row per registration | No |
| Hospital admissions, diagnoses and procedures (ICD-10, OPCS-4) | One row per hospital episode | No |
| Blood sample genotyping (Disease Susceptibility in Women sub-study, ~52,000 participants) | One row per assay, on a subset | No |

CD3's own tracker separately describes "GP" data and a "bowel cancer screening" linkage for MWS; neither appears on any CEU page consulted for this document, which lists only deaths, cancer registrations, and hospital admissions as the study's currently linked outcome data. This is flagged as an open item (§10) rather than assumed one way or the other. Whichever of this data eventually comes into scope, it needs its own event-grain table, decided deliberately — the same rule UK Biobank's own brief states in its §6 applies here without modification.

## 7. Recommended schemify scope

The complexity-avoidance section — a phased recommendation, not a decision, meant to be put to the steward at intake rather than assumed.

1. **Start with the three waves for which a real dictionary already exists**: recruitment, 3-year resurvey, and 8-year resurvey — 252 variables across 27 categories (§3, §4). This is the only slice of the cohort where field-level documentation is currently in hand.
2. **Before committing to that as the full scope, ask CEU directly whether comparable dictionaries exist for the 12-, 15-, and 20-year resurveys.** All three are real, confirmed waves with a published questionnaire PDF, but none has any documentation in the six-sheet workbook or the public Showcase — starting conversion without asking risks treating a documentation gap as if it were the cohort's actual scope.
3. **Resolve whether a participant-identifier field exists in the source data before modeling any cross-wave relationship.** None of the sheets obtained so far appears to contain one; if confirmed absent, that constrains how (or whether) rows across waves can ever be joined, and is worth knowing before, not after, the table structure is chosen.
4. **Treat the linked NHS outcome data (deaths, cancer registrations, hospital admissions) and the blood-sample genotyping sub-study as a distinct, later-phase scope decision.** Neither is reachable from the dictionary today, and — per §6 — CD3's own tracker's mention of GP and bowel-screening linkages isn't corroborated by CEU's own published data summary, so that scope needs confirming with the data provider before being assumed.
5. **Decide the within-wave skip/routing representation (§5) once, deliberately**, informed directly by the real questionnaire PDFs rather than the dictionary's own notes alone, since MWS's own package precedent elsewhere in CD3 found that printed skip instructions and the dictionary's own inferences didn't always agree.
6. **Expect a multi-sitting effort regardless of exact scope** — even the documented 252-field, 27-category slice is a large, multi-wave conversion, and extending to the undocumented resurveys would add a real discovery phase on top of that.

## 8. Data governance and access

There is currently **no accredited Trusted Research Environment** for MWS. CEU's own "Data access and sharing" page states plainly that the study is "working towards providing external researchers with access to data through an accredited Trusted Research Environment (TRE)" — a future direction, not the current state. Today, access runs through CEU's own Data Access Policy (version S3.3, September 2024): a Requestor submits a Data Access Application specifying the exact variables wanted, is reviewed by MWS's own Data Access Applications Review Panel (meeting roughly every six weeks), and — if approved — receives a pseudonymised, identifier-stripped dataset via a secure remote access platform or encrypted file transfer, governed by a signed Data Use Agreement between the University of Oxford and the requestor's institution. A basic access charge of roughly £2,500 GBP (including VAT) applies per approved request, calculated on a cost-recovery basis. Data can otherwise be obtained through a formal Collaboration Agreement with a named co-investigator inside the MWS team. Real participant-level data has not been obtained for any CD3 schemify work on this cohort; any toy or fixture data must be authored from the dictionary's own stated ranges and code lists, the same rule that applies to every other CD3 cohort.

The source dictionary does not state a single dataset-wide missing-value sentinel. Field-level non-response codes (e.g. `-1` for "not on this questionnaire version") are documented per field where the dictionary states them, and vary by field and wave — an intake process will need to propose, or ask the steward for, a generic fallback sentinel for cells with no field-specific code, since the source dictionary itself doesn't supply one dataset-wide.

## 9. Sources consulted

- `raw_data/millionwomenstudydatadictionary-v1-21.xlsx` (v1.21, dated 05/11/2024) — read and counted directly, 2026-09-28.
- `raw_data/mws-Q1.pdf`, `mws-Q3.pdf`, `mws-Q8.pdf` — the real recruitment, 3-year, and 8-year questionnaire PDFs. Consulted for structure; not re-verified line-by-line for this document.
- Cancer Epidemiology Unit (CEU), "The Million Women Study" — `https://www.ceu.ox.ac.uk/research/the-million-women-study` — cohort overview, PI names, funding, current research focus. Consulted 2026-09-28.
- CEU, "Recruitment and data collection" — `https://www.ceu.ox.ac.uk/research/the-million-women-study/about-the-study/recruitment-and-data-collection` — recruitment mechanism (66 centres, England and Scotland), ethics approvals, resurvey cadence, all five re-survey questionnaire PDFs (3/8/12/15/20-year), the Disease Susceptibility in Women and Changes to Lifestyle in Retirement sub-studies, NHS linkage description, the planned Mental Health Services Dataset linkage. Consulted 2026-09-28.
- CEU, "Summary of available data" — `https://www.ceu.ox.ac.uk/research/the-million-women-study/for-researchers/summary-of-available-data` — exact per-wave N (1.32 million / 869,000 / 688,000), which variable groups are available per wave, the linked-outcomes cutoff date (31 December 2020), and the 8-year wave's pending wellbeing/social/occupational data (estimated Q2 2025). Consulted 2026-09-28.
- CEU, "Data access and sharing" — `https://www.ceu.ox.ac.uk/research/the-million-women-study/for-researchers/data-access-and-sharing` — current data-sharing model, the "working towards an accredited TRE" statement, the Data Showcase link. Consulted 2026-09-28.
- CEU, "Data Access Policy" (version S3.3, September 2024) — `https://www.ceu.ox.ac.uk/research/the-million-women-study/for-researchers/data-access-policy` — HRA reference numbers, the Open Access Data Request process, access fee (~£2,500 GBP), the ~52,000-participant blood-sample sub-study and its limited-genotyping caveat, pseudonymisation and data-security terms. Consulted 2026-09-28.
- MWS Data Showcase — `https://datashare.ndph.ox.ac.uk/mws/` and its category browser — confirms the public showcase currently exposes only the recruitment wave (66 items across 2 categories), last regenerated 11 April 2023. Consulted 2026-09-28.
- CD3 team's own cross-cohort tracking: `General information/cohort data table.xlsx` (sheets "Summary Table -large" and "Cohort info on proposal"), `General information/Cohort Summary_Data Harmonization.xlsx` (sheets "Metadata Availability" and "Metadata compatibility") — read 2026-09-28.

## 10. Open questions for the steward

- **Do dictionaries exist for the 12-, 15-, and 20-year resurveys?** CEU's own site confirms all three exist as real questionnaires (PDFs are linked publicly), but neither the public Showcase nor the six-sheet workbook the team obtained documents any of them. Worth asking CEU directly rather than assuming the study's schemify-relevant scope stops where the current dictionary happens to stop.
- **Does a participant-identifier field exist anywhere in the source data**, even if absent from the sheets obtained so far? This is the single most consequential unresolved question for any cross-wave table design, and cannot be settled from documentation alone.
- **Is CD3's own tracker correct that MWS data includes a GP linkage and a bowel-cancer-screening-programme linkage?** CEU's own published "Summary of available data" lists only deaths, cancer registrations, and hospital admissions as currently linked outcome data — neither GP records nor bowel screening appears there. Worth confirming directly rather than trusting either source uncritically.
- **What is MWS's actual current ethnicity breakdown?** No CEU page consulted states one; CD3's tracker figure of ~99% White is carried forward unverified.
- **Given no accredited TRE exists yet (§8), what does "TRE access" mean for this cohort in CD3's own planning?** CD3's tracker records conflicting entries ("No" in one row, "UK-LLC" onboarding in another) — both are plausibly consistent with CEU's own "working towards an accredited TRE" statement, but the practical implication for how CD3 would actually obtain or work with MWS data (Open Access Data Request vs. Collaboration Agreement vs. a future TRE) is worth settling explicitly before scope decisions assume one route over another.
