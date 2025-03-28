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

    def to_json(self):

        """
        Returns a dictionary representation of the Student instance.

        Returns:
            dict: A dictionary with the same attributes as the instance.
        """

        return self.__dict__
