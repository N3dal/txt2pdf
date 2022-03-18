#!/usr/bin/python3
# -----------------------------------------------------------------
# simple script for edit and creating pdf files.
# and converting txt files to pdf files.
#
#
#
# Author:N84.
#
# Create Date:Fri Mar 18 11:28:38 2022.
# ///
# ///
# ///
# -----------------------------------------------------------------

from os import system
from os import name as os_name
from fpdf import FPDF


def clear():
    """wipe the terminal screen."""

    if os_name == "posix":
        # *nix machines.
        system("clear")

    else:
        # windows machines.
        system("cls")


clear()


def txt2pdf(file_path: str = None):
    """convert any text  => *.txt, to pdf"""

    if file_path is None:
        raise Exception("FilePathError: please enter the file path.")

    with open(file_path, "r") as file:
        text_lines = file.readlines()

    # create pdf object.
    pdf = FPDF()

    pdf.add_page()

    pdf.set_font("Arial", size=12)

    for index, line in enumerate(text_lines):
        pdf.cell(100, 10, txt=line, ln=1, align="C")

    # help(pdf.cell)

    pdf.output("./test.pdf")

    pdf.close()


def main():
    txt2pdf("./test.txt")


if __name__ == '__main__':
    main()
