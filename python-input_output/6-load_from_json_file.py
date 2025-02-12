#!/usr/bin/python3
"""Defines a function that creates an object from JSON file"""


import json


def load_from_json_file(filename):
    """
    Creates an object from a JSON file.

    Args:
        filename (str): The name of the JSON file.

    Returns:
        object: The Python object parsed from the JSON file.
    """

    with open(filename) as file:
        return json.load(file)
