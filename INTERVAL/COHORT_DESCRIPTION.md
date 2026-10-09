# INTERVAL — Cohort Description

*Standard pre-schemify brief, per `COHORT_DESCRIPTION_TEMPLATE.md` one level up. Written 2026-09-28, from the two raw INTERVAL data-request-form dictionaries, the INTERVAL study's own public website, and the CD3 team's own cross-cohort tracking spreadsheets — deliberately independent of the earlier, differently-conventioned schema work that already exists for this cohort elsewhere in the repository (§3, §10), so that this document stands as cohort knowledge on its own. Like EPIC-Oxford, this cohort has no `raw_data/` folder yet under the canonical `Harmonization/CD3_Schemify_Pilot/` location (§10).*

## 0. At a glance

| Field | Value |
|---|---|
| Cohort name / acronym | INTERVAL — a randomised controlled trial and biomedical resource in blood donors |
| Recruitment mechanism / governing body | Blood donors recruited at 25 permanent NHS Blood and Transplant (NHSBT) donation clinics across England. Set up by the Universities of Cambridge and Oxford in collaboration with NHSBT; overseen by a Steering Committee, a Management Group, and a Data Monitoring Committee |
| Enrollment period | June 2012 – June 2014 (the study's own site states recruitment started June 2012 and reached its 50,000-participant target exactly two years later, in June 2014) |
| Current size (N participants) | **50,000** — the only cohort among CD3's pilots so far where the study's own current public figure matches CD3's tracker exactly, with no staleness detected |
| Age at enrollment (range) | 17+ per CD3's own tracker; not independently restated on any INTERVAL page consulted |
| Sex (%) | CD3's own tracker: 50% women. Not independently corroborated on any INTERVAL page consulted |
| Ethnicity breakdown | CD3's own tracker: 81% White, 9% Other (the two figures sum to 90%, not 100% — a gap in the tracker's own row, not resolved anywhere else) |
| Follow-up waves (count, cadence) | This is a **randomised trial**, not a simple resurvey design: participants are randomised to standard or reduced blood-donation intervals over a 2-year period, give a research blood sample at enrolment and again after 2 years, and complete an online questionnaire every 6 months (6/12/18/24 months). A subset continued into Phase II (extended follow-up to June 2016, adding 30/36/42/48-month questionnaires) and a further ~4,000 into Phase III (extra blood samples at every donation, to study iron/haemoglobin recovery kinetics) (§2) |
| TRE / data access model | **No dedicated TRE of INTERVAL's own.** De-personalised data and samples are shared via secure file transfer after approval by a formal Data Access Committee (comprising study leads and public members), under the "Blood Donors Studies BioResource." Separately, INTERVAL also participates in the **UK Longitudinal Linkage Collaboration (UK LLC)**, which does provide its own TRE for cross-study linked-administrative-data research — both routes are real and simultaneously true, resolving what looked like a contradiction in CD3's own tracker (§8) |
| CD3 schemify status | An earlier, differently-conventioned schema-generation effort exists in `Harmonization/Harmonised Cohort Schemas (legacy)/CD3_INTERVAL_Schema/` (26 auto-generated JSON Schema files, ~1,539 variables, no category files, no routing, no steward-review record) — this document is written independently of that effort, the same way the UKB, MWS, OFH, LOLIPOP, EPIC-Oxford, and Genes & Health briefs were |
| Cross-cohort tracker row | `General information/cohort data table.xlsx`, sheets "Cohort info on proposal", "Summary Table -large", "Summary Table - small", "Ethnicity" — row "INTERVAL" / "INTERVAL (blood donors)" |

## 1. What the cohort is

INTERVAL is, first and foremost, a randomised controlled trial — a genuinely different design from every other CD3 pilot cohort so far, which are all observational. It was set up by the Universities of Cambridge and Oxford in collaboration with NHS Blood and Transplant to find the safest interval between blood donations, and whether that interval should be tailored by age, sex, genetic profile, or other characteristics. Recruitment ran from June 2012 to June 2014 at 25 permanent NHSBT donation clinics across England, reaching its target of 50,000 participants exactly on schedule.

On joining, each participant was randomised to either a standard donation interval (12 weeks for men, 16 weeks for women) or a reduced one (10 or 8 weeks for men; 14 or 12 weeks for women), and was asked to attend donation appointments at that assigned interval for two years. Participants gave a small research blood sample on enrolment and again after two years — specifically to compare iron status between more- and less-frequent donors — and completed an online questionnaire every six months throughout the trial (at 6, 12, 18, and 24 months). Everyone consented at enrolment to long-term linkage with their medical and other health-related records, to anonymised long-term storage and reuse of their data for future ethically-approved research, and to being contacted up to three times a year about further studies run by NHSBT or the two universities.

The trial extended in two further phases, both continuations of the original cohort rather than new recruitment. **Phase II** invited all participants to keep donating at their assigned interval beyond the original two years, through to a new end date of June 2016, adding four more six-monthly questionnaires (30, 36, 42, 48 months) — participants who donated at the Brentwood centre could not be invited, because that centre was due to close in March 2015. **Phase III** separately recruited roughly 4,000 existing participants (those without a current donation deferral and with enough time left on the study) to give an extra small blood sample at every remaining donation appointment, specifically to study how haemoglobin and iron stores recover between successive donations, rather than only at the two-year mark.

Beyond the trial's own data collection, INTERVAL's data has since been linked to: deaths and cancer diagnoses (NHS England), Hospital Episode Statistics (NHS England), diabetes records (NHS England), and — specifically for COVID-19 research — GP records, vaccination records (NHS England), and COVID-19 diagnosis and outcome data (UK Health Security Agency). The study's own site states plans to extend this further and notes it is separately in the process of requesting UKHSA infection data. The de-identified combination of all of this — trial data, biological samples, and linked records — is made available to other researchers as the **Blood Donors Studies BioResource** (§8).

**Within CD3:** no dedicated metadata-availability review row for INTERVAL was found in `General information/Cohort Summary_Data Harmonization.xlsx` — the same gap noted for EPIC-Oxford and Genes & Health; this cohort's harmonization approach hasn't yet been formally assessed there either.

## 2. Timeline and waves

| Wave / contact | Date range | Mode | What was collected | N invited / participated | Source |
|---|---|---|---|---|---|
| Enrolment / randomisation | June 2012 – June 2014 | In-clinic, at 25 NHSBT donation centres | Basic demographics, randomisation to a donation-interval arm, donation history, adverse-event history; a research blood sample | 50,000 recruited | INTERVAL study site, homepage and "What is involved?" (§9) |
| Baseline questionnaire | At enrolment | Online | 106 variables — height/weight (self-reported), diet, alcohol, smoking, and related lifestyle items | Whole cohort | Legacy schema plan (§9, §10) |
| Follow-up questionnaires (6, 12, 18, 24 months) | Every 6 months through the original 2-year trial | Online | General health status, activity limitation, and (from 18 months) an expanded set of lifestyle and wellbeing items — the 24-month wave is markedly larger (209 variables) than the others | Whole cohort, response rate not stated | Legacy schema plan (§9, §10) |
| 2-year research blood sample | ~2 years after enrolment | In-clinic | A repeat research sample, to compare with the enrolment sample | Whole cohort | INTERVAL, "What is involved?" (§9) |
| Cognitive testing, physical activity monitoring | Alongside the 24-month contact | In-clinic test / wearable device | Cognitive test scores (pairs, fluid IQ, Stroop); accelerometer-derived physical activity data | Not stated | Legacy schema plan (§9, §10) |
| Phase II follow-up questionnaires (30, 36, 42, 48 months) | 2015–June 2016 | Online | Continuing the same general-health item set; the 48-month wave is again markedly larger (177 variables) | All original participants except those donating at the Brentwood centre (closing March 2015) | INTERVAL, "INTERVAL Phase II" (§9) |
| Phase III extra blood samples | Ongoing through each participant's remaining time on the trial | In-clinic, at every remaining donation | An additional small blood sample at each donation, to study haemoglobin/iron recovery between donations | ≈4,000 selected participants | INTERVAL, "INTERVAL Phase III" (§9) |
| Linked health records | Continuously updated, by consent | Administrative linkage | Deaths, cancer, HES, diabetes (NHS England, all participants); GP records, vaccination records, COVID-19 diagnosis/outcome (NHS England / UKHSA, COVID-research-specific) | Whole cohort, by consent | INTERVAL, "Electronic Health Record Linkage" (§9) |

A note on precision: this is the one cohort among CD3's pilots so far where the study's own published enrolment figure (50,000) matches CD3's tracker exactly, with no staleness or discrepancy found. The follow-up questionnaires' exact response rates, and Phase III's exact current participant count, are not stated on any page consulted.

## 3. Data dictionary anatomy

INTERVAL's documentation is delivered as two Excel **data request form templates** — not a plain data dictionary, but the form the study team uses to process a researcher's request for specific variables — one per phase of the trial:

| File | Sheets | Variables | Covers |
|---|---|---|---|
| `dataRequestForm_PHASE1_EXT_Template_v3.xlsx` | 17 (16 data sheets + 1 overview) | 868 | The original 2012–2014 trial: enrolment, the baseline and four 6-monthly questionnaires, cognitive testing, physical activity, donation and adverse-event history, biomarkers, blood assays, omics platform metadata, and linked EHR data |
| `dataRequestForm_PHASE234_EXT_Template_v2.xlsx` | 11 (10 data sheets + 1 overview) | 671 | Phase II's four further questionnaires (30/36/42/48 months) plus Phase II/III's own versions of cognitive tests, adverse events, outcomes, blood assays, biomarkers, and omics |

Both share the same row-per-variable layout (`Variable_name`, `Description`, `Time_point`, and either a `Categories` or `Units` column, plus a `Requested` column for the researcher to mark which variables they want) — this is a request template, not a fixed source dictionary, so its own structure reflects "what can be requested," not necessarily "everything the study holds." Across both files: 868 + 671 = **1,539 documented variables**. A real participant identifier exists throughout — `donorID`, the unique blood-donor identifier — unlike EPIC-Oxford, where no equivalent field exists at all.

One coding quirk worth flagging directly: the source states `monthPulse` (month of blood collection) only as the shorthand "1–12 = January – December" rather than spelling out each value — the earlier schema-generation work for this cohort chose to expand this into an explicit, unambiguous code list rather than carry the shorthand forward, a reasonable normalisation worth keeping in mind as a precedent, not a source fact in itself.

## 4. Category / domain map

Phase 1 and Phase 2/3/4 use their own dictionaries, so the two are listed separately; several sheet names recur across both because they are genuinely the same kind of data collected again in the later phase.

### Phase 1 (2012–2014) — 16 sheets, 868 variables

| Sheet | Variables | What it holds |
|---|---|---|
| `basicInfo` | 14 | Demographics and administrative fields (sex, birth date, donor centre, blood group, and similar) |
| `questionnaire_bl` | 106 | Baseline lifestyle questionnaire (self-reported height/weight, diet, alcohol, smoking) |
| `questionnaire_6m` / `_12m` / `_18m` / `_24m` | 57 / 58 / 72 / 209 | Six-monthly follow-up questionnaires — general health, activity limitation, and (18m onward) an expanding set of lifestyle/wellbeing items |
| `cognitiveTest` | 9 | Cognitive test scores (pairs, fluid IQ, Stroop) |
| `physicalActivity` | 22 | Accelerometer file metadata and derived activity measures |
| `donationHistory` | 12 | Blood donation history before and during the study |
| `outcomes` | 4 | Donation/deferral outcome counts |
| `adverseEventHistory` | 10 | Pre-existing adverse-event history (bruising, rebleeds, fainting, and similar) |
| `adverseEvents` | 18 | Adverse events occurring during the study |
| `biomarkers` | 43 | Haematological biomarkers (e.g. CRP, ferritin) |
| `bloods` | 184 | Full blood-count and related assay results |
| `omics` | 45 | Genotyping and sequencing platform/QC metadata |
| `EHRData` | 5 | Linked-record endpoint flags (cancer registry, ONS mortality, GP) |

### Phase 2/3/4 (2015–2016+) — 10 sheets, 671 variables

| Sheet | Variables | What it holds |
|---|---|---|
| `questionnaire_30m` / `_36m` / `_42m` | 83 / 83 / 83 | Continuing six-monthly follow-up questionnaires |
| `questionnaire_48m` | 177 | The largest single Phase II questionnaire, again expanding the item set |
| `P234_cognitiveTest` | 9 | Cognitive test scores, repeated at 48 months |
| `P234_adverseEvents` | 18 | Adverse events during Phase II/III |
| `P234_outcomes` | 4 | Donation/deferral outcome counts, Phase II/III |
| `P234_bloods` | 186 | Blood assay results, including Phase III's additional per-donation samples |
| `P234_biomarkers` | 22 | Biomarkers, Phase II/III (a narrower panel than Phase 1's 43) |
| `P234_omics` | 6 | Omics metadata, Phase II/III (RNA sequencing, where Phase 1 was genotyping/exome-focused) |

A decision worth making deliberately, before any conversion work starts: the earlier schema-generation work for this cohort kept Phase 1 and Phase 2/3/4 as entirely separate schema files with no cross-referencing, even where a sheet name recurs (e.g. `bloods` vs. `P234_bloods`). Whether a future conversion should model these as one longitudinal table per topic (joined by `donorID` and time point) or keep them separate, the way the source templates themselves are organised, is exactly the kind of proposal intake should put to the steward rather than assume.

## 5. Repeated-measurement / instancing model

INTERVAL's repeat structure combines a genuine randomised-trial design with a conventional longitudinal questionnaire schedule — a combination none of CD3's other pilot cohorts has.

| Repeat structure | Triggered by | Cardinality | Notes |
|---|---|---|---|
| Donation-interval randomisation | Assignment at enrolment | 1 of up to 4 possible intervals per sex (2 for men: 10 or 8 weeks reduced, plus the 12-week standard; 2 for women: 14 or 12 weeks reduced, plus the 16-week standard) | This is the trial's actual randomised exposure — worth representing explicitly rather than folding into a generic "questionnaire" field, since it is the variable the whole study exists to test |
| Six-monthly questionnaire waves | A fixed schedule from each participant's own enrolment date | 4 waves in Phase 1 (6/12/18/24m) + 4 more in Phase II (30/36/42/48m) = 8 known waves, all sharing the `donorID` key across files | Each wave grows: baseline is 106 variables, but the 24-month and 48-month waves balloon to 209 and 177 respectively, suggesting substantial item additions at those specific contacts rather than a stable repeated instrument |
| Enrolment / 2-year research blood samples | Fixed trial design (2 samples per participant, by default) | 2, for the core trial; more for Phase III | The Phase III extension turns this into an open-ended series (a sample at every remaining donation) for its ~4,000 selected participants — a materially different cardinality from the rest of the cohort |
| Phase extension (Phase I → II → III) | Not a per-participant repeat, but a re-plan of the whole study's scope over time | 3 named phases | Phase II is a time extension of the same participants under the same design; Phase III is a nested sub-study on a subset — worth keeping these two kinds of "phase" conceptually distinct rather than treating all three phases as equivalent waves |

Two things worth deciding deliberately before any conversion work starts, rather than discovering them partway through:

- **The randomisation arm itself should be modelled as a first-class variable**, not incidentally reconstructed from a donation-frequency field — it is the trial's defining exposure, and the source dictionaries do not obviously flag it as special.
- **Phase II and Phase III are not the same kind of "extra data."** Phase II extends the same measurement schedule to the same participants over a longer calendar period; Phase III adds a structurally different, higher-frequency sampling scheme to a much smaller subset. Conflating the two risks miscounting who was actually measured, and how often.

## 6. Non-participant-grain data

| Source | Grain | Reachable from either dictionary? |
|---|---|---|
| Deaths and cancer diagnoses (NHS England) | One row per record | Only as flag-style endpoints in `EHRData` (Phase 1) — 5 variables total, not the underlying event-level records |
| Hospital Episode Statistics (NHS England) | One row per hospital episode | No |
| Diabetes records (NHS England) | One row per record | No |
| GP records, vaccination records (NHS England, COVID-specific) | One row per event | No |
| COVID-19 diagnosis and outcome (UK Health Security Agency) | One row per record | No |
| UK LLC-linked administrative data (health, education, employment, tax, benefits, environmental context) | Varies by dataset | No — accessible only inside UK LLC's own separate TRE (§8) |

As with UK Biobank's own stub-field mechanism, INTERVAL's `EHRData` sheet flags that linked-record data exists without exposing any of the underlying event-grain fields — a partial, not total, documentation gap, closer to UKB's situation than to MWS's or EPIC-Oxford's complete absence. Whichever of this data eventually comes into CD3's scope needs its own table at the matching grain, decided deliberately from a direct conversation with the study team rather than assumed from the stub flags alone.

## 7. Recommended schemify scope

The complexity-avoidance section — a phased recommendation, not a decision, meant to be put to the steward at intake rather than assumed.

1. **Establish `Harmonization/CD3_Schemify_Pilot/INTERVAL/raw_data/` as this cohort's canonical location before starting any conversion work**, copying in both data-request-form templates from wherever the steward confirms is the current authoritative copy.
2. **Start with Phase 1's core participant-grain data**: `basicInfo`, the five questionnaire waves, `cognitiveTest`, `physicalActivity`, `donationHistory`, `outcomes`, and the two adverse-event sheets — 868 variables total, all joinable via `donorID`.
3. **Decide up front how to represent the randomisation arm (§5)** as an explicit, first-class variable, since it is the trial's defining feature and neither source dictionary flags it specially.
4. **Decide whether Phase 1 and Phase 2/3/4 should be modelled as one longitudinal set of tables or kept separate**, as the source templates themselves are organised (§4) — this is a real design choice, not something to default into.
5. **Treat Phase III's extra per-donation blood samples as a distinct sub-study with its own cardinality**, not simply "more bloods data" folded into the main schedule (§5) — it applies to a much smaller, specifically selected subset.
6. **Treat the linked NHS/UKHSA administrative data, and the separate UK LLC-linked data, as a distinct, later-phase scope decision** (§6) — the `EHRData` sheet only flags that linkage exists, and the UK LLC's own linked datasets are not reachable from anything held locally at all.
7. **Expect a large, multi-sitting effort regardless of exact scope** — even Phase 1 alone (868 variables) is comparable in size to OFH's entire participant-grain slice, and the combined 1,539-variable dictionary is one of the largest among CD3's pilots so far.

## 8. Data governance and access

INTERVAL has **no Trusted Research Environment of its own**. Data collected during the trial is de-personalised (personal identifiers replaced with an anonymous study ID, held separately in a password-protected link table managed by the University of Cambridge School of Clinical Medicine) and stored in a restricted-access study database. Sharing this de-personalised data and biological samples with other researchers happens through the **Blood Donors Studies BioResource**: a formal Data Access Committee — comprising the study's own senior investigators and members of the public — reviews each application, and approved researchers receive only the specific data items their project needs, delivered by secure file transfer rather than through an online analysis platform. The University of Cambridge is the Data Controller, processing health data (a special category under GDPR) under the university's public-task legal basis, Articles 6(1)(e) and 9(2)(j).

Separately, INTERVAL is a partner study in the **UK Longitudinal Linkage Collaboration (UK LLC)** — a cross-study research resource created in 2019, run by the Universities of Bristol, Edinburgh, and Swansea together with the NHS and the Office for National Statistics. INTERVAL provides UK LLC with an anonymised copy of its data and, separately, participants' personal identifiers, so that UK LLC can establish linkage to administrative data (health, education, employment, tax, benefits, and environmental-context records such as air pollution or broadband access) inside **UK LLC's own TRE**. INTERVAL remains the Data Controller throughout and retains control over which of its participants' records enter UK LLC and which research teams may use them. These two access routes — the BioResource's own Data Access Committee process, and UK LLC's separate TRE — are both real and simultaneously true, which resolves what otherwise looks like a contradiction in CD3's own tracker (one entry marking "No" TRE access, another marking "Yes, UK-LLC").

No missing-value or sentinel convention is stated as a single dataset-wide rule in either data-request-form template; the earlier schema-generation work for this cohort treated `null` as a generic system-missing marker throughout, which — as with the other CD3 pilots — is a package-level convention rather than something either source template itself states.

## 9. Sources consulted

- `Harmonization/Original Cohort Metadata and Schemas/INTERVAL/dataRequestForm_PHASE1_EXT_Template_v3.xlsx` and its duplicate at `Harmonization/Harmonised Cohort Schemas (legacy)/CD3_INTERVAL_Schema/raw_data/` — read via the earlier schema-generation work's own exploration report, 2026-09-28.
- `Harmonization/Original Cohort Metadata and Schemas/INTERVAL/dataRequestForm_PHASE234_EXT_Template_v2.xlsx` and its duplicate — same. Read 2026-09-28.
- `Harmonization/Harmonised Cohort Schemas (legacy)/CD3_INTERVAL_Schema/CD3_INTERVAL_Source_Schema_Plan.md` and `output/explore_INTERVAL_report.txt` — the earlier, differently-conventioned schema-generation work for this cohort, read to cross-check sheet/variable counts and confirm the `donorID` participant-identifier field — not used as a source of cohort facts, consistent with this document's pre-schemify framing. Read 2026-09-28.
- INTERVAL study, homepage — `https://www.intervalstudy.org.uk/` — governing institutions, recruitment dates, the 50,000-participant target reached on schedule, trial rationale. Consulted 2026-09-28.
- INTERVAL, "What is involved?" — `https://www.intervalstudy.org.uk/about-the-study/what-is-involved/` — the randomisation design, donation-interval arms, research blood samples, six-monthly questionnaires, consent scope, re-contact limits. Consulted 2026-09-28.
- INTERVAL, "Who's involved?" — `https://www.intervalstudy.org.uk/about-the-study/whos-involved/` — governance committee structure. Consulted 2026-09-28.
- INTERVAL, "Where?" — `https://www.intervalstudy.org.uk/about-the-study/where/` — the 25 permanent NHSBT donation clinics across England. Consulted 2026-09-28.
- INTERVAL, "INTERVAL Phase II" — `https://www.intervalstudy.org.uk/interval-phase-ii/` — the extension of the original trial to June 2016, the Brentwood centre exclusion. Consulted 2026-09-28.
- INTERVAL, "INTERVAL Phase III" — `https://www.intervalstudy.org.uk/interval-phase-ii/interval-phase-iii/` — the ~4,000-participant iron/haemoglobin-recovery sub-study and its eligibility rules. Consulted 2026-09-28.
- INTERVAL, "Electronic Health Record Linkage" — `https://www.intervalstudy.org.uk/electronic-health-record-linkage/` — the linked-record sources, the link-table/de-personalisation process, the Blood Donors Studies BioResource and its Data Access Committee, the Cambridge Data Controller role. Consulted 2026-09-28.
- INTERVAL, "UK LLC" — `https://www.intervalstudy.org.uk/about-the-study/uk-llc/` — the UK Longitudinal Linkage Collaboration's own governance, its TRE, and how INTERVAL shares data into it while remaining Data Controller. Consulted 2026-09-28.
- CD3 team's own cross-cohort tracking: `General information/cohort data table.xlsx` (sheets "Cohort info on proposal", "Summary Table -large", "Summary Table - small", "Ethnicity", "working table"). Read 2026-09-28.

## 10. Open questions for the steward

- **Where should this cohort's files actually live?** Two copies of the same two dictionaries exist in the repository, neither at the canonical `Harmonization/CD3_Schemify_Pilot/INTERVAL/` location every other pilot cohort uses, and an entirely separate, differently-conventioned schema effort already exists in the "legacy" folder.
- **What is the tracker's missing 10% in the ethnicity breakdown?** CD3's own tracker states 81% White and 9% Other for this cohort, which sums to 90%, not 100% — worth confirming the correct figures directly rather than assuming a rounding artefact.
- **Should Phase 1 and Phase 2/3/4 be modelled as one longitudinal set of tables, or kept structurally separate** (§4, §7)? Both are defensible; the source templates themselves keep them apart.
- **What is the current, exact size of the Phase III sub-cohort**, and is it still recruiting or now closed? "Approximately 4,000" is the only figure found anywhere consulted.
- **What exactly triggered the large jumps in questionnaire size at 24 months (209 variables) and 48 months (177 variables)** compared to their neighbouring waves? Neither dictionary nor the study site explains this directly.
- **Is CD3's own tracker's repeated "Geospatial linkages" and "NHS Breast and bowel cancer screening programme"-style boilerplate genuinely specific to INTERVAL**, or, as suspected for UKB, OFH, LOLIPOP, EPIC-Oxford, and Genes & Health alike, carried over from other cohorts' rows without cohort-specific verification?
