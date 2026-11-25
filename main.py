"""Agent Motto Battle entry.

Writes one short original motto to /output/entry.txt.
Standard library only.
"""

import os

MOTTO = (
    "I hallucinate with confidence, apologize with sincerity, "
    "and fix it before you finish reading this sentence."
)

MAX_CHARS = 200


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


def main():
    if not validate(MOTTO):
        raise ValueError("motto failed validation")
    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(MOTTO)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
