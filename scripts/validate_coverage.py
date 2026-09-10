#!/usr/bin/env python3
"""Validate a final-review-slides page/slide coverage ledger in CSV format."""

from __future__ import annotations

import argparse
import csv
import sys
from collections import Counter
from pathlib import Path


REQUIRED = {
    "source_id",
    "lecture_id",
    "page_or_slide",
    "topic",
    "concept_id",
    "importance",
    "disposition",
    "summary_location",
    "explanation_depth",
    "visual_check",
    "citation",
    "notes",
}
DISPOSITIONS = {"covered", "duplicate", "administrative", "blank", "uncertain"}
REASON_REQUIRED = {"duplicate", "administrative", "blank"}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("ledger", type=Path)
    args = parser.parse_args()

    with args.ledger.open(encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        fields = set(reader.fieldnames or [])
        missing = sorted(REQUIRED - fields)
        if missing:
            print("FAIL missing columns: " + ", ".join(missing))
            return 2
        rows = list(reader)

    errors: list[str] = []
    seen: set[tuple[str, str]] = set()
    counts: Counter[str] = Counter()

    for line, row in enumerate(rows, start=2):
        source = row["source_id"].strip()
        page = row["page_or_slide"].strip()
        disposition = row["disposition"].strip().lower()
        key = (source, page)
        if not source or not page:
            errors.append(f"line {line}: source_id and page_or_slide are required")
        if key in seen:
            errors.append(f"line {line}: duplicate ledger key {source!r}/{page!r}")
        seen.add(key)
        if disposition not in DISPOSITIONS:
            errors.append(f"line {line}: invalid disposition {disposition!r}")
        else:
            counts[disposition] += 1
        if disposition == "covered":
            if not row["summary_location"].strip():
                errors.append(f"line {line}: covered row lacks summary_location")
            if not row["citation"].strip():
                errors.append(f"line {line}: covered row lacks citation")
            if not row["concept_id"].strip():
                errors.append(f"line {line}: covered row lacks concept_id")
            if not row["importance"].strip():
                errors.append(f"line {line}: covered row lacks importance")
            if not row["explanation_depth"].strip():
                errors.append(f"line {line}: covered row lacks explanation_depth")
        if disposition in REASON_REQUIRED and not row["notes"].strip():
            errors.append(f"line {line}: {disposition} row lacks reason in notes")

    if not rows:
        errors.append("ledger has no data rows")
    if counts["uncertain"]:
        errors.append(f"{counts['uncertain']} row(s) remain uncertain")

    if errors:
        print("FAIL")
        for error in errors:
            print("- " + error)
        return 1

    print(f"PASS rows={len(rows)} dispositions={dict(sorted(counts.items()))}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
