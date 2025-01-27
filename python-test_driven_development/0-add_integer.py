#!/usr/bin/python3
"""
This module defines a function `add_integer`.
It adds two integers or floats, casting them to integers if necessary.
"""


def add_integer(a, b=98):
    """
    Adds two integers or floats, casting them to integers if necessary.

    Args:
        a (int or float): The first number to add. Must be an integer or float.
        b (int or float, optional): The second number to add. Defaults to 98.
            Must be an integer or float.

    Returns:
        int: The addition of `a` and `b`, after casting floats to integers.

    Raises:
        TypeError: If `a` or `b` is not an integer or float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)
    return a + b
