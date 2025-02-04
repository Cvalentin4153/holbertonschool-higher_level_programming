#!/usr/bin/python3
"""
Defines a class
"""


class MyList(list):
    """
    MyList inherits from list.
    Args:
        list
    """
    def print_sorted(self):
        """
        Prints sorted list.
        """
        print(sorted(self))
