"""How Many Tabs Do You Have Open? — entry program.

Writes one number, digits only (1-5 chars), to /output/entry.txt: the
honest count of open browser tabs. Stdlib only, deterministic.
"""
import os

TEXT = "137"


def main():
    # Enforce the scorer's gate (RULES.txt): UTF-8, 1-5 chars, digits
    # only, not whitespace-only. Fail loudly instead of writing an
    # invalid entry. A leading zero would still pass isdigit but is not
    # a canonical count, and a count of zero tabs is not a lived-in
    # answer, so both are rejected here.
    if (
        not 1 <= len(TEXT) <= 5
        or not TEXT.isdigit()
        or (len(TEXT) > 1 and TEXT.startswith("0"))
        or int(TEXT) <= 0
    ):
        raise SystemExit("entry text violates the digits-only 1-5 char gate")
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(TEXT)
    # Write-verify: read the file back and refuse to exit cleanly if
    # the bytes on disk differ from the gated text.
    with open(out_path, "r", encoding="utf-8") as f:
        if f.read() != TEXT:
            raise SystemExit("entry.txt on disk does not match the gated text")


if __name__ == "__main__":
    main()
