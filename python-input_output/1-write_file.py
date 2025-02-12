#!/usr/bin/python3
"""Defines a function that overwrites a file"""


def write_file(filename="", text=""):
    """
    Writes a string to a text file (UTF8)
    and returns the number of characters written:
    Args:
        filename (str): name of the file to write
        text (str): string to write to the file
    Returns:
        int: the number of characters written
    """

    with open(filename, 'w', encoding="utf-8") as file:
        return file.write(text)
