#!/usr/bin/env python3
"""Produce an evidence-first PR review report from a unified diff.

This is intentionally deterministic: it gives Switch review agents auditable signals
to discuss, rather than pretending an LLM test result is evidence.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path


def finding(identifier: str, severity: str, evidence: str, action: str) -> dict[str, str]:
    return {"id": identifier, "severity": severity, "evidence": evidence, "recommended_action": action}


def review(diff: str) -> dict[str, object]:
    added = [line[1:] for line in diff.splitlines() if line.startswith("+") and not line.startswith("+++")]
    joined = "\n".join(added).lower()
    findings: list[dict[str, str]] = []

    if any(token in joined for token in ("/admin", "is_admin", "admin=")):
        findings.append(finding(
            "AUTH-REVIEW",
            "HIGH",
            "The change adds or alters an admin-sensitive path or flag.",
            "Add an authorization regression test and document the intended access policy.",
        ))
    if any(token in joined for token in ("password=", "api_key=", "secret=", "token=")):
        findings.append(finding(
            "SECRET-SCAN",
            "BLOCKER",
            "A line resembles a hard-coded credential or token.",
            "Remove the value, rotate it if real, and load it from a secret manager or environment variable.",
        ))
    if "test" not in diff.lower():
        findings.append(finding(
            "TEST-COVERAGE",
            "MEDIUM",
            "No test file or test assertion appears in the supplied diff.",
            "Add a targeted regression test for the changed behavior.",
        ))

    return {
        "added_lines": len(added),
        "findings": findings,
        "recommendation": "HOLD" if any(item["severity"] in {"BLOCKER", "HIGH"} for item in findings) else "REVIEW-READY",
        "note": "This report is a review aid. A human release owner makes the final decision.",
    }


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: python scripts/review_pr.py <unified-diff>", file=sys.stderr)
        return 2
    path = Path(sys.argv[1])
    if not path.is_file():
        print(f"Diff not found: {path}", file=sys.stderr)
        return 2
    print(json.dumps(review(path.read_text(encoding="utf-8")), indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
