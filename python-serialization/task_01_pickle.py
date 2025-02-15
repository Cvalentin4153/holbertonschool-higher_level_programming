#!/usr/bin/python3
"""Module for serializing and deserializing custom
Python objects using pickle."""
import pickle


class CustomObject:
    """
    A custom class to demonstrate serialization and deserialization.

    Attributes:
        name (str): The name of the person.
        age (int): The age of the person.
        is_student (bool): Whether the person is a student.
    """

    def __init__(self, name, age, is_student):
        """
        Initializes a CustomObject instance.

        Args:
            name (str): The name of the person.
            age (int): The age of the person.
            is_student (bool): Whether the person is a student.
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Prints object attributes in a structured format."""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """
        Serializes the current instance and saves it to a file.

        Args:
            filename (str): The filename to save the object.
        """
        try:
            with open(filename, "wb") as f:
                pickle.dump(self, f)
        except Exception as e:
            print(f"Error serializing object: {e}")

    @classmethod
    def deserialize(cls, filename):
        """
        Deserializes an object from a file.

        Args:
            filename (str): The filename to load the object from.

        Returns:
            CustomObject: The loaded object, or None if an error occurs.
        """
        try:
            with open(filename, "rb") as f:
                return pickle.load(f)
        except (FileNotFoundError, pickle.UnpicklingError, EOFError) as e:
            print(f"Error deserializing object: {e}")
            return None
