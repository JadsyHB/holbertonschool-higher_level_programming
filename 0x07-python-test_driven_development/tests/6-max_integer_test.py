#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):

    def test_success_ints_floats_signed_unsigned(self):
        self.assertEqual(max_integer([0]), 0)
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)
        self.assertEqual(max_integer([5, 3, 4, 2]), 5)
        self.assertEqual(max_integer([-1, -0.5, -10, -4]), -0.5)
        self.assertEqual(max_integer([0.1, 0.2, 0.4]), 0.4)

    def test_success_list_of_strings(self):
        self.assertEqual(max_integer(["a", "b", "c"]), "c")
        self.assertEqual(max_integer(["hello", "xyloph"]), "xyloph")

    def test_unsuccessful_cases_with_different_data_types(self):
        with self.assertRaises(TypeError):
            max_integer({1, 2, 4, 9})
        with self.assertRaises(TypeError):
            max_integer([1, 2, "hello"])
        with self.assertRaises(TypeError):
            max_integer(True)

    def test_None(self):
        self.assertIsNone(max_integer([]), None)
        self.assertIsNone(max_integer(), None)
        self.assertIsNone(max_integer([None]), None)

if __name__ == "__main__":
    unittest.main()
