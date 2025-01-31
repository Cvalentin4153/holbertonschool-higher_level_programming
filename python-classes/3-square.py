#!/usr/bin/python3
"""Defines a square class."""


class Square:
    """
    A class that defines a square.
    """
    def __init__(self, size=0):
        """
        Initializes a new sqaure.

        Args:
            size: the size of the square.

            Raises:
            TypeError: if size is not an integer.
            ValueError: if size is less than 0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Calculates the area of the square.

        Returns:
            The area of the square.
        """
        return self.__size ** 2
