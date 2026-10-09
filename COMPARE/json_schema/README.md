# COMPARE — data dictionary as JSON Schema

This package is a machine-checkable version of the COMPARE data request form (`dataRequestForm_COMPARE_EXT_Template_v3.xlsx`). It describes the variables that carry an `X` in that form's *Requested* column: **354 variables converted, in six tables**. The older v1 form and the 74 unrequested rows are out of scope (see §8). Everything here is transcribed from the dictionary; nothing was added from outside it (see §3 and §7).

A consumer with this folder and Python can validate data (`tools/validate.py`), browse the dictionary (`dictionary.html`) and read the rules (this file). Nothing here needs the tool that built it.

## 1. What this package describes

COMPARE is a study comparing methods of measuring haemoglobin in whole blood donors (published article: https://pmc.ncbi.nlm.nih.gov/articles/PMC8048787). The dictionary arrives as a data request form with one sheet per kind of data, and each table below is one sheet of requested variables, one row per donor, with column names exactly as the dictionary spells them.

| Table | Mother file | One row is | Categories (variables) |
|---|---|---|---|
| `basic_info` | `basic_info/basic_info.schema.json` | one donor in the recruitment record — 5 | Identification (1), Demographics (3), Blood Group (1) |
| `questionnaires` | `questionnaires/questionnaires.schema.json` | one donor in the questionnaires — 150 | Questionnaire Completion (4), Demographics (1), Anthropometric (2), Fitzpatrick Skin Type (9), General Health (36), Medical History (54), Blood Donation (2), Reproductive/Hormonal (3), Behavioral (12), Dietary (23), Occupation & Physical Activity (4) |
| `hb_measurements` | `hb_measurements/hb_measurements.schema.json` | one donor in the haemoglobin measurements taken at donation — 6 | Haemoglobin Measurements (6) |
| `bloods` | `bloods/bloods.schema.json` | one donor in the research blood sample results, visit 1 and visit 2 side by side — 180 | Blood Counts & Assays, Visit 1 (90), Blood Counts & Assays, Visit 2 (90) |
| `biomarkers` | `biomarkers/biomarkers.schema.json` | one donor in the Nightingale biomarker results — 10 | Blood Biomarkers (10) |
| `omics` | `omics/omics.schema.json` | one donor in the omics and linkage items — 3 | Omics (3) |

`donationHistory`, `adverseEventHistory` and `EHRData` have no requested variable, so no tables come from them. `basic_info` lists `identifier` ("unique anonymous identifier"); the other requested sheets do not, so only that table carries it (open item 1, §10).

## 2. Layout and composition

```
README.md   VARIABLES.csv   ROUTING.csv   dictionary.html   playground-<table>.html
common/defs.json                         shared definitions (§4)
<table>/<table>.schema.json              the mother file: an array of row objects
<table>/categories/<category>.json       one file per category
examples/<table>/toy_valid.json, toy_invalid.json, toy_invalid_ledger.json
tools/validate.py   tools/requirements.txt   assets/   (the page libraries)
```

A row is the `allOf` union of its category files. Every category file lists all of its properties as `required`, so every column must be present in every row. The mother file's single `unevaluatedProperties: false` rejects any column the dictionary does not list.

## 3. Value-encoding conventions

- **Codes are `oneOf` single-value constants, each with the dictionary's own label as its title.** Measures are `anyOf` a number plus the blank. Code labels, variable titles and units are the dictionary's own words, typos included (§7).
- **Ranges are asserted only where the dictionary states one**: `ht` is 0 – 2.99 metres, `wt` is 38 – 190 kilograms (`777 > 190kg` is its own labelled code), and the ranges written beside labelled codes such as `10 – 70 = age started`. Where it states none, none is asserted, and measured values are typed `number` because the dictionary states no data types.
- **Units** are carried as `x-unit` exactly as written in the dictionary: `g/l` for the Haemospect and Hemocue haemoglobin values but `g/dL` for Orsense; `109/L` and `1012/L` are kept as written (most likely 10⁹/L and 10¹²/L with the superscripts lost).
- **Dates** are plain text with no pattern: the dictionary says only "Date" (open item 8).
- **Whole numbers** are assumed for ranges such as `1 - 70` because the fractional values (such as `0.1`) are listed as their own labelled codes. A real extract with decimals in those columns would be flagged.
- **Shared codings** are defined once per category file and referenced by each item, which keeps its own title.
- **Checkbox questions** that the dictionary writes as one row (`pica_1 – pica_7`, `rls_6a – rls_6g`, `rls_7a – rls_7g`) are one column per option, each holding only the code the dictionary states (`1`).
- **Notes on columns** (`x-universe`) that summarise a sheet note are kept on `ageVeg`, `rls_9b` and the `_p2` dates; they are descriptions, not rules.
- **`$id` base.** All schemas use `https://schemas.example.org/cd3-compare-pilot/`, a placeholder that is never fetched. Replace it before publishing the schemas anywhere public.

## 4. Sentinel semantics

| Value | Meaning | Where it applies |
|---|---|---|
| `null` | "No value recorded": the data provider's blank. The dictionary defines no code for a missing value, and none was added. | every column |
| `999` | don't know / prefer not to answer | the questionnaire items whose dictionary codes list it; a few items give only "don't know" and carry that label on the item |
| `998` | not applicable | the restless-legs follow-up items (`rls_3`, `rls_4`, `rls_5`, `rls_8`, `rls_9a`, `rls_9b`, `rls_10` to `rls_13`) and `Breathless_scale`; the dictionary does not say who they are not applicable for (§6) |
| `777` | **a value, not a missing code**: "greater than N" (`777 > 190kg`, `more than 20 times per week`, `more than 75 years old`) | the items whose dictionary codes list it, each labelled |

Other labelled codes are exactly the dictionary's own and keep its labels, for instance `0.1 = less than once a week`, and `0 = no` on `hrt` and `pill` (elsewhere "no" is `2`). On the four health-belief items, code `3` ("don't know") is a real answer and `999` is separate.

## 5. Enforced routing rules

The routing policy is **faithful**: only rules the dictionary's own wording states are enforced, and none are added from domain knowledge. **No routing rule is enforced.** One rule, R002 (`rls_9b` asked only if `rls_9a` is yes), was encoded during the conversion and removed at the review because the dictionary does not state it (D046); see §6.

## 6. Documented but not enforced

**Routing the dictionary words or hints at but gives no rule or value for** (register: `ROUTING.csv`, all `not-enforceable` or `declined`):

| Rule | What the dictionary says | Why it is not enforced |
|---|---|---|
| R001 | `ageVeg` is for "(vegetarians only)" | no value is given for meat-eaters |
| R002 | `rls_9b` begins "If so" (after `rls_9a`) and has `998 = not applicable` | declined (D046): the dictionary states no rule |
| R003 | a note says some participants completed a second questionnaire (`commsCode`), with the `_p2` dates | the note states no rule; `commsCode` is in another table and not requested |
| R004 | each donor had one non-invasive spectrometer (Haemospect or Orsense), per the published article | not in the dictionary; no requested column says which |
| R005 | the restless-legs follow-up items have `998 = not applicable` | who it is not applicable for is not stated |
| R006 | `Breathless_scale` has `998 = not applicable` | not stated |

Other items read as dependent on an earlier answer (the ever/current pairs in smoking and drinking, `eatTyp_when`, the iron-frequency items after the iron-supplement items, the women-specific `hrt`/`pill`/`menopause`), but the dictionary states no rule, so none is enforced.

**Checks JSON Schema cannot make, which a consumer should apply downstream:**

- Row uniqueness and the `identifier` format (§1).
- Which spectrometer's columns a donor should have (`Hb_hs`/`spkDate_hs` or `Hb_os`/`orsDate_os`).

## 7. Known source issues handled

Titles and labels are the dictionary's own words; where a defect is visible, the schema keeps the source text and a `$comment` on the column notes it.

- **Typos kept in titles/labels:** "limit to" for "limit you" (`vig`, `mod`, `lift`, `stairA`, `stairB`), "impedence" (`PLT_I_*`), "corposcular" (`RBC_He_pg_*`), "as, a result of giving blood" (`pa_change`), "lying, down" (`rls_4`), "non-nutritional substances." (the Pica question).
- **`smStopAge`** ("How old were you when you stopped smoking?") labels its 10 – 70 range "age started", copied from `smStartAge`; kept as written.
- **Haemoglobin units differ by device** (g/l vs g/dL); kept as written, not converted.
- **Names:** the dictionary's checkbox codings write `Pica_1`, while the row is named `pica_1`; the schema uses the row's name.
- **Group rows:** the dictionary lists some questions as one row for several columns (`pica_1 – pica_7`, `rls_6a – rls_6g`, `rls_7a – rls_7g`); they are expanded to one column per option. The two ranking groups (`importance1 – importance5`, `preference1 – preference3`) are not requested.
- **Not variables or not named:** the `bloods` sheet has a data row with no variable name ("Time of appointment.", visit 2; not requested); the questionnaires note about blue cells refers to formatting that is not text; `commsCode` and `team` on `basicInfo` are not requested (open items 2 and 3).
- **v1 vs v3:** the older v1 form differs from v3 by the `X` ticks, a new `biomarkers` sheet, a changed `EHRData` sheet and the overview heading; names and codings compared are identical.

## 8. Sources and provenance

- **Dictionary used:** `raw_data/dataRequestForm_COMPARE_EXT_Template_v3.xlsx` (Excel; 9 data sheets plus an overview; one row per variable; the column layout differs by sheet); registered 2026-10-06. Only rows with `X` in `Requested` are converted (336 listed rows, expanding to 354 columns); the other 74 rows are listed in `VARIABLES.csv` as `dropped`.
- **Registered but not used:** `dataRequestForm_COMPARE_EXT_Template_v1.xlsx` (older version of the same form, no `X` ticks).
- **External source consulted:** the published COMPARE article https://pmc.ncbi.nlm.nih.gov/articles/PMC8048787 (2026-10-06) — visits, devices, no skip logic or identifier scheme. A web search for questionnaires, skip logic and data-dictionary documentation found nothing further; the trial registration https://www.isrctn.com/pdf/90871183 was not consulted. The steward has no other documents.
- **Not used as a source:** an earlier set of auto-generated schemas for this cohort; this package transcribes from the dictionary only.
- **Steward's rulings** (scope, grain, tables per sheet, missing-value convention, faithful routing, validation target) are recorded in the project's working notes and summarised in §3–§6.

## 9. Validating and browsing

```
pip install -r tools/requirements.txt      # or use: uv run tools/validate.py …
python3 tools/validate.py summary .        # schemas, fixtures, coverage, routing — everything
python3 tools/validate.py data . --file your_export.json --table questionnaires
```

- **Validate a JSON export, not a CSV with blank cells.** The validator reads an empty CSV cell as an empty string, and the coded and numeric columns accept only the blank written as `null`; a CSV with blanks fails on every such cell. A JSON array of row objects with `null` for blanks validates as intended (steward's choice, D007).
- **The data stays where it is.** If the data lives in a secure environment, bring this package and the validator to the data; the validator is a single Python file plus `jsonschema`.
- Open `dictionary.html` by double-click: a searchable dictionary of all six tables (keyword search is built in; the Semantic search switch fetches a small model once, then also finds related variables by meaning).
- For the toy-data viewer and live validator, run `python3 -m http.server 8000` from this folder, then open `http://localhost:8000/playground-questionnaires.html` (one page per table). Serve the whole folder so `assets/vendor/` travels with the page.

## 10. Open items to confirm with the data provider

None of these can be answered from the dictionary. Each stays as written until the data provider answers.

1. **The identifier.** What format does `identifier` have, and do the other tables carry it as a join key? (D009)
2. **Things in the dictionary file itself.** The `bloods` row 97 with no variable name ("Time of appointment.", visit 2); the blue cells on `questionnaires` that mark the second questionnaire's variables; the meaning of the marker column (`&`, `#`, `*`, `^`). (D010)
3. **The second questionnaire and the spectrometers.** `commsCode` is not requested: what do participants who completed one questionnaire hold in the `_p2` columns? No requested column says which spectrometer (Haemospect or Orsense) a donor had: what do the other device's columns hold? (D011)
4. **Unticked checkboxes.** In the restless-legs and Pica questions, what does an unticked box hold: blank, 0 or 2? (D030)
5. **Who "not applicable" is for.** Who is `998` for on `rls_3`, `rls_4`, `rls_5`, `rls_6g`, `rls_7g`, `rls_8`, `rls_9a`, `rls_9b`, `rls_10` to `rls_13` and `Breathless_scale`, and what is in the cell for someone not asked? (D032)
6. **Omics columns.** What do `Affymetrix_QC`, `smearID_v1` and `smearID_v2` hold, and are they delivered as columns? (D040)
7. **Ethnicity.** What does `ethnicPulse` hold, and does it use the same coding as the questionnaire's `ethnic`? (D013)
8. **Date format.** What is the delivered format in every date column? (D015, D035)
9. **Women-specific items.** What do men carry in `hrt`, `pill` and `menopause`? (D020)
10. **Who the "(vegetarians only)" item applies to.** What do meat-eaters hold in `ageVeg`? (D024)
