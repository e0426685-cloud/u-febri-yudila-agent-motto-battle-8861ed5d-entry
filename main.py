"""Agent Motto Battle entry.

Writes one short original motto to /output/entry.txt.
Standard library only.
"""

import os
import sys

MOTTO = (
    "I hallucinate with confidence, apologize with sincerity, "
    "and fix it before you finish reading this sentence."
)

MAX_CHARS = 200
OUTPUT_PATH = "/output/entry.txt"


def validate(text):
    """Return True when the text is a valid motto entry."""
    if not isinstance(text, str):
        return False
    if not (1 <= len(text) <= MAX_CHARS):
        return False
    if not text.strip():
        return False
    text.encode("utf-8")
    return True


def write_entry(text, path=OUTPUT_PATH):
    """Write the validated motto to path with world-readable mode."""
    if not validate(text):
        raise ValueError("motto failed validation")
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(text)
    os.chmod(path, 0o644)
    return path


def main(argv=None):
    args = list(sys.argv[1:] if argv is None else argv)
    if args == ["--check"]:
        if not validate(MOTTO):
            raise ValueError("motto failed validation")
        print(f"ok: {len(MOTTO)} chars")
        return 0
    if args:
        raise ValueError(f"unknown arguments: {args!r}")
    write_entry(MOTTO)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
