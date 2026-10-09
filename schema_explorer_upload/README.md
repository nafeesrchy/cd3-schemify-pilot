# Schema explorer upload folders

This folder holds the CD3 cohort schemas in the form the [schema explorer](https://jeyabbalas.github.io/schema-explorer/) can load: one folder per cohort (OFH, UKB, INTERVAL, COMPARE, MWS), each of which appears in the explorer as a single dataset.

## How to upload

1. Open <https://jeyabbalas.github.io/schema-explorer/>.
2. Click **Choose folder** (or drag a folder onto the page) and select one cohort folder, for example `OFH`.
3. Repeat for each of the other cohort folders. The cohorts then sit side by side in the explorer, one dataset each, five in total.

Load the whole cohort folder, not individual files. The category files refer to each other and to `common/defs.json` by relative path, and the paths only resolve when the folder is loaded as it is.

## Why this folder exists

The explorer turns every array-of-records schema that no other schema refers to into a dataset, and it stops at 16 datasets (it then skips the rest and says "Dataset limit (16) reached"). A schemify package has one such schema per table, so loading the packages directly would give 43 datasets: OFH alone has 21 tables, UKB 7, INTERVAL 6, COMPARE 6 and MWS 3. That is over the limit, and it spreads each cohort over many cards, when the explorer is meant for comparing data dictionaries across cohorts.

Each cohort folder therefore contains one extra file, `<COHORT>_all_tables.schema.json`. It lists every category file of every table of that cohort, so the cohort loads as one dataset and all its variables can be searched together.

## What is in each cohort folder

| Cohort | Tables | Category files | Variables |
| --- | --- | --- | --- |
| OFH | 21 | 26 | 834 |
| UKB | 7 | 50 | 4,454 |
| INTERVAL | 6 | 29 | 855 |
| COMPARE | 6 | 19 | 354 |
| MWS | 3 | 27 | 252 |

- `<COHORT>_all_tables.schema.json`: the one generated file, the root that makes the cohort one dataset.
- `common/defs.json` and `<table>/categories/*.json`: exact copies of the files in `<COHORT>/json_schema`, byte for byte and at the same relative paths, so every `$ref` and `$id` still resolves. Nothing in them has been edited.
- UKB repeats its participant-key category in every table; the bundle shows it once, which is why UKB has 4,454 variables here and 4,460 in the package.

## What it is not

It is a browsing view, not a validation schema. The tables of a cohort have different row types (a death record, a clinic measurement and a questionnaire are different kinds of row), and the bundle shows them side by side as sections of one record. To validate data, use each package's own schemas with its `tools/validate.py`. Each cohort also keeps its own missing-value conventions, and the explorer shows them as the package defines them.

## Rebuilding and checking

When a package changes, rebuild the folders and check them:

```
python build_bundles.py            # all five cohorts, or name some: python build_bundles.py OFH MWS
python verify_bundles.py           # needs: pip install jsonschema referencing
```

- `build_bundles.py` reads `<COHORT>/json_schema` from the folder above this one and rewrites the cohort folders here. It never changes a package.
- `verify_bundles.py` checks that every file has a unique `$id` (across all cohorts, because the explorer loads them together), that the root is valid JSON Schema, that every `$ref` resolves, and that each cohort loads as exactly one dataset. It also prints the numbers in the table above.

Built on 2026-10-09 from the packages as they stand: OFH limited to the data CD3 has requested (21 tables), MWS following the review rule that the schemas contain only what the source states, and UKB split into seven tables.
