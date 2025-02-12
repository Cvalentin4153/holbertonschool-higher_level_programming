#!/usr/bin/python3
"""Defines a function that returns JSON representation of an object"""


import json


def to_json_string(my_obj):
    """
    Returns a string representation of a JSON object.

    Args:
        my_obj (str): A string to be encoded in JSON.

    Returns:
        str: A JSON encoded string.
    """

    return json.dumps(my_obj)
