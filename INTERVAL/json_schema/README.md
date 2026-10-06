# INTERVAL — Phase 1 data dictionary as JSON Schema

This package is a machine-checkable version of the INTERVAL data request form for Phase 1 (`dataRequestForm_PHASE1_EXT_Template_v4.xlsx`). It describes the variables that carry an `X` in that form's *Requested* column: **855 variables converted and 1 deferred, in six tables**. The Phase 2/3/4 form, the older v3 Phase 1 form and the 129 unrequested Phase 1 rows are out of scope (see §8). Everything here is transcribed from the dictionary; nothing was added from outside it (see §3 and §7).

A consumer with this folder and Python can validate data (`tools/validate.py`), browse the dictionary (`dictionary.html`) and read the rules (this file). Nothing here needs the tool that built it.

## 1. What this package describes

INTERVAL is the blood-donor study at https://www.intervalstudy.org.uk/. The dictionary arrives as a data request form, one sheet per kind of data. Its variable names carry a time-point suffix (`_bl`, `_6m`, `_12m`, `_18m`, `_24m`), so each table below is one donor at one contact point, with column names exactly as the dictionary spells them.

| Table | Mother file | One row is | Categories (variables) |
|---|---|---|---|
| `baseline` | `baseline/baseline.schema.json` | one donor at baseline (recruitment) — 232 | Demographics (5), Recruitment (4), Anthropometric (2), General Health & SF-36 (54), Medical History (9), Reproductive/Hormonal (3), Dietary (12), Behavioral (12), Occupation & Physical Activity (3), Blood Biomarkers (24), Blood Counts & Assays (90), Omics (14) |
| `month_6` | `month_6/month_6.schema.json` | one donor at the 6-month questionnaire — 56 | General Health & SF-12 (30), Medical History (26) |
| `month_12` | `month_12/month_12.schema.json` | one donor at the 12-month questionnaire — 57 | General Health & SF-12 (30), Medical History (27) |
| `month_18` | `month_18/month_18.schema.json` | one donor at the 18-month questionnaire — 81 | General Health & SF-12 (30), Medical History (51) |
| `month_24` | `month_24/month_24.schema.json` | one donor at the 24-month contact (end of Phase I) — 425 | General Health & SF-36 (54), Blood Donation (1), Medical History (67), Dietary (19), Occupation & Physical Activity (130), Cognitive (9), Physical Activity (accelerometer) (18), Blood Biomarkers (20), Blood Counts & Assays (91), Omics (16) |
| `ehr_linkage` | `ehr_linkage/ehr_linkage.schema.json` | one donor in the linked-record (Caliber) endpoints — 4 | Linked Records (4) |

The dictionary lists **no participant identifier**, so no table has an identification category and rows cannot be checked for uniqueness (open item 1, §10).

## 2. Layout and composition

```
README.md   VARIABLES.csv   ROUTING.csv   manifest.json   dictionary.html   playground-<table>.html
common/defs.json                         shared definitions (§4)
<table>/<table>.schema.json              the mother file: an array of row objects
<table>/categories/<category>.json       one file per category
examples/<table>/toy_valid.json, toy_invalid.json, toy_invalid_ledger.json
tools/validate.py   tools/requirements.txt   assets/   (the page libraries)
```

A row is the `allOf` union of its category files, followed by any routing conditionals. Every category file lists all of its properties as `required`, so every column must be present in every row. The mother file's single `unevaluatedProperties: false` rejects any column the dictionary does not list.

## 3. Value-encoding conventions

- **Codes are `oneOf` single-value constants, each with the dictionary's own label as its title.** Measures are `anyOf` a number plus the blank. Code labels, variable titles and units are the dictionary's own words, typos included (§7).
- **No bounds are invented.** A range is asserted only where the dictionary states one (`0 - 100` for the SF-12/SF-36 scores, `0 – 23` hours, `0 – 59` minutes, and ranges written beside labelled codes such as `1 - 70 = age`). Where it states none, none is asserted, and measured values are typed `number` because the dictionary states no data types.
- **Units** are carried as `x-unit` exactly as written in the dictionary (`109/L` and `1012/L` are kept as written; they most likely mean 10⁹/L and 10¹²/L with the superscripts lost).
- **Dates** are plain text with no pattern: the dictionary says only "date" (open item 7).
- **Whole numbers** are assumed for ranges such as `1 - 70` and `10 - 75` because the fractional values (such as `0.1`) are listed as their own labelled codes. A real extract with decimals in those columns would be flagged.
- **Shared codings** (for example the SF-36 answer scales) are defined once per category file and referenced by each item, which keeps its own title.
- **Checkbox questions** that the dictionary writes as one row (`rls_6a_24m – rls_6g_24m`, `Pica_1_24m – Pica_7_24m`) are one column per option, each holding only the code the dictionary states (`1`).
- **`$id` base.** All schemas use `https://schemas.example.org/cd3-interval-pilot/`, a placeholder that is never fetched. Replace it before publishing the schemas anywhere public.

## 4. Sentinel semantics

| Value | Meaning | Where it applies |
|---|---|---|
| `null` | "No value recorded": the data provider's blank. The dictionary defines no code for a missing value, and none was added. | every column |
| `999` | don't know / prefer not to answer | the questionnaire items whose dictionary codes list it; a few items give only "don't know" and carry that label on the item |
| `998` | not applicable | 17 item families at 24 months (`ironFreq`, five `*_hosp`, `Breathless_scale`, `rls_3` to `rls_13`); the dictionary does not say who they are not applicable for (§6) |
| `777` | **a value, not a missing code**: "greater than N" (`more than 20 times per week`, `more than 75 years old`, `777 > 190kg`) | the items whose dictionary codes list it, each labelled |

Other labelled codes are exactly the dictionary's own and keep its labels, for instance `0.1 = less than once a week`, and `0 = no` on `hrt_bl` and `pill_bl` (elsewhere "no" is `2`). On the four health-belief items, code `3` ("don't know") is a real answer and `999` is separate.

## 5. Enforced routing rules

The routing policy is **faithful**: only rules the dictionary's own wording states are enforced, and none are added from domain knowledge. **No routing rule is enforced.** One rule, R004 (`rls_9b_24m` asked only if `rls_9a_24m` is yes), was encoded during the conversion and removed at the review because the dictionary does not state it (D096); see §6.

## 6. Documented but not enforced

**Routing the dictionary states or implies but gives no value for** (register: `ROUTING.csv`, all `not-enforceable` or `declined`):

| Rule | What the dictionary says | Why it is not enforced |
|---|---|---|
| R001 | `ageVeg_bl` is for "vegetarians only" | no value is given for meat-eaters |
| R002 | `rls_9b_18m` begins "If so" (after `rls_9a_18m`) | no value for others, and no `998` at 18 months |
| R003 | `supp_otc_2_24m` begins "If you take any" (after `supp_otc_24m`) | no value for others, and no `998` on the item |
| R004 | `rls_9b_24m` begins "If so" (after `rls_9a_24m`) and has `998 = not applicable` | declined (D096): the dictionary states no rule, so none is enforced |
| R005 | `ironFreq_24m` has `998 = not applicable` | who it is not applicable for is not stated |
| R006 | the five `*_hosp_24m` items have `998` | not stated |
| R007 | `Breathless_scale_24m` has `998` | not stated |
| R008 | `rls_3_24m`, `rls_4_24m`, `rls_5_24m`, `rls_6g_24m`, `rls_7g_24m`, `rls_8_24m`, `rls_10_24m` to `rls_13_24m` | not stated |

Other items read as dependent on an earlier answer (the `*_hosp` items after their condition, `heartProblems`, `eatTyp_INTERVAL_24m`, the women-specific `hrt_bl`/`pill_bl`/`menopause_bl`), but the dictionary states no rule, so none is enforced.

**Checks JSON Schema cannot make, which a consumer should apply downstream:**

- Row uniqueness (no identifier, §1).
- `attention_24m` is described as `stroop_MRT - colours_MRT`, and `trailsDiff_24m` as `trailsA_duration - trailsB_duration`; the SF-12/SF-36 scores and their norm-based versions are presumably computed from the item answers. None of these relationships is checked.
- Which of the 60 `enmo_*` columns a real extract contains: they are not declared (§10, item 3), so a real extract carrying them is flagged as having undeclared columns until the names are added.

## 7. Known source issues handled

Titles and labels are the dictionary's own words; where a defect is visible, the schema keeps the source text and a `$comment` on the column notes it.

- **Typos kept in titles/labels:** "limit to" for "limit you" (`mod_`, `stairA_` and the other activity-limitation items at 6–24 months), "Have you more tired" (`tired_6m`, `tired_12m`, `tired_18m`), "less that 10 years old" (`rls_13_18m`), "intenstity" (`mvpa_*`), "impedence" (`PLT_I_*`), "corposcular" (`RBC_He_pg_*`), "non-nutritional, substances" (Pica question).
- **`smStopAge_bl`** ("How old were you when you stopped smoking?") labels its 10 – 70 range "age started", copied from `smStartAge_bl`; kept as written.
- **Stray trailing commas** in some coding cells (`heartProblems_12m`, `eatTyp_change_24m`, `rls_13_18m`) are ignored; no code is missing.
- **Arrows:** the source's "→" in checkbox codings came through as "à" (`rls_6a = 1 à Morning`); the schemas use the option labels only.
- **Request-form wording** is kept where it is part of the dictionary's description: "(Ticked automatically with baseline)" (omics), "(24m Sample … ID's automatically included in dataset, see below)" (baseline omics; no "below" exists in the file), and the instruction after `processDate_bl`.
- **Group rows:** the dictionary lists some questions as one row for several columns (`rls_6a_18m – rls_6f_18m`, `Pica_1_24m – Pica_7_24m`, `leis_cswim … _24m`). They are expanded to one column per delivered column; the `leis_*` names (`leis_<activity>Freq/Hrs/Min_24m`) are the package's reading of the group row (open item 2).
- **Not variables:** footnote rows (`*NHSBT codes for adverse events`), `Non_Randomised` (a request-form option) and `CenDate` (named only in a footnote) are not columns of this package (§8, §10 item 5).
- **v3 vs v4:** the older v3 form differs from v4 only by one dropped variable (`Caliber_GP`), re-worded `hxFaint*` descriptions and the `Requested` ticks; no coding differs.

## 8. Sources and provenance

- **Dictionary used:** `raw_data/dataRequestForm_PHASE1_EXT_Template_v4.xlsx` (Excel; 16 data sheets plus an overview; one row per variable; header `Variable_name | Description | Time_point | Categories | marker | Requested`); registered 2026-10-05. Only rows with `X` in `Requested` are converted; the other 129 rows are listed in `VARIABLES.csv` as `dropped`.
- **Registered but not used:** `dataRequestForm_PHASE1_EXT_Template_v3.xlsx` (older version of the same form) and `dataRequestForm_PHASE234_EXT_Template_v2.xlsx` (Phase 2/3/4; out of scope).
- **External sources consulted:** the study website https://www.intervalstudy.org.uk/ (2026-10-05, for questionnaire or skip-logic documentation: none was found) and a web search for skip logic (2026-10-05: none found). The steward has no other documents.
- **Not used as a source:** an earlier internal brief of the cohort and an earlier set of auto-generated schemas for it; this package transcribes from the dictionary only.
- **Steward's rulings** (scope, grain, tables, missing-value convention, faithful routing, validation target) are recorded in the project's working notes and summarised in §3–§6.

## 9. Validating and browsing

```
pip install -r tools/requirements.txt      # or use: uv run tools/validate.py …
python3 tools/validate.py summary .        # schemas, fixtures, coverage, routing — everything
python3 tools/validate.py data . --file your_export.json --table baseline
```

- **Validate a JSON export, not a CSV with blank cells.** The validator reads an empty CSV cell as an empty string, and the coded and numeric columns accept only the blank written as `null`. A CSV export with blanks therefore fails on every such cell (open item 13; the steward chose to validate JSON exports for now). A JSON array of row objects with `null` for blanks validates as intended.
- **The data stays where it is.** If the data lives in a secure environment, bring this package and the validator to the data; the validator is a single Python file plus `jsonschema`.
- Open `dictionary.html` by double-click: a searchable dictionary of all six tables (keyword search is built in; the Semantic search switch fetches a small model once, then also finds related variables by meaning).
- For the toy-data viewer and live validator, run `python3 -m http.server 8000` from this folder, then open `http://localhost:8000/playground-baseline.html` (one page per table). Serve the whole folder so `assets/vendor/` travels with the page.

## 10. Open items to confirm with the data provider

None of these can be answered from the dictionary. Each stays as written until the data provider answers.

1. **Participant identifier.** Which column identifies a donor? The overview mentions a release-specific `ID_PROJECTID` merge column, but no variable lists it. (D010, D011)
2. **Leisure-activity column names.** The dictionary has one row per activity (`leis_cswim … _24m`) covering a frequency, an hours and a minutes column. Are the delivered names `leis_cswimFreq_24m`, `…Hrs_24m`, `…Min_24m`? (D012)
3. **The 60 `enmo_*` columns.** The row `enmo_0plus – enmo_4000plus` "will provide 60 variables" but lists none; the row is deferred. (D013, D078)
4. **Unticked checkboxes.** What does an unticked option hold in the restless-legs and Pica questions: blank, 0 or 2? (D060)
5. **Linked records.** Is the Caliber data a separate dataset (with `CenDate`) or four columns joined to the donor, and what do the columns hold? (D086)
6. **`ethnicPulse`.** What does it hold, and does it use the same coding as `ethnic_bl`? (D020)
7. **Date format.** What is the delivered format in every date column? (D022)
8. **Omics columns.** What do the 14 baseline and 16 24-month omics columns hold (a sample ID, a flag, a path), and are they delivered as columns? (D046, D084)
9. **Markers.** What do the `&`, `#`, `*` and `£` marks in the dictionary mean? (D015)
10. **Who "not applicable" is for.** Who is `998 = not applicable` for on the 17 items at 24 months, and what is in the cell for someone not asked? (D014)
11. **Women-specific items.** What do men carry in `hrt_bl`, `pill_bl`, `menopause_bl`, and is a rule wanted? (D030)
12. **Who the "If so" items apply to.** What do `ageVeg_bl` (meat-eaters), `rls_9b_18m` (when `rls_9a_18m` is no) and `supp_otc_2_24m` (when `supp_otc_24m` is no) hold? Is `outCome` numeric or text with trailing zeros (`1.10`)? (D036, D059, D067, D023)
13. **How the data will be delivered.** The package is set up to validate JSON exports in which a blank is `null` (the steward's choice, D094). A CSV with blank cells fails the validator (§9). If the data arrives as CSV, revisit: also accept the empty string as a written form of the blank, or convert blanks to `null` before validating. (D092, D094)
