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

    # Replace occurrences of '.', '?', and ':' followed by any spaces
    # with the punctuation, two new lines, and no trailing spaces
    result = ""
    i = 0

    while i < len(text):
        result += text[i]
        if text[i] in ".?:":
            result += "\n\n"
            i += 1
            while i < len(text) and text[i] == " ":
                i += 1
            continue
        i += 1

    # Print the resulting string without extra trailing spaces
    print(result.strip())
