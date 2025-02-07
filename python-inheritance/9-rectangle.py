#!/usr/bin/python3
"""Defines a Class"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):

    """Defines a class Rectangle that inherits from BaseGeometry"""

    def __init__(self, width, height):
        """
        Initializes a Rectangle with a given width and height.

        Args:
            width (int): width of the Rectangle.
            height (int): height of the Rectangle.

        Raises:
            TypeError: if either width or height is not an integer.
            ValueError: if either width or height is not greater than 0.
        """

        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def __str__(self):
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
