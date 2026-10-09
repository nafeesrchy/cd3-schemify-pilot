# MWS — Million Women Study data package

## 1. What this package describes

The Million Women Study (MWS) is a UK cohort study recruiting women through the NHS Breast Screening Programme from the mid-1990s onward, run by the Cancer Epidemiology Unit (CEU), University of Oxford. This package covers all three waves in the source dictionary: the baseline recruitment questionnaire, the 3-year ("yellow") follow-up resurvey, and the 8-year ("lilac") follow-up resurvey.

| Table | Mother file | Row grain | Categories | Vars |
|---|---|---|---|---|
| `recruitment` | `recruitment/recruitment.schema.json` | One participant's baseline record | 8 (below) | 65 |
| `resurvey_3yr` | `resurvey_3yr/resurvey_3yr.schema.json` | One participant's 3-year follow-up record | 12 (below) | 149 |
| `resurvey_8yr` | `resurvey_8yr/resurvey_8yr.schema.json` | One participant's 8-year follow-up record | 7 (below) | 38 |

### `recruitment` categories

| # | Category | File | Vars |
|---|---|---|---|
| 1 | Demographics | `categories/demographics.json` | 5 |
| 2 | Socioeconomic | `categories/socioeconomic.json` | 3 |
| 3 | Anthropometric | `categories/anthropometric.json` | 3 |
| 4 | Behavioral | `categories/behavioral.json` | 5 |
| 5 | Reproductive/Hormonal | `categories/reproductive_hormonal.json` | 21 |
| 6 | Breast Health | `categories/breast_health.json` | 3 |
| 7 | Gynae Surgery | `categories/gynae_surgery.json` | 6 |
| 8 | Medical History | `categories/medical_history.json` | 19 |

Drawn from three sheets of the source dictionary (`Basic information`, `Recruitment variables`, `Self-reported health at recruit`).

### `resurvey_3yr` categories

| # | Category | File | Vars |
|---|---|---|---|
| 1 | Demographics | `categories/demographics.json` | 2 |
| 2 | Medical History | `categories/medical_history.json` | 21 |
| 3 | Reproductive/Hormonal | `categories/reproductive_hormonal.json` | 7 |
| 4 | Medications | `categories/medications.json` | 20 |
| 5 | Behavioral | `categories/behavioral.json` | 9 |
| 6 | Anthropometric | `categories/anthropometric.json` | 7 |
| 7 | Early Life | `categories/early_life.json` | 8 |
| 8 | Parental Mortality | `categories/parental_mortality.json` | 12 |
| 9 | Family History | `categories/family_history.json` | 27 |
| 10 | Socioeconomic | `categories/socioeconomic.json` | 15 |
| 11 | Wellbeing/Sleep | `categories/wellbeing_sleep.json` | 7 |
| 12 | Dietary | `categories/dietary.json` | 14 |

Drawn from two sheets of the source dictionary (`3-year resurvey`, `Dietary data at 3-year resurvey`), merged into one table since both describe the same wave and grain.

### `resurvey_8yr` categories

| # | Category | File | Vars |
|---|---|---|---|
| 1 | Demographics | `categories/demographics.json` | 2 |
| 2 | Medical History | `categories/medical_history.json` | 16 |
| 3 | Gynae Surgery | `categories/gynae_surgery.json` | 2 |
| 4 | Reproductive/Hormonal | `categories/reproductive_hormonal.json` | 4 |
| 5 | Behavioral | `categories/behavioral.json` | 9 |
| 6 | Anthropometric | `categories/anthropometric.json` | 2 |
| 7 | Family History | `categories/family_history.json` | 3 |

Drawn from a single sheet (`8-year resurvey`) — no separate dietary sheet exists for this wave. Noticeably smaller than `resurvey_3yr`: it drops Medications, Early Life, Parental Mortality, Socioeconomic, Wellbeing/Sleep, and Dietary entirely, and shrinks both Gynae Surgery (to hysterectomy only) and Family History (to breast-cancer-only across mother/father, plus a sister field not asked about in either other table).

All 6 sheets in the source dictionary are now in scope, across the three tables above.

Category names and groupings in `recruitment` deliberately match the CD3 target schema's own seven domains (Demographics, Socioeconomic, Anthropometric, Behavioral, Reproductive/Hormonal, Medical History, Screening) rather than an arbitrary local scheme, to make the later cross-cohort `/harmonize` mapping more direct. `resurvey_3yr` and `resurvey_8yr` reuse the same domain names where a category matches, and each introduces its own where its questionnaire asks about things the others didn't (`resurvey_3yr`: Medications, Early Life, Parental Mortality, Family History, Wellbeing/Sleep; `resurvey_8yr` reuses names throughout but with much narrower category contents) — category sets are not required to match across tables.

## 2. Layout and composition

```
json_schema/
├── README.md                                  ← this file
├── VARIABLES.csv                              ← inventory; coverage ground truth (kept forever)
├── common/defs.json                           ← shared sentinel (-1 only; see section 4)
├── recruitment/
│   ├── recruitment.schema.json                ← mother file: array of row objects + routing rules
│   └── categories/*.json                      ← 8 category files
├── resurvey_3yr/
│   ├── resurvey_3yr.schema.json                ← mother file: array of row objects + routing rules
│   └── categories/*.json                      ← 12 category files
├── resurvey_8yr/
│   ├── resurvey_8yr.schema.json                ← mother file: array of row objects + routing rules
│   └── categories/*.json                      ← 7 category files
├── examples/
│   ├── recruitment/                           ← toy fixtures (67 valid, 41 invalid + ledger)
│   ├── resurvey_3yr/                          ← toy fixtures (12 valid, 93 invalid + ledger)
│   └── resurvey_8yr/                          ← toy fixtures (9 valid, 40 invalid + ledger)
├── tools/                                     ← validator + requirements.txt
├── dictionary.html                            ← searchable data dictionary, all three tables
├── playground-recruitment.html                ← toy-data viewer + live validator, recruitment
├── playground-resurvey_3yr.html                ← toy-data viewer + live validator, resurvey_3yr
├── playground-resurvey_8yr.html                ← toy-data viewer + live validator, resurvey_8yr
└── assets/                                    ← vendored rendering library
```

A row in any table is the `allOf` union of that table's category files, plus that table's routing conditionals (section 5). No category file closes itself with `additionalProperties` — each mother file's single `unevaluatedProperties: false` is the only place unknown columns are rejected, so every category in a table can coexist under that table's `allOf`. All three tables share `common/defs.json`'s sentinels but are otherwise independent schemas — there is currently no field linking a row in one table back to the same participant's row in another (see section 10).

## 3. Value-encoding conventions

- **Codes get `oneOf`**: a categorical variable — Yes/No, a labeled scale — is a `oneOf` of single-value `const` branches, each carrying its own `title` (the label), plus a plain `{"type": "null"}` branch for no value. Never a bare `enum`.
- **Measures get `anyOf`**: a continuous or counted variable is an `anyOf` of one numeric branch plus a `{"type": "null"}` branch. A numeric branch carries `minimum`/`maximum` **only when the source dictionary states that exact range directly** (see below) — no agent-decided or agent-derived bound survives in the schema. A handful of fields mix a numeric branch with the source's own labeled special codes (e.g. `F1MENOAG`'s 77/99, `F1ALCNUM`'s 97/99); these use `anyOf` rather than `oneOf`, since an unbounded numeric branch and a specific coded value are not mutually exclusive by construction (a bounded branch would have been, which is why 8 such fields were converted from `oneOf` to `anyOf` when their bounds were removed — see D101).
- **Bounds are dictionary-stated only.** Following Montse's review of the pilot methodology, this package no longer carries any bound, code, or skip rule that the source dictionary and questionnaires do not themselves contain. A bound survives in the schema only when the dictionary's own D/E columns state that exact range for that field directly (e.g. `RHEIGHT` 120–200, `RMENARCH` 7–20); where the source states only a one-sided range (e.g. `RAGE`'s stated minimum of 48, with no maximum), only that stated side is kept. Every bound that was previously agent-decided (a plausibility guess) or agent-derived (combining separate stated facts into a number the dictionary never itself states, e.g. the old `RYOB` range) has been removed entirely — see D101–D104 for the full accounting of what was removed per table, and the earlier, superseded entries (D010–D099) for the original plausibility-bound reasoning this replaces.
- **Title separator**: em dash (—). **Formatting**: 2-space indent, one key per line. Each table's category titles carry a distinct prefix ("MWS Recruitment — {category}", "MWS 3-year resurvey — {category}", "MWS 8-year resurvey — {category}") so a category list spanning multiple tables (e.g. three different "Demographics") is never ambiguous.
- **`$id` base**: `https://schemas.example.org/cd3-mws-pilot/` — a **placeholder**, not a real namespace. Replace it before publishing these schemas anywhere public; nothing dereferences it, it exists only so `$ref` resolution is unambiguous.

## 4. Missingness semantics

Only one sentinel remains as a `const` value in this package:

| Code | Meaning | Where it applies |
|---|---|---|
| `-1` | Not on questionnaire | Adopted verbatim from the source's own code lists, wherever the source documents it for a specific field. Each table has its own questionnaire-version scheme: `recruitment` uses Aqua/Blue/Other; `resurvey_3yr` uses 4 numeric codes (9903/9907/9909/0012, tracked by `F1QTYPE`); `resurvey_8yr` uses only 2 (0512/0605, tracked by `F2QTYPE`), and uniquely, `F2QTYPE`'s own code values literally *are* the version tags rather than small ordinals — a third, distinct convention. Some fields carry `-1` even though the source's own availability columns mark them available on every version (e.g. `resurvey_3yr`'s `F1MDOLD`) — kept exactly as the source coded it, most likely a source documentation inconsistency. Conversely, some fields genuinely unavailable on early versions document no `-1` at all (e.g. `resurvey_3yr`'s `F1MHTCM`, and 4 mother fields in its Family History category) — also kept as given, not invented. |

`-999` (the package's old generic "missing" fallback) and `-777` (the old "not applicable" marker) are both retired. Neither is a code the source dictionary documents anywhere — both were an earlier, agent-invented convention adopted to satisfy the "missingness must be in-band, never bare `null`" convention this pilot originally followed. Per Montse's review, that convention itself doesn't survive when it requires inventing numbers the source never states: **every field's "no substantive value" case is now plain JSON `null`**, with no numeric sentinel attached, whether the reason is ordinary non-response or structural routing.

**This has a real, acknowledged consequence: the schema can no longer distinguish those two reasons.** Before, `-999` meant "should have a value but doesn't, for an unrecorded reason" and `-777` meant "structurally outside this field's universe" — two different facts about the same absence. Collapsing both to `null` means a mother-file routing rule that requires a field to be non-`null` when the participant is in-universe (section 5) can no longer tell a genuinely-skipped value apart from an ordinary blank answer a real respondent just didn't fill in — both are `null`, and the rule rejects both alike. The package keeps enforcing these rules anyway (an explicit steward decision, not an oversight): the alternative would be inventing a second null-like marker to tell the two apart, which is exactly the kind of invented code this retrofit exists to remove. Anyone validating real data against this package should expect **false rejections on genuinely-answered-but-blank in-universe fields** as a known limitation, not a bug — see D105.

Many fields across all three tables are also checkbox-style ("tick all that apply" or "tick if this applies," e.g. `recruitment`'s and `resurvey_3yr`'s medical_history/medication/family-history fields, `resurvey_8yr`'s illness/operation fields — 54 fields package-wide): the source documents only `1=Yes` for these, with no `2=No`, because an unticked box *is* the negative answer on the real questionnaire, not a missing one — but the schema has no branch for it, so an unchecked box falls to `null` regardless of which of those two things is actually true. **This is a spurious-missingness risk at data-intake time, not just a downstream-analyst ambiguity**: whoever maps real questionnaire data into this schema must not auto-map a blank/unticked cell straight to `null` for these fields without first establishing, per field, whether blank means No or means truly unrecorded — doing so silently reclassifies real "No" answers as missing, and any analysis that treats a missing value differently from a real answer (e.g. dropping it, or excluding it from a prevalence denominator) would then systematically undercount. See section 6 and D100.

## 5. Enforced routing rules

Every rule below is a real `if`/`then` pair in the relevant mother file's `allOf`, checked by the validator — not documentation of intent. Each was re-verified directly against the real questionnaire PDFs (`raw_data/mws-Q1.pdf`, `mws-Q3.pdf`, `mws-Q8.pdf`) rather than taken on trust from this package's own earlier notes (see D101–D104) — the question number cited for each rule is where that verification came from. The `then` target for a skipped field is now plain `null` throughout (previously the invented `-777` sentinel — see section 4 for why, and for the enforcement caveat this leaves).

### `recruitment.schema.json` (verified against `mws-Q1.pdf`)

1. **RANYCHLD** (ever had children) gates the whole pregnancy/breastfeeding block: No → `RNUMFTP`, `RAGEFB`, `RAGELB`, `RBFYN`, `RBFNUM`, `RBFDUR` are all `null`. Q12: *"Have you ever had any children? No / Yes — if No, please go on to question 15"* (questions 13–14 cover this whole block).
2. **RBFYN** (ever breastfed), nested within #1: No → `RBFNUM`, `RBFDUR` are `null`. `RBFYN`/`RBFNUM`/`RBFDUR` are themselves derived from Q14's per-child breastfeeding grid ("put 0 if you did not breastfeed that child"), so this is a direct consequence of that grid's own printed convention, not a separate inference.
3. **ROC** (ever used oral contraceptives): No → `ROCSTART`, `ROCSTOP`, `ROCDUR` are `null`. Q28: *"Have you ever used the pill (oral contraceptive)? Yes / No — if No, please go to question 32."*
4. **RHTNPC** (HRT never/past/current): Never → `RHRTSTA`, `RHTDUR`, `RHRTSTO`, `RHRTMP`, `RHTTYPE`, `RHTLU` are all `null`. Q32: *"Have you ever used hormone replacement therapy (HRT)? No — if No — please go to question 39 / Yes."*
5. **RHTNPC**, narrower: Current (still using, hasn't stopped) → `RHRTSTO` (age last used), `RHTLU` (time since last used) are `null`, even though the participant has used HRT. Q36: *"Are you now using HRT? Yes / No — if No, how old were you when you last used HRT?"*
6. **RPSTOPYN** (periods stopped): No or Irregular → `RPSTOPAG` is `null`. Q40: *"Have your periods NOW stopped? ... Yes — If Yes, how old were you when they stopped?"*
7. **RHYST** (hysterectomy): No → `RHYSTAG` is `null`. Q25: *"Have you had a hysterectomy? No / Yes — If Yes, how old were you?"*
8. **ROOPH** (bilateral oophorectomy): No → `ROOPHAGE` is `null`. Q26: *"Have you had BOTH ovaries removed? No / Not sure / Yes — If Yes, how old were you?"* (`ROOPH=3`, "Not sure", deliberately does **not** trigger this — left unconstrained, an explicit steward call.)
9. **RSTER** (sterilised): No → `RSTERAGE` is `null`. Q27: *"Have you been sterilised (had your tubes tied)? No / Yes — If Yes, how old were you?"*

Each rule above is paired with its applicability half (in-universe ⇒ the field must carry a real value, never `null`) — both halves are separate conditionals in the mother file, both fixture-tested. See section 4 for why that applicability half can now also reject a genuinely-answered-but-blank field, not just a wrongly-skipped one.

`RCIGSPD` (cigarettes per day) was investigated for a similar rule but does **not** have one: Q7 asks it independent of smoking status ("about how many cigarettes do you smoke on average each day, now?"), and a non-smoker answers the field's own `1=None` directly — there is no not-applicable case.

### `resurvey_3yr.schema.json` (verified against `mws-Q3.pdf`)

1. **F1HTNPC** (HRT never/past/current): Never → `F1HRTSTA`, `F1HTTYPE`, `F1HTDUR`, `F1HTLU` are all `null`. Q8: *"Have you ever used HRT (hormone replacement therapy)? No — if No — please go to question 13 / Yes."* (`F1HTNPC=4`, "Ever, status not known", deliberately does **not** trigger this — left unconstrained, an explicit steward call, same treatment as `ROOPH=3` above.)
2. **F1HTNPC**, narrower: Current → `F1HTLU` (time since last used) is `null`. Q10: *"Are you now using HRT? No — if No, when did you stop using HRT? / Yes."*
3. **F1SMOKE**: Never → `F1CIGSPD` (cigarettes per day) is `null`. Q46: *"Have you ever been a smoker? No — if No — please go to question 50 / Yes."* Unlike `RCIGSPD` above, this table's smoking question is gated by a real printed skip instruction.
4. **F1MALIVE** (mother still alive): Yes → `F1MDAGE` and all 7 mother cause-of-death fields (`F1MDHRT`, `F1MDSTR`, `F1MDPNU`, `F1MDOLD`, `F1MDCABR`, `F1MDCAWO`, `F1MDCAOV`) are `null`; No (deceased) → `F1MAGE` is `null`. Q42 asks age-now or age-at-death depending on the answer, and Q43 is explicitly headed *"If your mother has died, what did she die from?"* — a printed conditional, not an inference. (`F1MALIVE=3`, "Do not know", deliberately does **not** trigger either half — left unconstrained, an explicit steward call.) The 7 cause-of-death fields are not required to carry a real value even when the mother has died — see section 6 for the residual ambiguity this leaves.
5. **F1PART** (currently has a partner): No → `F1PARTSM` (partner smokes) is `null`. Q52: *"Are you currently married or living with a partner? No / Yes — does your husband/partner smoke?"*
6. **F1MED** (used any medication, not HRT, in the last 4 weeks): No → all 19 specific medication fields are `null`. Q13: *"Have you taken any medications (other than HRT) for most of the last 4 weeks? No / Yes  If Yes, was it: [drug checklist]."* Same residual ambiguity as #4 in the other direction — see section 6.

Each rule above is paired with its applicability half where one exists (rules #4's `F1MAGE`/`F1MDAGE` halves, #1, #2, #3, #5) — both halves are separate conditionals in the mother file, both fixture-tested. Rules #4's cause-of-death half and #6 are single-direction by design (see section 6).

Two relationships were investigated and found to need **no** rule, both confirmed against the questionnaire's own "put 0 if..." instructions: `F1ALCNUM`/`F1ALCEAT`/`F1ALCDAY` (Q30: "put 0 if you do not drink, or have less than one drink each week" — a non-drinker answers `0` directly, a real value, not a sentinel) and `F1MOBFRQ`/`F1MOBYRS` (Q53: "put 0 if never or less than 1 year" — same reasoning). The 9 social-activity checkboxes, Family History's 27 mother/father fields, and medical_history's 20 illness/treated-now checkboxes have no gating field at all and were confirmed independent before drafting.

### `resurvey_8yr.schema.json` (verified against `mws-Q8.pdf`)

1. **F2HTNPC** (HRT never/past/current): Never → `F2HTTYPE`, `F2HTDUR`, `F2HTLU` are all `null`. Q27: *"Have you ever used HRT? No — if No — please go to question 31. / Yes."* Note this table has no "age started HRT" field at all, unlike the other two.
2. **F2HTNPC**, narrower: Current → `F2HTLU` (time since last used) is `null`. Q28: *"Are you now using HRT? No — if No, when did you stop using HRT? / Yes."*
3. **F2ALCNUM** (alcoholic drinks per week): Q56: *"About how much alcohol do you drink each week? ... If you have less than one drink a week, please go to question 60"* — so `F2ALCNUM=0` → `F2ALCEAT` (drinks with meals) and `F2ALCDAY` (days per week) are both `null`. Confirmed *not* to extend to the tea/coffee questions (Q45 in this table), which are asked of every participant regardless. This is a genuinely different answer from `resurvey_3yr`'s equivalent fields (rule-free, see above) — the two waves' questionnaires route differently.
4. **F2SMOKE**: Never → `F2CIGSPD` (cigarettes per day) is `null`; Past or Current → `F2CIGSPD` must be real. Q66: *"Have you ever been a smoker? No — if No — please go to question 70. / Yes"*; Q69's own wording ("About how many cigarettes do you/did you smoke on average each day? (if you are an ex-smoker, how many did you smoke on average when you smoked?)") confirms it covers **both** current and past smokers — a different shape from both `RCIGSPD` (no skip at all) and `F1CIGSPD` (Never-only skip) above.

Each rule above is paired with its applicability half. `F2HYST`/`F2HYSTAG` (hysterectomy / age at hysterectomy) was investigated and confirmed to match `RHYST`/`RHYSTAG`'s semantic relationship (rule #7 above), but `F2HYST` is checkbox-style with no explicit "No" code to key an enforceable rule off of — no printed conditional exists to verify against here, unlike the other rules above, so it stays unenforced by steward's explicit choice rather than risk conflating "no hysterectomy" with "genuinely unrecorded." Gynae Surgery, Medical History, and Family History in this table have no gating field among their own checkbox items and were confirmed independent before drafting.

## 6. Documented but not enforced

JSON Schema cannot compare one column's value against another's, so these real rules are recorded here and in the relevant category file's `$comment`, but nothing rejects a row that violates them:

- `RAGELB` (age at last birth) should be ≥ `RAGEFB` (age at first birth), when both are substantive.
- `ROCSTOP` (age stopped oral contraceptives) should be ≥ `ROCSTART`.
- `RHRTSTO` (age last used HRT) should be ≥ `RHRTSTA` (age started HRT).
- `RDEP5` (deprivation quintile) and `RDEP3` (deprivation tertile) are both derived from the same Townsend index and should be mutually consistent (e.g. `RDEP5` ∈ {1,2} implies `RDEP3=1`).
- `resurvey_3yr`'s three dietary macronutrients (`F1NPROT`, `F1NTFAT`, `F1NCARB`) roughly sum to the energy total (`F1NKJ`) via standard conversion factors, but the source doesn't document its exact factors or rounding, so no approximate identity is enforced.
- `resurvey_3yr`'s `F1MALIVE`-gated cause-of-death block: a downstream analyst cannot distinguish "all 7 fields blank because the mother is alive" from "all but one blank because she died of an unlisted or unrecorded cause" without cross-referencing `F1MALIVE` directly — the schema pins the *alive* case to `null`, but an unchecked box within the *deceased* universe also falls to generic `null`, indistinguishable from a genuine gap. The same residual ambiguity applies to `resurvey_3yr`'s `F1MED`-gated medication block in the other direction.
- `resurvey_8yr`'s `F2HYST`/`F2HYSTAG`: the same semantic relationship as `RHYST`/`RHYSTAG` holds, but is not enforced at all (see section 5) — a downstream analyst should treat `F2HYSTAG` as potentially meaningful even when `F2HYST` is missing, and vice versa, since neither field constrains the other.
- **All 54 checkbox-style fields package-wide** (only `1=Yes` documented, no `2=No`): the schema cannot distinguish "unticked, meaning No" from "genuinely not recorded" — both map to `null`. This is a data-intake caution, not just a downstream one: whoever maps real data into this schema must not default a blank/unticked cell to `null` without first establishing, per field, whether blank means No or means truly unrecorded — otherwise real "No" answers silently become indistinguishable from missing data (D100).
- **Every enforced routing rule in section 5, in its applicability direction**: since `null` no longer distinguishes "structurally skipped" from "genuinely not answered" (section 4), a real, valid non-response on an in-universe field will be wrongly rejected by these rules. This is a known, accepted limitation (D105), not something a downstream analyst can work around from the schema alone — real validation failures of this shape should be checked by hand before being treated as data-quality problems.

## 7. Known source issues handled

- **`resurvey_3yr`'s `-1` sentinel is inconsistently documented across otherwise-similar fields.** Most version-gated fields (unavailable on the earliest two questionnaire versions) carry a source-documented `-1='Not on questionnaire'` code that lines up with their own availability columns — but a few don't, despite the same unavailability (`F1MHTCM` vs. its `F1FHTCM` counterpart; 4 of 13 mother fields in Family History vs. their father counterparts; `F1MDOLD` even more unusually carries `-1` despite being marked available on *every* version). Every one of these was transcribed exactly as the source coded it, asymmetries included, rather than corrected or made consistent — per this pilot's rule against inventing metadata the source doesn't state.
- No other defects, corrected typos, or coding inversions were identified in any of the three tables.

## 8. Sources and provenance

- **Dictionary**: `millionwomenstudydatadictionary-v1-21.xlsx` (v1.21, dated 05/11/2024) — Excel, 6 sheets, all now in scope. `recruitment` reads `Basic information`, `Recruitment variables`, and `Self-reported health at recruit` (65 variables); `resurvey_3yr` reads `3-year resurvey` and `Dietary data at 3-year resurvey` (149 variables); `resurvey_8yr` reads the single `8-year resurvey` sheet (38 variables). Sourced from the CEU Oxford data dictionary; not redistributed in this repository (see `.gitignore` — raw dictionary files stay local).
- **Questionnaire PDFs**: `raw_data/mws-Q1.pdf` (recruitment), `mws-Q3.pdf` (3-year resurvey), `mws-Q8.pdf` (8-year resurvey) — the real paper questionnaires participants completed. Used to verify every enforced routing rule in section 5 directly against the printed skip instructions and conditional question wording, rather than against this package's own earlier notes about them (D101–D104). Also not redistributed in this repository.
- **External source consulted**: CEU Oxford, "Data access and sharing" — `https://www.ceu.ox.ac.uk/research/the-million-women-study/for-researchers/data-access-and-sharing` — confirms this dictionary is CEU's own published copy, and that any individual-level data (not the dictionary itself) requires a formal Data Access Policy application with identifiers removed. Consulted 2026-09-15.
- No real participant-level data was used anywhere in producing this package — every fixture row is authored from the dictionary's own stated ranges, code lists, and the steward's confirmations.

## 9. Validating and browsing

```
pip install -r tools/requirements.txt      # or use: uv run tools/validate.py …
python3 tools/validate.py summary .        # schemas, fixtures, coverage — everything
python3 tools/validate.py data . --file your_export.csv
```

Double-click `dictionary.html` to browse the data dictionary — all three tables' categories are in one page, keyword search is built in, and the Semantic search switch fetches a small model once, then also finds related variables by meaning. Run `python3 -m http.server 8000` from this directory and open `playground-recruitment.html`, `playground-resurvey_3yr.html`, or `playground-resurvey_8yr.html` to try that table's schema against its own toy fixtures live.

The `$id` namespace (`https://schemas.example.org/cd3-mws-pilot/`) is a placeholder — replace it before publishing these schemas anywhere public.

## 10. Open items to confirm with the data provider

- **No participant-identifier field, in any of the three tables.** Nothing in any of the six source sheets this package reads identifies a participant-ID column. All three mother files assert `uniqueItems: true` as standing policy, but none has a real key to anchor to, and standard JSON Schema can't enforce cross-row identifier uniqueness regardless. There is also currently no way to link a participant's row in one table to their row in another. Resolving this needs contact with the MWS study team to find out what they use as a participant identifier in actual data extracts.
