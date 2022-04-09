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
from sys import argv


def clear():
    """wipe the terminal screen."""

    if os_name == "posix":
        # *nix machines.
        system("clear")

    else:
        # windows machines.
        system("cls")


clear()


def get_args():
    """return all the arguments that pass,
    to the program except the program name."""

    return argv[1:]


def separate2lines(string: str, max_char: int = 64):
    """separate a string into multi line string, with max_length of line,
    equal to max_char.
    we will use this function to align pdf lines."""

    # first make sure to remove all linefeeds.
    text = string.replace("\n", "")

    lines = []
    temp_string, counter = "", 0

    for char in text:

        if counter == max_char-1:
            lines.append(temp_string + char + "\n")
            temp_string = ""
            counter = 0
            continue

        temp_string += char
        counter += 1

    return lines


def txt2pdf(file_path: str = None):
    """convert any text  => *.txt, to pdf"""

    if file_path is None:
        raise Exception("FilePathError: please enter the file path.")

    with open(file_path, "r") as file:
        text = file.read()

    # create pdf object.
    pdf = FPDF()

    pdf.add_page()

    pdf.set_font("Arial", size=12)

    text_lines = separate2lines(text, 90)
    # print(text_lines)

    for index, line in enumerate(text_lines):
        pdf.cell(0, 10, txt=line, ln=1, align="L")

    pdf.output("./test.pdf")

    pdf.close()


def main():
    txt2pdf("./test.txt")


if __name__ == '__main__':
    main()
