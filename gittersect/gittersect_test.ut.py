import unittest
import requests_mock
import time
import sys

from gittersect import *


class Test_gittersect(unittest.TestCase):
    def setUp(self):
        self.gittersect = GittersectService()

    @requests_mock.mock()
    def test_returns_user_data_from_api(self, mock):
        mock.get('https://api.github.com/users/standard_user/followers', text='[ { "login": "A" }, { "login": "B" }, { "login": "C" }, { "login": "D" } ]')
        followers = self.gittersect.single_user('standard_user')
        self.assertEqual(4 == len(followers), True)

    @requests_mock.mock()
    def test_returns_nothing_if_user_has_no_followers(self, mock):
        mock.get('https://api.github.com/users/no_followers/followers', text='[]')
        followers = self.gittersect.single_user('no_followers')
        self.assertEqual(0 == len(followers), True)

    @requests_mock.mock()
    def test_returns_nothing_if_user_does_not_exist(self, mock):
        mock.get('https://api.github.com/users/non_existing_user/followers', text='{ "message": "Not Found", "documentation_url": "https://developer.github.com/v3/users/followers/#list-followers-of-a-user" }')
        followers = self.gittersect.single_user('non_existing_user')
        self.assertEqual('Not Found' == followers['message'], True)

    @requests_mock.mock()
    def test_api_token_is_invalid(self, mock):
        mock.get('https://api.github.com/users/existing_user/followers', text='{ "message": "Bad credentials", "documentation_url": "https://developer.github.com/v3/users/followers/#list-followers-of-a-user" }')
        followers = self.gittersect.single_user('existing_user')
        self.assertEqual('Bad credentials' == followers['message'], True)

    @requests_mock.mock()
    def test_compare_users_works_with_two_valid_users(self, mock):
        mock.get('https://api.github.com/users/standard_user_a/followers', text='[ { "login": "A" }, { "login": "B" }, { "login": "C" }, { "login": "D" } ]')
        mock.get('https://api.github.com/users/standard_user_b/followers', text='[ { "login": "A2" }, { "login": "B" }, { "login": "C2" }, { "login": "D" } ]')
        response = self.gittersect.compare_users('standard_user_a', 'standard_user_b')
        self.assertEqual([u'B', u'D'] == response, True)

if __name__ == '__main__':
    unittest.main()