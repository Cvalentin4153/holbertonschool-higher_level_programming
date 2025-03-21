#!/usr/bin/python3
"""Defines a Pascal's triangle function."""


def pascal_triangle(n):
    """
    Returns a list of lists of integers representing
    the Pascal's triangle of n.

    Returns an empty list if n is 0 or negative.
    Otherwise, returns a list of lists where each inner
    list has one more element
    than the last, and the first and last elements
    of each inner list are 1.
    The remaining elements of each inner list are the
    sum of the two elements
    directly above them.
    """

    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        row.append(1)
        triangle.append(row)

    return triangle
