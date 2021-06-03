#!/usr/bin/python3
"""
unittest for Square class
"""


import os
from io import StringIO
from contextlib import redirect_stdout
import unittest
from models import square
Square = square.Square


class testBase(unittest.TestCase):
    """
    test for Square
    """
    def test_attributes_allgiven(self):
        """
        test when all attributes are given
        """
        s = Square(4, 1, 1, 1)
        self.assertTrue(s.width == 4)
        self.assertTrue(s.height == 4)
        self.assertTrue(s.size == 4)
        self.assertTrue(s.x == 1)
        self.assertTrue(s.y == 1)
        self.assertTrue(s.id == 1)

    def test_attributes_not_given(self):
        """
        default test atts
        """
        s1 = Square(4)
        self.assertTrue(s1.width == 4)
        self.assertTrue(s1.height == 4)
        self.assertTrue(s1.size == 4)
        self.assertTrue(s1.x == 0)
        self.assertTrue(s1.y == 0)
        self.assertTrue(s1.id is not None)

    def test_errors(self):
        """
        testing errors
        """
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("2")
            Square([3])
            Square(True)
            Square({1})
            Square((1, ))
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(-1)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, "2")
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 2, "3")
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Square(1, -2)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Square(1, 2, -3)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(0)

    def test_area(self):
        """
        test area
        """
        s2 = Square(4)
        self.assertEqual(s2.area(), 16)
        s3 = Square(3)
        self.assertEqual(s3.area(), 9)

    #def test_display(self):
        """
        testing display
        """
    def test_print(self):
        """
        testing __str__
        """
        s4 = Square(4, 2, 1, 12)
        self.assertEqual(str(s4), "[Square] (12) 2/1 - 4")
        s5 = Square(5)
        self.assertEqual(str(s5), "[Square] (24) 0/0 - 5")

    def test_update_args(self):
        """
        testing update
        """
        s1 = Square(5)
        self.assertEqual(str(s1), "[Square] (26) 0/0 - 5")
        s1.update(10)
        self.assertEqual(str(s1), "[Square] (10) 0/0 - 5")
        s1.update(1, 2)
        self.assertEqual(str(s1), "[Square] (1) 0/0 - 2")
        s1.update(1, 2, 3)
        self.assertEqual(str(s1), "[Square] (1) 3/0 - 2")
        s1.update(1, 2, 3, 4)
        self.assertEqual(str(s1), "[Square] (1) 3/4 - 2")

    def test_update_kwargs(self):
        """
        testing update kwargs
        """
        s2 = Square(2, 3, 4, 1)
        self.assertEqual(str(s2), "[Square] (1) 3/4 - 2")
        s2.update(x=12)
        self.assertEqual(str(s2), "[Square] (1) 12/4 - 2")
        s2.update(size=7, y=1)
        self.assertEqual(str(s2), "[Square] (1) 12/1 - 7")
        s2.update(size=7, id=89, y=1)
        self.assertEqual(str(s2), "[Square] (89) 12/1 - 7")

    def test_to_dictionnary(self):
        """
        test to_dictionnary
        """
        s3 = Square(10, 2, 1)
        self.assertEqual(str(s3), "[Square] (25) 2/1 - 10")
        self.assertEqual(type(s3.to_dictionary()), dict)

    def test_more_or_less_args(self):
        """
        testing more args or less args
        """
        with self.assertRaises(TypeError):
            Square(1, 1, 1, 1, 1, 1, 1)
            Square()
