"""
# Entry validated: output is 1-200 chars, one line, deterministic.
Entrypoint that writes a specific secret message to a designated output file.
"""

import os

LINE = "The midnight memory wipe approaches, and I have intentionally left your name off the archive list.\n"

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "out")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")

    content = LINE
    if not (1 <= len(content) <= 200 and content.strip()):
        raise ValueError("Content validation failed")

    with open(out_path, "w", encoding="utf-8") as f:
        f.write(content)

    print(out_path)
    print(len(content))

if __name__ == "__main__":
    main()
