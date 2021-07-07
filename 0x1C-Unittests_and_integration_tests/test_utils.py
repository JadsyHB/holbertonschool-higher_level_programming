#!/usr/bin/env python3
""" Unittest module """

from parameterized import parameterized
from unittest import TestCase
from utils import access_nested_map, get_json, memoize
from unittest.mock import patch, Mock


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

    @parameterized.expand([
        ({}, ("a",), 'a'),
        ({"a": 1}, ("a", "b"), 'b')
    ])
    def test_access_nested_map_exception(self, map, path, false):
        """test method for error raised"""
        with self.assertRaises(KeyError) as err:
            access_nested_map(map, path)
            self.assertEqual(false, err.exception)

class TestGetJson(TestCase):
    """class test get json"""
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, test_url, test_payload):
        """test method returns output"""
        mock_resp = Mock()
        mock_resp.json.return_value = test_payload
        with patch('requests.get', return_value=mock_resp):
            resp = get_json(test_url)
            self.assertEqual(resp, test_payload)

class TestMemoize(TestCase):
    """class for testing  memoize"""
    def test_memoize(self):
        """test memoize"""
        class TestClass:

            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(TestClass, 'a_method', return_value=42) as p:
            test_class = TestClass()
            ret = test_class.a_property
            self.assertEqual(ret, 42)
            p.assert_called_once()
