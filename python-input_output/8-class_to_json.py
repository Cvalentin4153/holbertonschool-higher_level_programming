#!/usr/bin/python3
"""
    class_to_json function
"""


def class_to_json(obj):
    """
    Converts an object to a JSON-serializable dictionary.

    Args:
        obj: The object instance to convert.

    Returns:
        A dictionary representation of the object's attributes.
    """

    return obj.__dict__
