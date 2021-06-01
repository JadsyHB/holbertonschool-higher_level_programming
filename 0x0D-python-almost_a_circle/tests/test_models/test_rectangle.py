#!/usr/bin/python3
"""
unittest for Base class
"""


import os
from io import StringIO
from contextlib import redirect_stdout
import unittest
from models import rectangle
Rectangle = rectangle.Rectangle


class testBase(unittest.TestCase):
    """
    test for Rectangle
    """
    def test_attributes_allgiven(self):
        """
        test when all attributes are given
        """
        r = Rectangle(4, 6, 2, 3, 5)
        self.assertTrue(r.width == 4)
        self.assertTrue(r.height == 6)
        self.assertTrue(r.x == 2)
        self.assertTrue(r.y == 3)
        self.assertTrue(r.id == 5)

    def test_attributes_not_given(self):
        """
        default test atts
        """
        r1 = Rectangle(5, 6)
        self.assertTrue(r1.width == 5)
        self.assertTrue(r1.height == 6)
        self.assertTrue(r1.x == 0)
        self.assertTrue(r1.y == 0)
        self.assertTrue(r1.id is not None)

    def test_errors(self):
        """
        testing errors
        """
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("2", 1, 3, 3, 1)
            Rectangle([3], 1, 3, 3, 1)
            Rectangle((1, 2), 1, 3, 3, 1)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, "1", 3, 3, 1)
            Rectangle(3, [1], 3, 3, 1)
            Rectangle(1, (1, 2), 3, 3, 1)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(2, 1, "3", 3, 1)
            Rectangle(3, 1, [3], 3, 1)
            Rectangle(2, 1, (3, 2), 3, 1)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(2, 1, 3, "3", 1)
            Rectangle(3, 1, 3, [3], 1)
            Rectangle(2, 1, 3, (3, 2), 1)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(0, 1, 3, 3, 1)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(2, 0, 3, 3, 1)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(2, 1, -2, 3, 1)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(2, 1, 3, -1, 1)

    def test_area(self):
        """
        test area
        """
        r2 = Rectangle(3, 4)
        self.assertEqual(r2.area(), 12)
        r3 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r3.area(), 56)

    #def test_display(self):
        """
        testing display
        """
    def test_print(self):
        """
        testing __str__
        """
        r1 = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r1), "[Rectangle] (12) 2/1 - 4/6")
        r2 = Rectangle(5, 5, 1)
        self.assertEqual(str(r2), "[Rectangle] (6) 1/0 - 5/5")

    def test_update_args(self):
        """
        testing update
        """
        r1 = Rectangle(10, 10, 10, 10)
        self.assertEqual(str(r1), "[Rectangle] (7) 10/10 - 10/10")
        r1.update(89)
        self.assertEqual(str(r1), "[Rectangle] (89) 10/10 - 10/10")
        r1.update(89, 2)
        self.assertEqual(str(r1), "[Rectangle] (89) 10/10 - 2/10")
        r1.update(89, 2, 3)
        self.assertEqual(str(r1), "[Rectangle] (89) 10/10 - 2/3")
        r1.update(89, 2, 3, 4)
        self.assertEqual(str(r1), "[Rectangle] (89) 4/10 - 2/3")
        r1.update(89, 2, 3, 4, 5)
        self.assertEqual(str(r1), "[Rectangle] (89) 4/5 - 2/3")

    def test_update_kwargs(self):
        """
        testing update kwargs
        """
        r1 = Rectangle(10, 10, 10, 10)
        self.assertEqual(str(r1), "[Rectangle] (8) 10/10 - 10/10")
        r1.update(height=1)
        self.assertEqual(str(r1), "[Rectangle] (8) 10/10 - 10/1")
        r1.update(width=1, x=2)
        self.assertEqual(str(r1), "[Rectangle] (8) 2/10 - 1/1")
        r1.update(y=1, width=2, x=3, id=89)
        self.assertEqual(str(r1), "[Rectangle] (89) 3/1 - 2/1")
        r1.update(x=1, height=2, y=3, width=4)
        self.assertEqual(str(r1), "[Rectangle] (89) 1/3 - 4/2")

    def test_to_dictionnary(self):
        """
        test to_dictionnary
        """
        r1 = Rectangle(10, 2, 1, 9, 1)
        self.assertEqual(str(r1), "[Rectangle] (1) 1/9 - 10/2")
        self.assertEqual(type(r1.to_dictionary()), dict)

    def test_more_or_less_args(self):
        """
        testing more args or less args
        """
        with self.assertRaises(TypeError):
            Rectangle(1, 1, 1, 1, 1, 1, 1)
            Rectangle()
            Rectangle(1)
