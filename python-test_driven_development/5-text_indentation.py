#!/usr/bin/python3
"""
This module defines a function `text_indentation`.
It adds two new lines after each of these characters: '.', '?', ':'.
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each '.', '?', or ':'.

    Args:
        text (str): The input text to format.

    Raises:
        TypeError: If `text` is not a string.

    Examples:
        >>> text_indentation("Hello. How are you?")
        Hello.
        <BLANKLINE>
        <BLANKLINE>
        How are you?
        <BLANKLINE>
        <BLANKLINE>
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    # Remove extra spaces and ensure proper output formatting
    i = 0
    while i < len(text):
        print(text[i], end="")
        if text[i] in ".?:":
            print("\n")
            print()
            # Skip consecutive spaces after punctuation
            while i + 1 < len(text) and text[i + 1] == " ":
                i += 1
        i += 1
