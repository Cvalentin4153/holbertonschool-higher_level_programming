#!/usr/bin/python3
"""
This module defines a function `matrix_divided`.
It divides all elements of a matrix by a divisor.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a given number.

    Args:
        matrix (list of lists): A list of lists containing integers or floats.
        div (int or float): The divisor.

    Returns:
        list of lists: A new matrix with each element divided by `div`,
        rounded to 2 decimal places.

    Raises:
        TypeError: If `matrix` is not a list of lists of integers/floats.
        TypeError: If rows of `matrix` are not of the same size.
        TypeError: If `div` is not a number.
        ZeroDivisionError: If `div` is equal to 0.
    """
    # Validate `matrix` is a list of lists and not empty
    if not isinstance(matrix, list) or not all(isinstance(row, list)
                                                     for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    # Validate all elements in the matrix are integers or floats
    for row in matrix:
        if not all(isinstance(element, (int, float)) for element in row):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    # Validate all rows in the matrix are of the same size
    row_size = len(matrix[0]) if len(matrix) > 0 else 0
    for row in matrix:
        if len(row) != row_size:
            raise TypeError("Each row of the matrix must have the same size")

    # Validate `div` is a number
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    # Validate `div` is not zero
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Perform division and round results to 2 decimal places
    return [[round(element / div, 2) for element in row] for row in matrix]
