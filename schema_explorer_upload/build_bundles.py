"""Build the schema explorer upload folders: one folder per cohort, each loading as ONE dataset.

Why: the schema explorer (https://jeyabbalas.github.io/schema-explorer/) turns every array-of-records schema that no other schema
references into a dataset, and it stops at 16 datasets. A schemify package has one such schema per table (OFH alone has 21), so the
packages cannot be uploaded as they are. This script writes, for each cohort, one extra root schema that lists every category file of
every table, so the cohort appears as a single dataset.

Usage (from anywhere):  python build_bundles.py [COHORT ...]        default: OFH UKB INTERVAL COMPARE MWS
Reads  <repo root>/<COHORT>/json_schema   (read-only; this script never changes a package)
Writes <this folder>/<COHORT>/             (deleted and rebuilt each run)

The category files and common/defs.json are copied byte for byte, at the same relative paths, so every $ref and $id still resolves.
Only the root file <COHORT>_all_tables.schema.json is generated. The bundle is a browsing view, not a validation schema: the tables
have different row types and are shown side by side as sections of one record."""
import json, shutil, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
PKGS = HERE.parent                      # the repository root, which holds <COHORT>/json_schema
COHORTS = sys.argv[1:] or ["OFH", "UKB", "INTERVAL", "COMPARE", "MWS"]


def tables_of(pkg):
    """Tables in the package's own reading order (manifest.json), then any others alphabetically."""
    man = pkg / "manifest.json"
    names = json.loads(man.read_text(encoding="utf-8")).get("tables") if man.exists() else None
    found = sorted(p.parent.name for p in pkg.glob("*/*.schema.json"))
    return [n for n in names if n in found] + [n for n in found if n not in names] if names else found


report = {}
for cohort in COHORTS:
    pkg = PKGS / cohort / "json_schema"
    dest = HERE / cohort
    if dest.exists():
        shutil.rmtree(dest)
    dest.mkdir(parents=True)
    (dest / "common").mkdir()
    shutil.copy2(pkg / "common" / "defs.json", dest / "common" / "defs.json")
    refs, seen_ident, base = [], False, None
    for table in tables_of(pkg):
        mother = json.loads((pkg / table / f"{table}.schema.json").read_text(encoding="utf-8"))
        order = [Path(x["$ref"]).stem for x in mother["items"]["allOf"] if "$ref" in x]
        (dest / table / "categories").mkdir(parents=True)
        for name in order:
            src = pkg / table / "categories" / f"{name}.json"
            if name == "identification":
                if seen_ident:        # the same participant key is repeated in every table; show it once
                    continue
                seen_ident = True
            shutil.copy2(src, dest / table / "categories" / f"{name}.json")
            refs.append({"$ref": f"{table}/categories/{name}.json"})
            if base is None:
                cid = json.loads(src.read_text(encoding="utf-8")).get("$id", "")
                base = cid.rsplit(f"/{table}/categories/", 1)[0] if f"/{table}/categories/" in cid else "https://schemas.example.org/explorer"
    root = {
        "$schema": "https://json-schema.org/draft/2020-12/schema",
        "$id": f"{base}/{cohort}_all_tables.schema.json",
        "title": f"{cohort}: all tables (explorer view)",
        "description": (f"Generated browsing view of the {cohort} schemify package: every table's categories side by side in one record, "
                        "so the cohort appears as one dataset in the schema explorer. Not for validating data: the tables have different row types "
                        "(see the package's own schemas)."),
        "type": "array",
        "minItems": 1,
        "items": {"type": "object", "title": f"{cohort} record (all tables)", "allOf": refs},
    }
    (dest / f"{cohort}_all_tables.schema.json").write_text(json.dumps(root, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    report[cohort] = {"tables": len(tables_of(pkg)), "category files": len(refs)}
print(json.dumps(report, indent=1))
