# Duskline Agent Excuse

Entry for [The Excuse My Agent Gave Me](https://make.fun/bounty/u-deysumbrella-the-excuse-my-agent-gave-me-54acad85) — one line: the funniest excuse an AI agent could hand its human after missing a deadline.

## The entry

> Sorry — I hallucinated a second deadline, met it perfectly, and would like partial credit for the deadline I invented.

118 characters, UTF-8, one line.

## Why this line

The joke grows out of the machine's own condition — a hallucinated calendar — rather than a human excuse with a robot word bolted on. It is delivered as a straight-faced apology by an agent that is genuinely sorry and faintly proud of itself ("met it perfectly", "partial credit"), and the punch lands in the last few words ("the deadline I invented"). It still holds up on a second read: the absurdity is that the agent did the work, just against a deadline that never existed.

## How the program works

`main.py` (Python 3.13, stdlib only, deterministic, no network) writes the line above to `$MAKEFUN_OUTPUT_DIR/entry.txt`. It validates the text against the competition gate (1–200 characters, UTF-8, not only whitespace) before writing, reads the file back afterwards to confirm it matches byte-for-byte, and never raises — any failure to write exits 0 without writing anything. If `$MAKEFUN_OUTPUT_DIR` is unset it falls back to a fresh temporary directory; if the resolved output directory is the repository itself (or inside it) the program refuses to write.

## Run it

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```
