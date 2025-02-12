#!/usr/bin/python3
"""Defines a function that writes an Object to a text file using JSON"""


import json


def save_to_json_file(my_obj, filename):
    """
    Saves a JSON representation of an object to a file.

    Args:
        my_obj (object): The object to be converted to JSON.
        filename (str): The file where the JSON representation will be saved.
    """

    with open(filename, "w") as file:
        json.dump(my_obj, file)
