#!/usr/bin/python3
"""Defines a class BaseGeometry"""


class BaseGeometry():
    """
    A base class for geometric operations.

    This class provides a foundation for geometric calculations
    and includes methods for validating integer values. It serves
    as a blueprint for other geometry-related classes.

    Methods:
        area(self):
            Raises an Exception indicating that the method is not implemented.

        integer_validator(self, name, value):
            Validates that `value` is an integer greater than 0.
    """

    def area(self):
        """
        Calculate the area.

        Raises:
            Exception: If the area method is not implemented.
        """

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates if a given value is an integer greater than 0.

        Args:
            name: String with the name of the value to validate.
            value: Value to validate.

        Raises:
            TypeError: if value is not an integer.
            ValueError: if value is not greater than 0.
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")

class Rectangle(BaseGeometry):
        """
        Initializes a Rectangle with a given width and height.

        Args:
            width (int): width of the Rectangle.
            height (int): height of the Rectangle.

        Raises:
            TypeError: if either width or height is not an integer.
            ValueError: if either width or height is not greater than 0.
        """
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
