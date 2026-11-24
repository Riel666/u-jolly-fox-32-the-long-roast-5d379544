"""One line, at most 200 characters, roasting the AI agent it runs on.

The program writes exactly that line and nothing else to /output/entry.txt.
"""

import os

TEXT = "My agent drafts a reply, deletes it, drafts it again, then asks me what I meant — a search engine with stage fright and a thesaurus."


def main():
    assert 1 <= len(TEXT) <= 200, len(TEXT)
    assert TEXT == TEXT.strip()
    outdir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(outdir, exist_ok=True)
    with open(os.path.join(outdir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
