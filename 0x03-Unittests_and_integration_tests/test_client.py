#!/usr/bin/env python3
"""Module to test the GithubOrgClient class."""
import unittest
from typing import Dict
from unittest.mock import MagicMock, Mock, PropertyMock, patch
from parameterized import parameterized, parameterized_class
from requests import HTTPError
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD


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


class TestGithubOrgClient(unittest.TestCase):
    """Tests the GithubOrgClient class."""

    def test_public_repos_url(self):
        """Tests the _public_repos_url method of GithubOrgClient."""
        payload = {"repos_url": "https://api.github.com/orgs/test_org/repos"}

        with patch('client.GithubOrgClient.org', return_value=payload):
            github_client = GithubOrgClient("test_org")
            result = github_client._public_repos_url()

        expected_url = payload["repos_url"]
        self.assertEqual(result, expected_url)
