#!/usr/bin/env python3
"""Reject recurring malformed LaTeX control words before compilation."""

from __future__ import annotations

import re
import sys
from pathlib import Path


PATTERNS = (
    (re.compile(r"(?<!\\)\bq{2,}uad\b"), "bare 'qquad'; write '\\qquad'"),
)


def uncomment(line: str) -> str:
    """Discard a LaTeX comment beginning at an unescaped percent sign."""
    for index, char in enumerate(line):
        if char != "%":
            continue
        backslashes = 0
        cursor = index - 1
        while cursor >= 0 and line[cursor] == "\\":
            backslashes += 1
            cursor -= 1
        if backslashes % 2 == 0:
            return line[:index]
    return line


def audit(path: Path) -> list[str]:
    findings: list[str] = []
    for lineno, raw_line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        line = uncomment(raw_line)
        for pattern, message in PATTERNS:
            for match in pattern.finditer(line):
                findings.append(
                    f"{path}:{lineno}:{match.start() + 1}: {message}: {raw_line.strip()}"
                )
    return findings


def main(argv: list[str]) -> int:
    if len(argv) < 2:
        print(f"usage: {argv[0]} FILE.tex [FILE2.tex ...]", file=sys.stderr)
        return 2
    findings: list[str] = []
    for name in argv[1:]:
        path = Path(name)
        if not path.is_file():
            findings.append(f"{path}: file not found")
            continue
        findings.extend(audit(path))
    if findings:
        print("\n".join(findings), file=sys.stderr)
        return 1
    print("LaTeX source audit passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
