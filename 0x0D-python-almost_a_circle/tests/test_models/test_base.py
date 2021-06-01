#!/usr/bin/python3
"""
unittest for Base class
"""

import json
import os
import unittest
from models import base
from models import rectangle
Base = base.Base
Rectangle = rectangle.Rectangle


class testBase(unittest.TestCase):
    """
    test for base
    """

    def setUp(self):
        pass

    def tearDown(self):
        try:
            os.remove("Rectangle.json")
        except:
            pass

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

    def test_error_args(self):
        """
        testing with error args: more
        """
        with self.assertRaises(TypeError):
            Base(1, 1)

    def test_class(self):
        """
        test class
        """
        self.assertTrue(Base(10), self.__class__ == Base)

    def test_to_json_string(self):
        """
        test to json string
        """
        r1 = Rectangle(10, 7, 2, 8, 1)
        dictionary = r1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        self.assertEqual(dictionary, {'x': 2, 'width': 10, 'id': 1, 'height': 7, 'y': 8})
        self.assertTrue(json_dictionary, '[{"x": 2, "width": 10, "id": 1, "height": 7, "y": 8}]')
        
    def test_empty_json(self):
        """
        none
        """
        self.assertTrue(Base.to_json_string(None), "[]")
        self.assertTrue(type(Base.to_json_string(None)) == str)
        dic = dict()
        self.assertTrue(Base.to_json_string(dic), "[]")
        self.assertTrue(type(Base.to_json_string(dic)) == str)

    def test_save_to_file(self):
        """
        test save to file
        """
        r1 = Rectangle(10, 7, 2, 8, 1)
        Rectangle.save_to_file([r1])
        with open("Rectangle.json", "r") as file:
            self.assertTrue('[{"y": 8, "x": 2, "id": 1, "width": 10, "height": 7}]', file.read())

    def test_save_empty(self):
        """
        test with empty
        """
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as f:
            self.assertEqual("[]", f.read())

    def test_from_json_string(self):
        """
        test from json string
        """
        list_input = [
            {'id': 89, 'width': 10, 'height': 4}, 
            {'id': 7, 'width': 1, 'height': 7}
        ]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertTrue(list_output, [{'height': 4, 'width': 10, 'id': 89}, {'height': 7, 'width': 1, 'id': 7}])

    def test_load_from_file(self):
        """
        test load
        """
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 0, 0, 2)
        list_rectangles_input = [r1, r2]
        Rectangle.save_to_file(list_rectangles_input)
        list_rectangles_output = Rectangle.load_from_file()
        for k, v in enumerate(list_rectangles_output):
            if k == 0:
                self.assertEqual(str(v), '[Rectangle] (1) 2/8 - 10/7')
            if k == 1:
                self.assertEqual(str(v), '[Rectangle] (2) 0/0 - 2/4')

    def test_save_empty(self):
        """
        test save empty
        """
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as f:
            self.assertEqual("[]", f.read())

    def test_load_empty(self):
        """
        test load none and empty
        """
        Rectangle.save_to_file(None)
        rr = Rectangle.load_from_file()
        self.assertEqual(len(rr), 0)

    def test_load_empty(self):
        """
        test load none and empty
        """
        Rectangle.save_to_file([])
        rr = Rectangle.load_from_file()
        self.assertEqual(len(rr), 0)
