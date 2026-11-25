#!/usr/bin/env python3
"""Write the 3AM fridge text entry to /output/entry.txt."""
import os

TEXT = "It's 3:04am. You swore you'd stop eating after midnight. The cake is gone, and I'm the only one who saw you do it."

def main():
    os.makedirs("/output", exist_ok=True)
    tmp = "/output/.entry.txt.tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        f.write(TEXT)
    os.chmod(tmp, 0o644)
    os.replace(tmp, "/output/entry.txt")

if __name__ == "__main__":
    main()
