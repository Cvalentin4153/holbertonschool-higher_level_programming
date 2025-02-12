#!/usr/bin/python3
""" Student class """


class Student:
    def __init__(self, first_name, last_name, age):

        """
        Initializes a new Student instance.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance.

        Args:
            attrs (list, optional): List of attribute names to retrieve.

        Returns:
            dict: A dictionary representation of the Student instance.
        """
        if isinstance(attrs, list) and all(isinstance(attr, str)
                                           for attr in attrs):
            return {key: getattr(self, key)
                    for key in attrs if hasattr(self, key)}
        return self.__dict__

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance
        with values from a JSON dictionary.

        Args:
            json (dict): A dictionary containing attribute
            names and values.
        """
        for key, value in json.items():
            setattr(self, key, value)
