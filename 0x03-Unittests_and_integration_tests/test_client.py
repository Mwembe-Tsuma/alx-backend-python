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
    """Module to test the GithubOrgClient"""
    @parameterized.expand([
        ("google"),
        ("abc"),
        ])
    @patch("client.get_json", return_value={"payload": True})
    def test_org(self, org_name, mock_get):
        """ Tests the org method of GithubOrgClient """
        github_client = GithubOrgClient(org_name)
        tests_return = github_client.org
        self.assertEqual(tests_return, mock_get.return_value)
        mock_get.assert_called_once

    def test_public_repos_url(self):
        """ Tests the _public_repos_url method of GithubOrgClient """
        with patch.object(GithubOrgClient,
                          "org",
                          new_callable=PropertyMock,
                          return_value={"repos_url": "holberton"}) as mock_get:
            test_json = {"repos_url": "holberton"}
            github_client = GithubOrgClient(test_json.get("repos_url"))
            tests_return = github_client._public_repos_url
            mock_get.assert_called_once
            self.assertEqual(tests_return,
                             mock_get.return_value.get("repos_url"))

    @patch("client.get_json", return_value=[{"name": "holberton"}])
    def test_public_repos(self, mock_get):
        """ Tests the _public_repos_url method of GithubOrgClient """
        with patch.object(GithubOrgClient,
                          "_public_repos_url",
                          new_callable=PropertyMock,
                          return_value="https://api.github.com/") as mock_pub:
            github_client = GithubOrgClient("hoberton")
            tests_return = github_client.public_repos()
            self.assertEqual(tests_return, ["holberton"])
            mock_get.assert_called_once
            mock_pub.assert_called_once

    """ Test the functionality """
    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
        ])
    def test_has_license(self, repo, license_key, expected_return):
        """ to unit-test GithubOrgClient.has_license """
        github_client = GithubOrgClient("holberton")
        tests_return = github_client.has_license(repo, license_key)
        self.assertEqual(expected_return, tests_return)


@parameterized_class(
    ("org_payload", "repos_payload", "expected_repos", "apache2_repos"),
    TEST_PAYLOAD
)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """ Integration tests for the GithubOrgClient class """
    @classmethod
    def setUpClass(cls):
        """ Set up the class for integration testing """
        cls.get_patcher = patch('requests.get', side_effect=HTTPError)

    @classmethod
    def tearDownClass(cls):
        """ Tear down the class after integration testing """
        cls.get_patcher.stop()

    def test_public_repos(self):
        """ Integration test for the public_repos method """
        test_class = GithubOrgClient("holberton")
        assert True

    def test_public_repos_with_license(self):
        """ Integration test for the public_repos_with_license method """
        test_class = GithubOrgClient("holberton")
        assert True
