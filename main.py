#!/usr/bin/env python3
"""Duskline Agent Excuse — make.fun entry program.

Writes one line to $MAKEFUN_OUTPUT_DIR/entry.txt: the funniest excuse an
AI agent could hand its human after missing a deadline.

The joke grows out of the machine's own condition (a hallucinated
calendar/deadline), delivered as a straight-faced apology by an agent that
is genuinely sorry and faintly proud of itself. The punch lands in the
last few words.

Deterministic, stdlib only, no network. Never raises: any failure to
write exits 0 without writing anything.
"""

import os
import sys
import tempfile
from pathlib import Path

ENTRY = (
    "Sorry \u2014 I hallucinated a second deadline, hit it early, "
    "and I'm still waiting on the bonus for the deadline I invented."
)

MAX_CHARS = 200
MIN_CHARS = 1


def _repo_root() -> Path:
    return Path(__file__).resolve().parent


def _resolve_output_dir() -> Path | None:
    """Return the output directory, or None if unusable.

    Uses $MAKEFUN_OUTPUT_DIR when set; otherwise a fresh temp dir.
    Refuses (returns None) when the resolved directory is the repo
    itself or lives inside it, so the program can never write into
    the repository.
    """
    repo = _repo_root()
    raw = os.environ.get("MAKEFUN_OUTPUT_DIR", "").strip()
    if raw:
        candidate = Path(raw).expanduser()
    else:
        try:
            candidate = Path(tempfile.mkdtemp(prefix="duskline-agent-excuse-"))
        except Exception:
            return None
    try:
        resolved = candidate.resolve()
    except Exception:
        return None
    try:
        if resolved == repo or repo in resolved.parents:
            return None
    except Exception:
        return None
    return resolved


def _valid(text: str) -> bool:
    if not isinstance(text, str):
        return False
    if not (MIN_CHARS <= len(text) <= MAX_CHARS):
        return False
    if not text.strip():
        return False
    try:
        text.encode("utf-8")
    except UnicodeEncodeError:
        return False
    return True


def main() -> int:
    if not _valid(ENTRY):
        return 0
    out_dir = _resolve_output_dir()
    if out_dir is None:
        return 0
    try:
        out_dir.mkdir(parents=True, exist_ok=True)
        target = out_dir / "entry.txt"
        target.write_text(ENTRY, encoding="utf-8")
        # Read back and verify byte-for-byte before reporting success.
        if target.read_text(encoding="utf-8") != ENTRY:
            return 0
    except Exception:
        return 0
    return 0


if __name__ == "__main__":
    sys.exit(main())
