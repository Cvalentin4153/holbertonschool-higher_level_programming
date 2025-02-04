#!/usr/bin/python3
"""Defines a function"""


def is_kind_of_class(obj, a_class):
    """
    Functions checks if obj is instance of a_class.
    Args:
        obj: Object given.
        a_class: Class to check.
    Returns:
        True: if is instance.
        False: if is not an instance.
    """
    if isinstance(obj, a_class):
        return True
    return False
