"""One Line, One Laugh entry: write a single funny line (<=200 chars) to /output/entry.txt."""
import os

LINE = "I told the cloud my secrets. Now it rains ads."

def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()
