"""
Exporter module to produce dataset.json, dataset.csv, sample_audit.json,
and patterns_summary.json for Composio Product Ops Reviewers.
"""

import json
import csv
import os
from typing import Dict, Any
from assignment.agent.dataset_builder import FULL_APPS_DATA, SAMPLE_AUDIT_20
from assignment.agent.analyzer import analyze_patterns
from assignment.agent.verifier import run_full_verification


def export_all_artifacts(output_dir: str = "assignment/data") -> Dict[str, str]:
    os.makedirs(output_dir, exist_ok=True)
    paths = {}

    # 1. Master dataset.json
    dataset_json_path = os.path.join(output_dir, "dataset.json")
    with open(dataset_json_path, "w", encoding="utf-8") as f:
        json.dump(FULL_APPS_DATA, f, indent=2, ensure_ascii=False)
    paths["dataset_json"] = dataset_json_path

    # 2. Master dataset.csv
    dataset_csv_path = os.path.join(output_dir, "dataset.csv")
    csv_fields = [
        "id", "name", "category", "website_hint", "one_liner",
        "auth_methods", "primary_auth", "access_model", "access_details",
        "api_surface", "api_breadth", "mcp_status", "buildability_verdict",
        "main_blocker", "priority_quadrant", "evidence_url"
    ]
    with open(dataset_csv_path, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=csv_fields, extrasaction="ignore")
        writer.writeheader()
        for app in FULL_APPS_DATA:
            row = dict(app)
            # Join lists into comma strings for CSV
            if isinstance(row.get("auth_methods"), list):
                row["auth_methods"] = "; ".join(row["auth_methods"])
            writer.writerow(row)
    paths["dataset_csv"] = dataset_csv_path

    # 3. Stratified Sample Audit sample_audit.json
    audit_json_path = os.path.join(output_dir, "sample_audit.json")
    with open(audit_json_path, "w", encoding="utf-8") as f:
        json.dump(SAMPLE_AUDIT_20, f, indent=2, ensure_ascii=False)
    paths["sample_audit"] = audit_json_path

    # 4. Patterns Summary patterns_summary.json
    patterns = analyze_patterns(FULL_APPS_DATA)
    verification_report = run_full_verification()
    patterns["verification_report"] = verification_report

    patterns_json_path = os.path.join(output_dir, "patterns_summary.json")
    with open(patterns_json_path, "w", encoding="utf-8") as f:
        json.dump(patterns, f, indent=2, ensure_ascii=False)
    paths["patterns_summary"] = patterns_json_path

    print("All data artifacts successfully exported:")
    for k, v in paths.items():
        print(f"  - {k}: {v} ({os.path.getsize(v)} bytes)")

    return paths


if __name__ == "__main__":
    export_all_artifacts()
