"""Check the upload folders before uploading them (no network, nothing is changed).

For every cohort folder next to this script it checks that
  1. every JSON file parses and has a unique $id (within the folder and across all the folders, because the explorer loads them together);
  2. the root schema <COHORT>_all_tables.schema.json is valid JSON Schema (draft 2020-12);
  3. every $ref reachable from the root resolves to a file inside the same folder (an empty record is run through the root to force this);
  4. the root is the only array-of-records schema that nothing else references, so the cohort loads as exactly ONE dataset.
It prints the numbers used in README.md.   Needs:  pip install jsonschema referencing"""
import json, sys
from pathlib import Path
from jsonschema import Draft202012Validator
from referencing import Registry, Resource
from referencing.jsonschema import DRAFT202012

HERE = Path(__file__).resolve().parent
cohorts = sorted(p.name for p in HERE.iterdir() if p.is_dir() and (p / f"{p.name}_all_tables.schema.json").exists())
all_ids, problems, summary = {}, [], []

for c in cohorts:
    folder = HERE / c
    docs = {}
    for f in sorted(folder.rglob("*.json")):
        d = json.loads(f.read_text(encoding="utf-8"))
        i = d.get("$id")
        if not i:
            problems.append(f"{c}: {f.relative_to(HERE)} has no $id")
            continue
        if i in docs:
            problems.append(f"{c}: duplicate $id {i}")
        if i in all_ids and all_ids[i] != c:
            problems.append(f"{c}: $id {i} is also used by {all_ids[i]}")
        docs[i] = d
        all_ids[i] = c
    registry = Registry().with_resources((i, Resource.from_contents(d, default_specification=DRAFT202012)) for i, d in docs.items())
    root = json.loads((folder / f"{c}_all_tables.schema.json").read_text(encoding="utf-8"))
    Draft202012Validator.check_schema(root)
    try:
        list(Draft202012Validator(root, registry=registry).iter_errors([{}]))   # walks every $ref
    except Exception as e:                                                       # an unresolvable $ref raises here
        problems.append(f"{c}: a $ref does not resolve: {type(e).__name__}: {str(e)[:160]}")
    # which schemas are array-of-records and not referenced by any other schema?
    referenced = {Path(r["$ref"]).name for r in root["items"]["allOf"]}
    arrays = [i for i, d in docs.items() if d.get("type") == "array" and not any(i.endswith("/" + n) for n in referenced)]
    if len(arrays) != 1:
        problems.append(f"{c}: {len(arrays)} unreferenced array schemas (should be 1): {arrays}")
    cats = [d for i, d in docs.items() if "properties" in d]
    props = sum(len(d["properties"]) for d in cats)
    tables = sorted({r["$ref"].split("/")[0] for r in root["items"]["allOf"]})
    summary.append((c, len(tables), len(root["items"]["allOf"]), props))

print("%-10s %7s %16s %11s" % ("cohort", "tables", "category files", "variables"))
for s in summary:
    print("%-10s %7d %16d %11d" % s)
print("datasets if every folder is loaded:", len(summary), "(the explorer allows 16)")
if problems:
    print("\nPROBLEMS:")
    for p in problems:
        print(" -", p)
    sys.exit(1)
print("\nAll checks passed.")
