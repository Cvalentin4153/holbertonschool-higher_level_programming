#!/usr/bin/python3
"""Module for serializing and deserializing Python dictionaries using JSON."""
import json


def serialize_and_save_to_file(data, filename):
    """
    Serializes a Python dictionary and saves it to a JSON file.

    Args:
        data (dict): The Python dictionary to be serialized.
        filename (str): The filename of the output JSON file.

    Note:
        If the file already exists, it will be replaced.
    """
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)


def load_and_deserialize(filename):
    """
    Loads and deserializes JSON data from a file to a Python dictionary.

    Args:
        filename (str): The filename of the JSON file to be loaded.

    Returns:
        dict: A Python dictionary with the deserialized JSON data.
    """
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
