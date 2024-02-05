#!/usr/bin/env python3
"""Module to test the GithubOrgClient class."""
import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Tests the GithubOrgClient class."""

    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch('client.get_json', return_value={"name": "test_org"})
    def test_org(self, org_name, res):
        """Tests the org method of GithubOrgClient."""
        github_client = GithubOrgClient(org_name)
        result = github_client.org()

        res.assert_called_once_with(f"https://api.github.com/orgs/{org_name}")
        self.assertEqual(result, {"name": "test_org"})
