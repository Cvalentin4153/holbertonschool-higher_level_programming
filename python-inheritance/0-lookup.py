#!/usr/bin/python3
"""
Defines a function named lookup.
"""


def lookup(obj):
    """
    Returns the list of available attributes and methods of an object.
    Args:
        obj: object
    Returns:
        list
    """
    return dir(obj)
