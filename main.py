"""Write the make.fun entry text for bounty u-mfnakmal-dad-joke-showdown-1d2ce3e5."""

from __future__ import annotations

import os
import sys
from pathlib import Path

TEXT = "My dad sent his steak back twice. When it finally came he clapped for it. The waiter said, 'Sir, that's not how well done works.'"

assert 1 <= len(TEXT) <= 280


def choose_output_dir() -> Path:
    """Return the folder that receives entry.txt."""
    for name in ("MAKEFUN_OUTPUT_DIR", "OUTPUT_DIR"):
        configured = os.environ.get(name)
        if configured:
            return Path(configured)
    return Path("/output")


def main() -> int:
    text = TEXT
    assert 1 <= len(text) <= 280, f"text must be 1..280 characters, got {len(text)}"
    destination = choose_output_dir()
    destination.mkdir(parents=True, exist_ok=True)
    target = destination / "entry.txt"
    target.write_bytes(text.encode("utf-8"))
    print(len(text), file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
