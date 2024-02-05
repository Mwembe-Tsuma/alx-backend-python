#!/usr/bin/env python3
"""Test utils module"""


import unittest
from typing import Dict, Tuple, Union
from parameterized import parameterized
from utils import (
    access_nested_map,
    get_json,
    memoize,
)


class TestAccessNestedMap(unittest.TestCase):

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected_results):
        self.assertEqual(access_nested_map(nested_map, path), expected_results)

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError),
    ])
    def test_access_nested_map_exception(self, nested_map, path, exception):
        with self.assertRaises(exception):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """Tests the `get_json` function."""
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    def test_get_json(self, test_url, test_payload, mock_get):
        """Tests get_json function with mocked requests.get."""
        mock_get.return_value = test_payload
        result = get_json(test_url)
        self.assertEqual(result, test_payload)
