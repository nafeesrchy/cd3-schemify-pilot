# COMPARE — conversion progress

package: CD3_Schemify_Pilot/COMPARE/json_schema · started: 2026-10-06
grain: One element is one donor in each table — one table per requested dictionary sheet
dictionary: `dataRequestForm_COMPARE_EXT_Template_v3.xlsx` (only variables with an X in the Requested column) — full inventory in SOURCES.md

## Tables

| Table | Grain | Vars |
|---|---|---|
| `basic_info` | One donor in the recruitment record | 5 |
| `questionnaires` | One donor in the questionnaires | 150 |
| `hb_measurements` | One donor in the haemoglobin measurements taken at donation | 6 |
| `bloods` | One donor in the research blood sample results | 180 |
| `biomarkers` | One donor in the Nightingale biomarker results | 10 |
| `omics` | One donor in the omics and linkage items | 3 |

354 variables in scope (D001). Not converted: 74 unrequested rows (`dropped` in VARIABLES.csv) and the older v1 form. `donationHistory`, `adverseEventHistory` and `EHRData` have no requested variable, so no tables come from them.

## How to continue

This conversion runs over several sittings — an agent session can hold only so
much at once, so the work is planned in units that each fit one session. Nothing
is lost between sittings: this file is the memory.

To continue at any time: open a fresh agent session in `Harmonization/CD3_Schemify_Pilot/COMPARE/json_schema`
and invoke the skill again. The agent reads this file and proposes the next
unit. You can also ask for anything directly — a specific category, a change,
a question, the final review.

## Conventions

- sentinels: `999` don't know / prefer not to answer · `998` not applicable (both adopted verbatim from the dictionary); a missing value with no code is the provider's blank, written as JSON `null` titled "No value recorded" — no code of our own · D004
- `777` is a top-coded value ("greater than N"), not a sentinel · D004
- $id base: https://schemas.example.org/cd3-compare-pilot/ (replace before publishing) · D012
- grain: see header · title separator: — (em dash) · formatting: 2-space, one key per line · names, titles and labels are the dictionary's own wording
- real data: none in repo; none to be read · D005
- routing: faithful — nothing beyond what the dictionary's own wording states · D008
- validation: draft 2020-12, package's own `tools/validate.py`; validate JSON exports with `null` blanks · D007
- identifier: `identifier` is in `basicInfo` only; format and join-key use are open questions for the data provider · D009

## Categories

| # | table | category | file | vars | source slice | status | touched |
|---|---|---|---|---|---|---|---|
| 1 | basic_info | Identification | basic_info/categories/identification.json | 1 | basicInfo identifier | confirmed | 2026-10-06 |
| 2 | basic_info | Demographics | basic_info/categories/demographics.json | 3 | basicInfo (sexPulse, agePulse, ethnicPulse) | confirmed | 2026-10-06 |
| 3 | basic_info | Blood Group | basic_info/categories/blood_group.json | 1 | basicInfo ABORH | confirmed | 2026-10-06 |
| 4 | questionnaires | Questionnaire Completion | questionnaires/categories/questionnaire_completion.json | 4 | questionnaires start/end dates (incl. _p2) | confirmed | 2026-10-06 |
| 5 | questionnaires | Anthropometric | questionnaires/categories/anthropometric.json | 2 | questionnaires ht, wt | confirmed | 2026-10-06 |
| 6 | questionnaires | Demographics | questionnaires/categories/demographics.json | 1 | questionnaires ethnic | confirmed | 2026-10-06 |
| 7 | questionnaires | Occupation & Physical Activity | questionnaires/categories/occupation_physical_activity.json | 4 | questionnaires occupation, pa_* items | confirmed | 2026-10-06 |
| 8 | questionnaires | Fitzpatrick Skin Type | questionnaires/categories/fitzpatrick_skin_type.json | 9 | questionnaires fitz* items | confirmed | 2026-10-06 |
| 9 | questionnaires | Medical History | questionnaires/categories/medical_history.json | 54 | questionnaires symptoms, iron, pica, restless-legs, medication items | confirmed | 2026-10-06 |
| 10 | questionnaires | Blood Donation | questionnaires/categories/blood_donation.json | 2 | questionnaires haemLow, feel_after | confirmed | 2026-10-06 |
| 11 | questionnaires | General Health | questionnaires/categories/general_health.json | 36 | questionnaires self-rated health, limitation, mood items | confirmed | 2026-10-06 |
| 12 | questionnaires | Reproductive/Hormonal | questionnaires/categories/reproductive_hormonal.json | 3 | questionnaires hrt, pill, menopause | confirmed | 2026-10-06 |
| 13 | questionnaires | Behavioral | questionnaires/categories/behavioral.json | 12 | questionnaires smoking and alcohol items | confirmed | 2026-10-06 |
| 14 | questionnaires | Dietary | questionnaires/categories/dietary.json | 23 | questionnaires diet and eating-change items | confirmed | 2026-10-06 |
| 15 | hb_measurements | Haemoglobin Measurements | hb_measurements/categories/haemoglobin_measurements.json | 6 | Hb_measurements sheet | confirmed | 2026-10-06 |
| 16 | bloods | Blood Counts & Assays, Visit 1 | bloods/categories/blood_counts_assays_visit_1.json | 90 | bloods sheet, _v1 rows | confirmed | 2026-10-06 |
| 17 | bloods | Blood Counts & Assays, Visit 2 | bloods/categories/blood_counts_assays_visit_2.json | 90 | bloods sheet, _v2 rows | confirmed | 2026-10-06 |
| 18 | biomarkers | Blood Biomarkers | biomarkers/categories/blood_biomarkers.json | 10 | biomarkers sheet | confirmed | 2026-10-06 |
| 19 | omics | Omics | omics/categories/omics.json | 3 | omics sheet | confirmed | 2026-10-06 |

Category names reuse the topic vocabulary of the other CD3 packages. Steward-approved whole 2026-10-06 (D012).

## Package milestones

- [x] intake: sources registered · grain confirmed · categories confirmed (2026-10-06)
- [x] common/defs.json + mother scaffold validate green
- [x] every category confirmed (18 of 18, 2026-10-06)
- [x] skip audit (ROUTING.md) — policy `faithful`; 6 register rows: 0 encoded, 5 not-enforceable (R001, R003-R006), 1 declined (R002, dropped at the review, D046); audited 2026-10-06
- [x] coverage audit 1:1 (2026-10-06): 428 inventory rows = 354 converted + 74 dropped; 354 schema properties, 0 orphans either way
- [x] pages current for the whole package (render.py check clean, 2026-10-06: dictionary.html + 6 playgrounds)
- [x] review walked · cleanup decided (2026-10-06): all 16 agent-decided calls accepted (R002 dropped, D046), 6 open items migrated to README §10 by the steward's choice, working files kept (D048)

## Session log

- 2026-10-06 · intake · sources surveyed (v3, 428 inventory rows, 354 requested), method introduced, interview answered (D001–D011), 18 categories across 6 tables approved, package scaffolded · next: convert Identification (basic_info)
- 2026-10-06 · intake · routing register rows given their tables (R001-R003 questionnaires, R004 hb_measurements; R003 also cross-table); validate summary green
- 2026-10-06 · convert basic_info · 3 categories drafted (Identification 1, Demographics 3, Blood Group 1 = 5 vars), fixtures 12 valid / 9 invalid caught, pages rendered; D013; fixed lib $id base (first run wrote the INTERVAL base, corrected before validation of the package) · next: confirm basic_info categories, then convert questionnaires (Questionnaire Completion, Demographics, Anthropometric first)
- 2026-10-06 · convert questionnaires/Questionnaire Completion · basic_info categories confirmed (D014); 4 date columns drafted (text; _p2 universe noted, R003 stays not-enforceable), fixtures 12 valid / 3 invalid caught, pages rendered; D015 · next: confirm Questionnaire Completion, then convert questionnaires Demographics (ethnic) and Anthropometric (ht, wt)
- 2026-10-06 · convert questionnaires/Demographics + Anthropometric · Questionnaire Completion confirmed (D016); Demographics 1 var (ethnic, 16 codes + 999), Anthropometric 2 vars (ht, wt with stated ranges, 777 > 190kg), fixtures 12 valid / 11 invalid caught, pages rendered; D017 · next: confirm Demographics and Anthropometric, then convert questionnaires Fitzpatrick Skin Type (9) and Reproductive/Hormonal (3)
- 2026-10-06 · convert questionnaires/Fitzpatrick Skin Type + Reproductive-Hormonal · Demographics and Anthropometric confirmed (D018); 9 + 3 vars drafted, fixtures 12 valid / 17 invalid caught, pages rendered; D019-D020 · next: confirm those two, then convert questionnaires Behavioral (12), Occupation & Physical Activity (4), Blood Donation (2)
- 2026-10-06 · convert questionnaires/Behavioral + Occupation & Physical Activity + Blood Donation · Fitzpatrick and Reproductive/Hormonal confirmed (D022); 12 + 4 + 2 vars drafted, fixtures 12 valid / 31 invalid caught (questionnaires), pages rendered; D021, D023 · next: confirm those three, then convert questionnaires Dietary (23; R001 ageVeg waits here) and General Health (36)
- 2026-10-06 · convert questionnaires/Dietary · Behavioral, Occupation & Physical Activity, Blood Donation confirmed (D025); 23 vars drafted, R001 ageVeg not-enforceable (D024), fixtures 12 valid / 35 invalid caught (questionnaires), pages rendered · next: confirm Dietary, then convert questionnaires General Health (36)
- 2026-10-06 · convert questionnaires/General Health · Dietary confirmed (D026); 36 vars drafted (limited_activity, time_scale, true_false_scale shared codings), fixtures 12 valid / 39 invalid caught (questionnaires), pages rendered; D027 · next: confirm General Health, then convert questionnaires Medical History (54; R002 rls_9a→rls_9b waits here)
- 2026-10-06 · convert questionnaires/Medical History · General Health confirmed (D028); 54 vars drafted (3 checkbox groups, rls block, 998 families), R002 encoded as a pair (D029) with 2 fixture cases, fixtures 12 valid / 45 invalid caught (questionnaires), pages rendered; D030-D031; a def-rename collision (ironFreq items got the yes/no def) was caught on inspection and rebuilt from the source codings · next: confirm Medical History (incl. R002), then convert the hb_measurements table
- 2026-10-06 · routing register · R003 trigger blanked (cross-table), R005 (rls 998 items) and R006 (Breathless_scale) registered not-enforceable; routing check clean
- 2026-10-06 · steward ruling D033 (keep only what the dictionary explicitly mentions): R002 encoded pair removed, x-universe and x-role annotations removed, R002/R003 declined, R004 deleted; validate summary green (questionnaires fixtures 43/43), pages re-rendered · next: confirm Medical History (questionnaires, now without R002), then convert hb_measurements
- 2026-10-06 · undo of D033 at the steward's request: R002 pair, x-universe notes, x-role and register rows R003/R004 restored as before; D033 superseded-by D034; validate summary green; Medical History (questionnaires, incl. R002) still awaits confirmation · next: confirm Medical History, then convert hb_measurements
- 2026-10-06 · convert hb_measurements · questionnaires Medical History confirmed (D036) - the questionnaires table is fully confirmed (11 categories); Haemoglobin Measurements 6 vars drafted (3 dates text, 3 values number with source units), fixtures 12 valid / 6 invalid caught, pages rendered; D035 · next: confirm Haemoglobin Measurements, then convert bloods (Visit 1 90, Visit 2 90)
- 2026-10-06 · convert bloods · Haemoglobin Measurements confirmed (D038); Visit 1 (90) and Visit 2 (90) drafted, fixtures 12 valid / invalid caught, pages rendered; D037 · next: confirm the two bloods categories, then convert biomarkers (10) and omics (3)
- 2026-10-06 · convert biomarkers + omics · both bloods categories confirmed (D041); Blood Biomarkers 10 vars (number, units) and Omics 3 vars (text; D040 open) drafted, fixtures 12 valid each, pages rendered; all 6 tables now fully drafted (354 of 354 converted) · next: confirm Blood Biomarkers and Omics, then skip audit, coverage audit, pages check, review
- 2026-10-06 · skips audit · Blood Biomarkers and Omics confirmed (D042), all 18 categories confirmed; routing check green with no findings; register 1 encoded (R002, both halves fixtured) + 5 not-enforceable; every 998-bearing property is in a register row (D043) · next: coverage audit, pages check, then review (README, ledger walk, cleanup offer)
- 2026-10-06 · coverage audit · inventory 428 = 354 converted + 74 dropped; 354 schema properties, no orphans; plan counts match files; 336 X rows expand to 354 columns (D044) · next: pages check, then review (README, ledger walk, cleanup offer)
- 2026-10-06 · pages check · render.py check clean (dictionary.html and the 6 playground pages current with schemas and fixtures; no stale pages, no absolute-path or skill-directory references); validate summary green · next: review (README, ledger walk by confidence, cleanup offer)
- 2026-10-06 · review started · ledger = 44 lines (21 user-confirmed, 16 agent-decided active, 6 open, 1 superseded); group 1 (the 6 open questions, all for the data provider, plus the provider questions inside D013, D015, D020, D024, D035) presented · next: review — steward answers or migrates the open items; then walk the 16 agent-decided calls by theme; then README and cleanup offer
- 2026-10-06 · review · open items stay open (D045); presenting the 16 agent-decided calls in themed batches · next: steward answers batch 1 (codes/ranges, types/units), then batch 2 (wording, routing/structure)
- 2026-10-06 · review · themes A (codes/ranges) and B (types/units) accepted: 5 lines flipped to user-confirmed (review); 11 mixed lines (wording/routing/structure) held for the next batch · next: present batch 2 (wording, routing/structure), then user-confirmed recap, README, cleanup offer
- 2026-10-06 · review · R002 conditional dropped at the steward's request (D046): conditionals, 2 toy cases removed, register row declined, D029 superseded; summary green; batch 2 (wording, routing/structure) still awaiting the steward's answer · next: steward answers batch 2 themes C and D (routing item 12 now reads: no rule enforced), then recap, README, cleanup offer
- 2026-10-06 · review · themes C and D accepted: all 16 agent-decided calls now user-confirmed (review); D047 records the skip audit re-run after R002 was dropped; README.md written (10 sections) · next: the cleanup offer (fold working files into the README and delete, or keep), then final summary and handoff
- 2026-10-06 · review complete · working files kept (D048); real-data offer made (none in repo, none read); 6 open items remain in README §10 for the data provider; summary green, pages current · next: — (complete)
