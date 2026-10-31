#!/usr/bin/env python3
"""Check a Humanizar rewrite against one test case in evals/cases.json.

Usage: python3 scripts/check-eval.py CASE_ID REWRITE_FILE
List the cases: python3 scripts/check-eval.py --list
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
CASES = json.loads((ROOT / "evals" / "cases.json").read_text(encoding="utf-8"))


def contains(text: str, phrase: str) -> bool:
    """Match whole words, so "tela" does not match inside "cautela"."""
    pattern = re.escape(phrase.casefold())
    if phrase[:1].isalnum():
        pattern = r"(?<!\w)" + pattern
    if phrase[-1:].isalnum():
        pattern += r"(?!\w)"
    return re.search(pattern, text.casefold()) is not None


def main(arguments: list[str]) -> int:
    if arguments == ["--list"]:
        for case in CASES:
            print(f"{case['id']} ({case['lang']}): {case['notes']}")
        return 0
    if len(arguments) != 2:
        print(__doc__.strip())
        return 2

    case_id, rewrite_path = arguments
    case = next((case for case in CASES if case["id"] == case_id), None)
    if case is None:
        print(f"No case named {case_id}. Run with --list to see the cases.")
        return 2

    rewrite = Path(rewrite_path).read_text(encoding="utf-8")
    problems = [
        f"Still contains: {phrase!r}"
        for phrase in case["must_not_contain"]
        if contains(rewrite, phrase)
    ]
    problems += [
        f"Lost: {phrase!r}"
        for phrase in case["must_keep"]
        if not contains(rewrite, phrase)
    ]

    for problem in problems:
        print(problem)
    print(f"{case_id}: {'fail' if problems else 'pass'}")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
