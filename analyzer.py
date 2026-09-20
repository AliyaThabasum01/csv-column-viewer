import csv
import os


def analyze_csv(filename):
    if not os.path.isfile(filename):
        return None

    with open(filename, "r", encoding="utf-8", newline="") as file:
        reader = csv.DictReader(file)
        rows = list(reader)

    return {
        "rows": len(rows),
        "columns": len(reader.fieldnames or []),
        "names": reader.fieldnames or [],
        "sample": rows[:3]
    }
