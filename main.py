"""Make the Judge Smile: one warm, surprising line about a small good
thing that happened today.

The line: a neighbour's cat steals a slipper in the morning, then
returns it with a leaf on top — a tiny kindness with a joke in it.
Warmth (the cat's gift), surprise (a leaf, offered like rent), one
concrete detail (the slipper), fresh wording, no greeting-card phrasing.
"""

import os

LINE = "My neighbour's cat stole my slipper this morning, then brought it back with a leaf on top, like rent."


def output_path():
    if os.environ.get("ENTRY_OUTPUT"):
        return os.environ["ENTRY_OUTPUT"]
    for key in ("OUTPUT_DIR", "MAKEFUN_OUTPUT_DIR"):
        if os.environ.get(key):
            return os.path.join(os.environ[key], "entry.txt")
    return "/output/entry.txt"


def main():
    # Gate: 1-200 characters, a single line, not only whitespace.
    line = LINE.strip()
    assert 1 <= len(line) <= 200, "line must be 1-200 chars, got %d" % len(line)
    assert "\n" not in line and "\r" not in line, "line must be a single line"
    assert line.strip(), "line must not be only whitespace"
    path = output_path()
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(line)
    os.chmod(path, 0o644)
    with open(path, "rb") as f:
        written = f.read()
    assert written == line.encode("utf-8"), "output bytes must match the line"
    # Re-read as text and re-apply the gate to what is actually on disk,
    # so a write quirk (newline, encoding) cannot slip past the check.
    with open(path, "r", encoding="utf-8") as f:
        on_disk = f.read()
    assert on_disk == line, "re-read line must equal the intended line"
    assert 1 <= len(on_disk) <= 200, "on-disk line must be 1-200 chars"
    assert "\n" not in on_disk and "\r" not in on_disk, "on-disk must be one line"
    print("Wrote %d chars to %s: %s" % (len(line), path, line))


if __name__ == "__main__":
    main()
