#!/usr/bin/python3
"""
unittest for Base class
"""


import unittest
import pep8
from models import base
from models import rectangle
Base = base.Base
Rectangle = rectangle.Rectangle


class testBase(unittest.TestCase):
    """
    test for base
    """
    def test_base_id(self):
        """
        testing id
        """
        self.assertTrue(Base(1), self.id == 1)
        self.assertTrue(Base(5), self.id == 5)
        self.assertTrue(Base(-1), self.id == -1)

    def test_base_id_not_given(self):
        """
        testing no id given
        """
        self.assertTrue(Base(), self.id == 1)
        self.assertTrue(Base(), self.id == 2)
        self.assertTrue(Base(), self.id == 3)

    
