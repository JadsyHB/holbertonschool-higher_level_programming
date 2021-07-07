#!/usr/bin/env python3
""" Unittest module """

from parameterized import parameterized
from unittest import TestCase
from utils import access_nested_map


class TestAccessNestedMap(TestCase):
    """
    unittest test class
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1), 
        ({"a": {"b": 2}}, ("a",), {"b": 2}), 
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, map, path, expected_out):
        """Test method for access nested map"""
        out = access_nested_map(map, path)
        self.assertEqual(out, expected_out)
