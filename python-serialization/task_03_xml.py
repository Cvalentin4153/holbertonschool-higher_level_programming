#!/usr/bin/python3
"""Module for serializing and deserializing
Python dictionaries using XML."""
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Serializes a Python dictionary into
    XML format and saves it to a file.

    Args:
        dictionary (dict): The dictionary to serialize.
        filename (str): The filename to save the XML data.

    Returns:
        bool: True if serialization was successful, False otherwise.
    """
    try:
        # Create root element
        root = ET.Element("data")

        # Convert dictionary to XML elements
        for key, value in dictionary.items():
            child = ET.SubElement(root, key)
            child.text = str(value)  # Convert all values to string

        # Create an XML tree and write to file
        tree = ET.ElementTree(root)
        tree.write(filename, encoding="utf-8", xml_declaration=True)

        return True  # Successful serialization

    except Exception as e:
        print(f"Error during XML serialization: {e}")
        return False


def deserialize_from_xml(filename):
    """
    Deserializes XML data from a file into a Python dictionary.

    Args:
        filename (str): The XML file to read.

    Returns:
        dict: A Python dictionary representing the XML data.
    """
    try:
        # Parse XML file
        tree = ET.parse(filename)
        root = tree.getroot()

        # Convert XML elements back into a dictionary
        return {child.tag: child.text for child in root}

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return None

    except ET.ParseError:
        print(f"Error: Failed to parse XML from '{filename}'.")
        return None
