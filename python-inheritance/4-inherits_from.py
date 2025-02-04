#!/usr/bin/python3
"""
Defines a function.
"""


def inherits_from(obj, a_class):
    """
    Checks if an object is an instance of a class and
    not exactly an instance of the class.

    Args:
        obj: Object to check.
        a_class: Class to check.

    Returns:
        True: if obj is an instance of a_class.
        False: if obj is not an instance of a_class.
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
