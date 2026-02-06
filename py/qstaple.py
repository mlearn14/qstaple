#!/usr/bin/env python

import os
from pathlib import Path
import sys

from pypdf import PdfWriter


def main(dir):
    dir = Path(dir).expanduser()

    if not dir.is_dir():
        print(f"Directory {dir} does not exist")
        sys.exit(1)

    pdfs = sorted(dir.glob("*.pdf"))

    if not pdfs:
        print("No PDF files found.")
        return

    output = os.path.join(dir, "deployment_packet.pdf")

    if Path(output) in pdfs:
        print(
            f"Output file already exists. Delete {output} before proceding further. Exiting."
        )
        sys.exit(1)

    merger = PdfWriter()
    for pdf in pdfs:
        print(f"Adding {pdf.name}")
        merger.append(str(pdf))

    merger.write(output)
    merger.close()

    print(f"\nCreated: {output}")


if __name__ == "__main__":
    directory = input("Enter directory to staple PDFs from:\n> ").strip()
    main(directory)
    input("\nPress any key to close...")
