# INTERVAL — conversion progress

package: CD3_Schemify_Pilot/INTERVAL/json_schema · started: 2026-10-05
grain: One element is one donor at one contact point (baseline, 6, 12, 18 or 24 months, or the linked-record data) — one table per contact point
dictionary: `dataRequestForm_PHASE1_EXT_Template_v4.xlsx` (Phase 1 only; only variables with an X in the Requested column) — full inventory in SOURCES.md

## Tables

| Table | Grain | Vars |
|---|---|---|
| `baseline` | One donor at baseline (recruitment) | 232 |
| `month_6` | One donor at the 6-month questionnaire | 56 |
| `month_12` | One donor at the 12-month questionnaire | 57 |
| `month_18` | One donor at the 18-month questionnaire | 81 |
| `month_24` | One donor at the 24-month contact (end of Phase I) | 425 |
| `ehr_linkage` | One donor in the linked-record (Caliber) endpoints | 4 |

856 variables in scope (D001): 855 converted, 1 deferred (the `enmo_0plus – enmo_4000plus` row standing for 60 columns, D013/D078). Not converted: 129 unrequested Phase 1 rows (`dropped` in VARIABLES.csv), the Phase 2/3/4 workbook and v3. `donationHistory`, `outcomes`, `adverseEventHistory`, `adverseEvents` have no requested variable, so no tables come from them.

## How to continue

This conversion runs over several sittings — an agent session can hold only so
much at once, so the work is planned in units that each fit one session. Nothing
is lost between sittings: this file is the memory.

To continue at any time: open a fresh agent session in `Harmonization/CD3_Schemify_Pilot/INTERVAL/json_schema`
and invoke the skill again. The agent reads this file and proposes the next
unit. You can also ask for anything directly — a specific category, a change,
a question, the final review.

## Conventions

- sentinels: `999` don't know / prefer not to answer · `998` not applicable (both adopted verbatim from the dictionary); a missing value with no code is the provider's blank, written as JSON `null` titled "No value recorded" (as in the other CD3 packages) — no code of our own, the dictionary mimics the provider's · D005, D021
- `777` is a top-coded value ("greater than N"), not a sentinel · D005
- $id base: https://schemas.example.org/cd3-interval-pilot/ (replace before publishing) · agent-decided with D018
- grain: see header · title separator: — (em dash) · formatting: 2-space, one key per line · names, titles and labels are the dictionary's own wording
- real data: none in repo; none to be read · D006
- routing: faithful — nothing beyond what the dictionary's own wording states (R001–R003) · D008
- validation: draft 2020-12, package's own `tools/validate.py` · D009
- no participant identifier in the dictionary — to consult the data provider; row uniqueness not enforceable meanwhile · D010, D011

## Categories

| # | table | category | file | vars | source slice | status | touched |
|---|---|---|---|---|---|---|---|
| 1 | baseline | Demographics | baseline/categories/demographics.json | 5 | basicInfo (sexPulse, yearPulse, agePulse, ethnicPulse) + questionnaire_bl ethnic_bl | confirmed | 2026-10-06 |
| 2 | baseline | Recruitment | baseline/categories/recruitment.json | 4 | basicInfo (attendanceDate, centre, outCome) + startDate_bl | confirmed | 2026-10-06 |
| 3 | baseline | Blood Biomarkers | baseline/categories/blood_biomarkers.json | 24 | biomarkers sheet (+ basicInfo ABORH at baseline) | confirmed | 2026-10-06 |
| 4 | baseline | Anthropometric | baseline/categories/anthropometric.json | 2 | questionnaire_bl ht_bl, wt_bl | confirmed | 2026-10-06 |
| 5 | baseline | General Health & SF-36 | baseline/categories/general_health_sf36.json | 54 | questionnaire (self-rated health, limitation, SF36 items and scores) | confirmed | 2026-10-06 |
| 6 | baseline | Medical History | baseline/categories/medical_history.json | 9 | questionnaire (symptoms, conditions, iron/medication/supplement items) | confirmed | 2026-10-06 |
| 7 | baseline | Reproductive/Hormonal | baseline/categories/reproductive_hormonal.json | 3 | questionnaire_bl hrt, pill, menopause | confirmed | 2026-10-06 |
| 8 | baseline | Dietary | baseline/categories/dietary.json | 12 | questionnaire (diet and eating-change items) | confirmed | 2026-10-06 |
| 9 | baseline | Behavioral | baseline/categories/behavioral.json | 12 | questionnaire_bl alcohol and smoking items | confirmed | 2026-10-06 |
| 10 | baseline | Occupation & Physical Activity | baseline/categories/occupation_physical_activity.json | 3 | questionnaire (work, leisure, activity, screen time) | confirmed | 2026-10-06 |
| 11 | baseline | Blood Counts & Assays | baseline/categories/blood_counts_assays.json | 90 | bloods sheet | confirmed | 2026-10-06 |
| 12 | baseline | Omics | baseline/categories/omics.json | 14 | omics sheet | confirmed | 2026-10-06 |
| 13 | month_6 | General Health & SF-12 | month_6/categories/general_health_sf12.json | 30 | questionnaire (self-rated health, limitation, SF12 items and scores) | confirmed | 2026-10-06 |
| 14 | month_6 | Medical History | month_6/categories/medical_history.json | 26 | questionnaire (symptoms, conditions, iron/medication/supplement items) | confirmed | 2026-10-06 |
| 15 | month_12 | General Health & SF-12 | month_12/categories/general_health_sf12.json | 30 | questionnaire (self-rated health, limitation, SF12 items and scores) | confirmed | 2026-10-06 |
| 16 | month_12 | Medical History | month_12/categories/medical_history.json | 27 | questionnaire (symptoms, conditions, iron/medication/supplement items) | confirmed | 2026-10-06 |
| 17 | month_18 | General Health & SF-12 | month_18/categories/general_health_sf12.json | 30 | questionnaire (self-rated health, limitation, SF12 items and scores) | confirmed | 2026-10-06 |
| 18 | month_18 | Medical History | month_18/categories/medical_history.json | 51 | questionnaire (symptoms, conditions, iron/medication/supplement items) | confirmed | 2026-10-06 |
| 19 | month_24 | General Health & SF-36 | month_24/categories/general_health_sf36.json | 54 | questionnaire (self-rated health, limitation, SF36 items and scores) | confirmed | 2026-10-06 |
| 20 | month_24 | Blood Donation | month_24/categories/blood_donation.json | 1 | questionnaire_24m haemLow_24m | confirmed | 2026-10-06 |
| 21 | month_24 | Medical History | month_24/categories/medical_history.json | 67 | questionnaire (symptoms, conditions, iron/medication/supplement items) | confirmed | 2026-10-06 |
| 22 | month_24 | Dietary | month_24/categories/dietary.json | 19 | questionnaire (diet and eating-change items) | confirmed | 2026-10-06 |
| 23 | month_24 | Occupation & Physical Activity | month_24/categories/occupation_physical_activity.json | 130 | questionnaire (work, leisure, activity, screen time) | confirmed | 2026-10-06 |
| 24 | month_24 | Cognitive | month_24/categories/cognitive.json | 9 | cognitiveTest sheet | confirmed | 2026-10-06 |
| 25 | month_24 | Physical Activity (accelerometer) | month_24/categories/physical_activity_accelerometer.json | 18 | physicalActivity sheet | confirmed | 2026-10-06 |
| 26 | month_24 | Blood Biomarkers | month_24/categories/blood_biomarkers.json | 20 | biomarkers sheet (+ basicInfo ABORH at baseline) | confirmed | 2026-10-06 |
| 27 | month_24 | Blood Counts & Assays | month_24/categories/blood_counts_assays.json | 91 | bloods sheet | confirmed | 2026-10-06 |
| 28 | month_24 | Omics | month_24/categories/omics.json | 16 | omics sheet | confirmed | 2026-10-06 |
| 29 | ehr_linkage | Linked Records | ehr_linkage/categories/linked_records.json | 4 | EHRData sheet | confirmed | 2026-10-06 |

Category names reuse the MWS topic vocabulary and recur across tables (`Medical History`, `General Health`, `Dietary`, `Blood …`, `Omics`). SF-12 vs SF-36 follows the dictionary's own labelling. Steward-approved whole 2026-10-05 (D017, D018).

## Package milestones

- [x] intake: sources registered · grain confirmed · categories confirmed (2026-10-05)
- [x] common/defs.json + mother scaffold validate green
- [x] every category confirmed (29 of 29, 2026-10-06)
- [x] skip audit (ROUTING.md) — policy `faithful`; 8 register rows: 0 encoded, 7 not-enforceable (R001–R003, R005–R008), 1 declined (R004, dropped at the review, D096); audited 2026-10-06
- [x] coverage audit 1:1 (2026-10-06): 985 inventory rows = 855 converted + 1 deferred + 129 dropped; 855 schema properties, 0 orphans either way
- [x] pages current for the whole package (render.py check clean, 2026-10-06: dictionary.html + 6 playgrounds)
- [x] review walked · cleanup decided (2026-10-06): all 35 agent-decided calls accepted, 13 open items migrated to README §10 by the steward's choice, working files kept (D095)

## Session log

- 2026-10-05 · intake · sources surveyed (Phase 1 v4, 985 columns, 856 requested), method introduced, interview answered, 17 categories across 6 tables approved, package scaffolded · next: convert Demographics (baseline)
- 2026-10-05 · convert baseline/Demographics · 5 vars (sexPulse, yearPulse, agePulse, ethnicPulse, ethnic_bl) drafted, fixtures 6 valid / 8 invalid caught, dictionary + playground rendered; D019–D020 · next: confirm Demographics, then convert Recruitment (baseline)
- 2026-10-06 · revise blank handling · blank switched from "" to JSON null ("No value recorded") per steward, D021 supersedes D016; defs, Demographics, fixtures, pages refreshed · next: confirm Demographics, then convert Recruitment (baseline)
- 2026-10-06 · convert baseline/Recruitment · Demographics confirmed (D024); Recruitment 4 vars (startDate_bl, attendanceDate, centre, outCome) drafted, fixtures 12 valid / 11 invalid caught, pages rendered; D022–D023 · next: confirm Recruitment, then convert Anthropometric (baseline)
- 2026-10-06 · convert baseline/Anthropometric · Recruitment confirmed (D025); Anthropometric 2 vars (ht_bl, wt_bl) drafted, fixtures 12 valid / 13 invalid caught, pages rendered; D026–D027 · next: confirm Anthropometric, then convert Medical History (baseline)
- 2026-10-06 · convert baseline/Medical History · Anthropometric confirmed (D028); Medical History 9 vars drafted (all yes/no/999), fixtures 12 valid / 15 invalid caught, pages rendered; stale 'Medical History & Symptoms' names fixed in ROUTING.csv · next: confirm Medical History (baseline), then convert Reproductive/Hormonal (baseline)
- 2026-10-06 · convert baseline/Reproductive-Hormonal · Medical History confirmed (D029); Reproductive/Hormonal 3 vars drafted ('no' is 0 on hrt/pill), fixtures 12 valid / 17 invalid caught, pages rendered; D030 · next: confirm Reproductive/Hormonal, then convert Dietary (baseline; R001 ageVeg_bl waits here)
- 2026-10-06 · convert baseline/General Health & SF-36 · Reproductive/Hormonal confirmed (D031); 54 vars drafted (4 shared codings, 18 SF36 scores 0–100), fixtures 12 valid / 20 invalid caught, pages rendered; D032–D033 · next: confirm General Health & SF-36, then convert Dietary (baseline; R001 ageVeg_bl waits here)
- 2026-10-06 · convert baseline/Dietary · General Health & SF-36 confirmed (D034); Dietary 11 vars drafted, fixtures 12 valid / 23 invalid caught, pages rendered; R001 ageVeg_bl set not-enforceable (no value stated for non-vegetarians, D036); D035 · next: confirm Dietary, then convert Behavioral (baseline)
- 2026-10-06 · convert baseline/Behavioral · Dietary confirmed (D037) then reopened to add smooth_bl (misfiled under Behavioral by my rule, D038): Dietary 12, Behavioral 12 vars drafted, fixtures 12 valid / 26 invalid caught, pages rendered; D039 · next: confirm Behavioral + Dietary's added smooth_bl, then convert Occupation & Physical Activity (baseline)
- 2026-10-06 · convert baseline/Occupation & Physical Activity · Behavioral + smooth_bl confirmed (D040); 3 vars drafted (work_bl, leisure_bl, occupation_bl), fixtures 12 valid / 28 invalid caught, pages rendered · next: confirm Occupation & Physical Activity, then convert Blood Biomarkers (baseline)
- 2026-10-06 · convert baseline/Blood Biomarkers · Occupation & Physical Activity confirmed (D043); 24 vars drafted (ABORH, 16 measured biomarkers, 7 lab-processing dates), fixtures 12 valid / 31 invalid caught, pages rendered; D041-D042 · next: confirm Blood Biomarkers, then convert Blood Counts & Assays (baseline, 90 vars)
- 2026-10-06 · convert baseline/Blood Counts & Assays · Blood Biomarkers confirmed (D045); 90 vars drafted (89 analyser results + processDate_bl), fixtures 12 valid / 33 invalid caught, pages rendered; D044 · next: confirm Blood Counts & Assays, then convert Omics (baseline, 14 vars) — baseline's last category
- 2026-10-06 · convert baseline/Omics · Blood Counts & Assays confirmed (D047); Omics 14 vars drafted (typed text, nothing stated; D046 open), fixtures 12 valid / 34 invalid caught, pages rendered; baseline table now fully drafted · next: confirm Omics, then convert month_6 General Health & SF-12
- 2026-10-06 · convert month_6/General Health & SF-12 · Omics confirmed (D048); tired_6m/12m/18m moved to Medical History (D049); 30 vars drafted, fixtures 12 valid / 6 invalid caught, pages rendered; D050; generic converter used · next: confirm month_6 General Health & SF-12, then convert month_6 Medical History (26 vars)
- 2026-10-06 · convert month_6/Medical History · General Health & SF-12 confirmed (D051); 26 vars drafted (all yes/no), fixtures 12 valid / 10 invalid caught (month_6 table fully drafted), pages rendered; D052 · next: confirm month_6 Medical History, then convert month_12 General Health & SF-12 (30)
- 2026-10-06 · convert month_12/General Health & SF-12 · month_6 Medical History confirmed (D053); 30 vars drafted, fixtures 12 valid / 6 invalid caught, pages rendered; D054 · next: confirm month_12 General Health & SF-12, then convert month_12 Medical History (27)
- 2026-10-06 · convert month_12/Medical History · General Health & SF-12 confirmed (D055); 27 vars drafted (all yes/no), fixtures 12 valid / 10 invalid caught (month_12 table fully drafted), pages rendered; D056 · next: confirm month_12 Medical History, then convert month_18 General Health & SF-12 (30)
- 2026-10-06 · convert month_18/General Health & SF-12 · month_12 Medical History confirmed (D057); 30 vars drafted, fixtures 12 valid / 6 invalid caught, pages rendered; D058 · next: confirm month_18 General Health & SF-12, then convert month_18 Medical History (51; R002 rls_9a→rls_9b waits here)
- 2026-10-06 · convert month_18/Medical History · General Health & SF-12 confirmed (D063); 51 vars drafted (restless-legs block with 12 checkbox columns, rls_13 range), fixtures 12 valid / 10 invalid caught (month_18 fully drafted), pages rendered; R002 not-enforceable (D059); D060–D062 · next: confirm month_18 Medical History, then convert month_24 General Health & SF-36
- 2026-10-06 · convert month_24/General Health & SF-36 · month_18 Medical History confirmed (D064); 54 vars drafted, fixtures 12 valid / 6 invalid caught, pages rendered; D065 · next: confirm month_24 General Health & SF-36, then convert month_24 Medical History (67; R003 and 998 families in this table)
- 2026-10-06 · convert month_24/Medical History · General Health & SF-36 confirmed (D068); 67 vars drafted (998 families as values only; checkbox groups rls_6/7 a-g; rls_13), R004 encoded as a pair (D066) with 2 fixture cases, R003 not-enforceable (D067), fixtures 12 valid / 12 invalid caught, pages rendered; D069 · next: confirm month_24 Medical History (incl. R004), then convert month_24 Dietary (19)
- 2026-10-06 · convert month_24/Dietary · Medical History (incl. R004) confirmed (D070, D066 ratified); 19 vars drafted (7 Pica checkbox columns, 12 diet-change items), fixtures 12 valid / 13 invalid caught, pages rendered; D071 · next: confirm month_24 Dietary, then convert month_24 Occupation & Physical Activity (130 — probably two sittings: leisure items vs the rest)
- 2026-10-06 · convert month_24/Occupation & Physical Activity · Dietary confirmed (D073); 130 vars drafted (25 items + 35 leisure activities x Freq/Hrs/Min), fixtures 12 valid / 20 invalid caught, pages rendered; D072; first run dropped leis code 1 'None' (parser), caught on inspection, re-run clean · next: confirm month_24 Occupation & Physical Activity, then convert month_24 Blood Donation (1), Cognitive (9), Physical Activity (accelerometer) (19)
- 2026-10-06 · convert month_24/Blood Donation · Occupation & Physical Activity confirmed (D074); 1 var drafted (haemLow_24m), fixtures re-run, pages rendered; D075 · next: confirm Blood Donation, then convert month_24 Cognitive (9)
- 2026-10-06 · convert month_24/Cognitive · Blood Donation confirmed (D077); 9 vars drafted (test scores, number, ms where stated), fixtures 12 valid / 26 invalid caught, pages rendered; D076 · next: confirm Cognitive, then convert month_24 Physical Activity (accelerometer) (19; enmo_* thresholds D013 open)
- 2026-10-06 · convert month_24/Physical Activity (accelerometer) · Cognitive confirmed (D079); 18 vars drafted, enmo_0plus–enmo_4000plus (60 columns, names unlisted) deferred (D078/D013), fixtures 12 valid / 28 invalid caught, pages rendered · next: confirm Physical Activity (accelerometer), then convert month_24 Blood Biomarkers (20)
- 2026-10-06 · convert month_24/Blood Biomarkers · Physical Activity (accelerometer) confirmed (D081); 20 vars drafted (10 biomarkers + 10 lab dates), fixtures 12 valid / 30 invalid caught (one seeded wrong-type had put a string in a text column - fixed, generator patched), pages rendered; D080 · next: confirm Blood Biomarkers, then convert month_24 Blood Counts & Assays (91)
- 2026-10-06 · convert month_24/Blood Counts & Assays · Blood Biomarkers confirmed (D083); 91 vars drafted (89 results + 2 dates), fixtures 12 valid / 32 invalid caught, pages rendered; D082 · next: confirm Blood Counts & Assays, then convert month_24 Omics (16) — last month_24 category
- 2026-10-06 · convert month_24/Omics · Blood Counts & Assays confirmed (D085); 16 vars drafted (text, nothing stated; D084), fixtures 12 valid / 34 invalid caught, pages rendered; month_24 table fully drafted · next: confirm month_24 Omics, then convert ehr_linkage Linked Records (4)
- 2026-10-06 · convert ehr_linkage/Linked Records · month_24 Omics confirmed (D087); 4 vars drafted (text, nothing stated; D086 open), fixtures 12 valid / 3 invalid caught (toy rows first duplicated - uniqueItems - fixed), pages rendered; all 6 tables now fully drafted (851+4 of 856 converted, 1 deferred = enmo group row) · next: confirm Linked Records, then skips audit and coverage audit, then review
- 2026-10-06 · skips audit · Linked Records confirmed (D088), all 29 categories confirmed; routing check green but flagged 17 unregistered 998-bearing month_24 properties -> registered as R005–R008 not-enforceable (gate unstated, D014/D089); register 1 encoded + 7 not-enforceable; validate summary green · next: coverage audit, pages check, then review (README, ledger walk, cleanup offer)
- 2026-10-06 · coverage audit · inventory 985 = 855 converted + 1 deferred (enmo group row) + 129 dropped; 855 schema properties, no orphans; plan counts match files; month_24 table count corrected 426→425 (D090) · next: pages check, then review (README, ledger walk, cleanup offer)
- 2026-10-06 · pages check · render.py check clean (dictionary.html and the 6 playground pages current with schemas and fixtures; no stale pages, no absolute-path or skill-directory references); validate summary green · next: review (README, ledger walk by confidence, cleanup offer)
- 2026-10-06 · review started · ledger = 90 lines (40 user-confirmed, 35 agent-decided active, 13 open, 2 superseded); group 1 (the 13 open questions, all for the data provider) presented · next: review — steward answers or migrates the 13 open items; then walk the 35 agent-decided calls by theme; then README and cleanup offer
- 2026-10-06 · review · open items stay open (D091); agent-decided themes A (codes), B (types/ranges), C (placement) accepted: 19 lines flipped to user-confirmed (review 2026-10-06) · next: review — walk remaining 16 agent-decided calls (wording, routing, structure), then user-confirmed recap, README, cleanup offer
- 2026-10-06 · review · all 35 agent-decided calls accepted at the walk (D093 records the title question); user-confirmed recap given; README.md written (10 sections); found at the README test that CSV blanks fail the package validator (D092 open) · next: steward decides D092 (CSV blanks) and the cleanup offer (fold working files into README and delete, or keep); then final summary and handoff
- 2026-10-06 · review complete · CSV blanks: option 1 (validate JSON exports, D094); working files kept (D095); real-data offer made (none in repo, none read); 13 open items remain in README §10 for the data provider; summary green, pages current · next: — (complete)
- 2026-10-06 · pages · steward asked why month_24 came before month_6 in `dictionary.html` (mother-file names sorted as text); added `manifest.json` (D096) and re-rendered `dictionary.html`; `render.py check` clean
- 2026-10-06 · revision · R004 (rls_9a_24m to rls_9b_24m) dropped at the steward's request, as in COMPARE (D096): conditionals, 2 toy cases removed, register row declined, D066 superseded, README §5/§6 updated; summary green · next: — (complete)
