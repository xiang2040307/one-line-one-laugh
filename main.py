"""One Line, One Laugh entry: write a single funny line (<=200 chars) to /output/entry.txt."""
import os

LINE = "I told the cloud my secrets. Now it rains ads."

# Sealed gate: the entry must be 1-200 UTF-8 characters, not only whitespace.
if not (1 <= len(LINE) <= 200 and LINE.strip()):
    raise SystemExit(f"entry line invalid: {len(LINE)} chars")

def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()
