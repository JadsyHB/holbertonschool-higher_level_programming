#!/usr/bin/env python3
"""
unittest for client
"""
from client import GitHubOrgClient
from unittest import TestCase
from parameterized import parameterized
from unittest.mock import patch, Mock, PropertyMock



class TestGithubOrgClient(TestCase):
    """
    class github test
    """
    @parameterized.expand([
        ("google"),
        ("abc")
    ])
    @patch("client.get_json", return_value={"payload": True})
    def test_org(self, org, get_mock):
        """test org function"""
        client = GithubOrgClient(org)
        ret = client.org
        self.assertEqual(ret, get_mock.return_value)
