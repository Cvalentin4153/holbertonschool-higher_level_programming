#!/usr/bin/python3
"""
This module defines a function `print_square`.
It prints a square with the character `#`.
"""


def print_square(size):
    """
    Prints a square with the character `#`.

    Args:
        size (int): The size length of the square.

    Raises:
        TypeError: If `size` is not an integer.
        ValueError: If `size` is less than 0.

    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")

    for _ in range(size):
        print("#" * size)
