#!/usr/bin/python3
"""
This module defines a function `say_my_name`.
It prints a formatted string with the first and last name.
"""


def say_my_name(first_name, last_name=""):
    """
    Prints 'My name is <first_name> <last_name>'.

    Args:
        first_name (str): The first name. Must be a string.
        last_name (str, optional): The last name. Must be a string.
        Defaults to "".

    Raises:
        TypeError: If `first_name` or `last_name` is not a string.

    Examples:
        >>> say_my_name("John", "Smith")
        My name is John Smith
        >>> say_my_name("Bob")
        My name is Bob
        >>> say_my_name("Alice", "")
        My name is Alice
        >>> say_my_name("", "")
        My name is 
        >>> say_my_name(12, "Smith")
        Traceback (most recent call last):
            ...
        TypeError: first_name must be a string
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    # Print without adding extra spaces for empty strings
    print("My name is {}{}".format(first_name,
         f" {last_name}" if last_name else ""))
