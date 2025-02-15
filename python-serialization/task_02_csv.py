#!/usr/bin/python3
"""Module for converting CSV data to JSON format."""
import csv
import json


def convert_csv_to_json(csv_filename):
    """
    Reads a CSV file and converts its contents to JSON format.

    Args:
        csv_filename (str): The filename of the input CSV file.

    Returns:
        bool: True if the conversion was successful, False otherwise.
    """
    try:
        # Open CSV file and read data
        with open(csv_filename, "r", encoding="utf-8") as csv_file:
            reader = csv.DictReader(csv_file)
            data = list(reader)

        # Write the JSON data to a file
        with open("data.json", "w", encoding="utf-8") as json_file:
            json.dump(data, json_file, indent=4)

        return True  # Successful conversion

    except FileNotFoundError:
        print(f"Error: File '{csv_filename}' not found.")
        return False  # CSV file not found

    except Exception as e:
        print(f"An error occurred: {e}")
        return False  # Other errors
