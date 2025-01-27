#!/usr/bin/python3
"""Unittest for max_integer function in 6-max_integer.py"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test cases for max_integer function"""

    def test_regular_list(self):
        """Test with a regular list of integers"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def test_negative_numbers(self):
        """Test with a list containing negative numbers"""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        self.assertEqual(max_integer([-4, -3, -2, -1]), -1)

    def test_mixed_numbers(self):
        """Test with a list containing both positive and negative numbers"""
        self.assertEqual(max_integer([-10, 5, 2, -1, 0]), 5)

    def test_single_element(self):
        """Test with a list containing a single element"""
        self.assertEqual(max_integer([42]), 42)

    def test_empty_list(self):
        """Test with an empty list"""
        self.assertIsNone(max_integer([]))

    def test_duplicates(self):
        """Test with a list containing duplicate values"""
        self.assertEqual(max_integer([1, 2, 3, 3]), 3)
        self.assertEqual(max_integer([3, 3, 3, 3]), 3)

    def test_large_numbers(self):
        """Test with a list containing very large numbers"""
        self.assertEqual(max_integer([10**6, 10**8, 10**10]), 10**10)

    def test_floats(self):
        """Test with a list containing floating point numbers"""
        self.assertEqual(max_integer([1.1, 2.2, 3.3, 4.4]), 4.4)
        self.assertEqual(max_integer([-1.1, -2.2, -3.3, -4.4]), -1.1)

    def test_mixed_types(self):
        """Test with a list containing both integers and floats"""
        self.assertEqual(max_integer([1, 2.5, 3, 4.8]), 4.8)

    def test_strings(self):
        """Test with a list containing strings"""
        self.assertEqual(max_integer(['a', 'b', 'c', 'd']), 'd')
        self.assertEqual(max_integer(['apple', 'banana', 'cherry']), 'cherry')

    def test_single_string(self):
        """Test with a single string"""
        self.assertEqual(max_integer('hello'), 'o')

    def test_none(self):
        """Test with None as input"""
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_invalid_types(self):
        """Test with invalid input types"""
        with self.assertRaises(TypeError):
            max_integer(42)
        with self.assertRaises(TypeError):
            max_integer(3.14)
        with self.assertRaises(TypeError):
            max_integer({'a': 1, 'b': 2})
        with self.assertRaises(TypeError):
            max_integer(True)

if __name__ == '__main__':
    unittest.main()