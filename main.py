"""Describe Your Ex in One Word — a single-word verdict.

The brief asks for exactly one word, at most 111 characters, that
describes an ex, with nothing else attached. The judge weighs, in
order: (1) instantly readable as a verdict on a former partner,
(2) comic punch through a twist or precise absurdity, not a plain
insult, (3) surprise that stays instantly clear, (4) craft: exactly
one word, spelled correctly, no punctuation tricks, (5) recognition
— anyone who has had an ex feels the truth in it.
"""

# Each candidate scored 0-5 per criterion, in the judge's own order.
# Criterion 1 is the gate, so it counts double in the total.
CANDIDATES = {
    "Blocked":   {"c1": 5, "c2": 2, "c3": 0, "c4": 5, "c5": 4},
    "Mistake":   {"c1": 5, "c2": 2, "c3": 0, "c4": 5, "c5": 4},
    "Overdraft": {"c1": 4, "c2": 4, "c3": 4, "c4": 5, "c5": 4},
    "Unstable":  {"c1": 4, "c2": 2, "c3": 1, "c4": 5, "c5": 3},
    "Expired":   {"c1": 5, "c2": 5, "c3": 4, "c4": 5, "c5": 5},
    "Trial":     {"c1": 3, "c2": 4, "c3": 4, "c4": 5, "c5": 3},
}


def total(scores):
    return 2 * scores["c1"] + scores["c2"] + scores["c3"] + scores["c4"] + scores["c5"]


# "Expired" wins: the whole relationship summed up as a date on a
# carton — it was fine once, it stayed too long, and now keeping it
# would only make you sick. A verdict at a glance, a twist instead
# of an insult, and a nod from anyone who has ever cleaned out the
# fridge after a breakup.
WINNER = max(CANDIDATES, key=lambda w: total(CANDIDATES[w]))

MAX_CHARS = 111


def check_word(word):
    """Refuse anything that is not one bare word inside the gate."""
    if not word or not word.strip():
        raise ValueError("entry is empty or only whitespace")
    if len(word) > MAX_CHARS:
        raise ValueError(f"entry is {len(word)} chars, over the {MAX_CHARS} cap")
    if len(word.split()) != 1:
        raise ValueError("entry must be a single word, nothing attached")


def emit():
    import os
    from pathlib import Path

    check_word(WINNER)
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    try:
        out_dir.mkdir(parents=True, exist_ok=True)
        target = out_dir / "entry.txt"
        target.write_text(WINNER, encoding="utf-8")
    except OSError:
        # Local run without a writable /output: fall back to ./output.
        target = Path("output") / "entry.txt"
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(WINNER, encoding="utf-8")
    print(f"wrote {WINNER!r} ({len(WINNER)} chars) to {target}")


if __name__ == "__main__":
    emit()
