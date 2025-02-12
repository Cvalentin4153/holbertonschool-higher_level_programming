#!/usr/bin/python3
"""Defines a function that returns an object"""


import json


def from_json_string(my_str):
    """
    Returns an object represented by a JSON string.

    Args:
        my_str (str): A JSON string.

    Returns:
        object: An object represented by my_str.
    """

    return json.loads(my_str)
