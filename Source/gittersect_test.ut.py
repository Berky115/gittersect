import unittest
import time
import sys

from GittersectService import *


class Test_gittersect(unittest.TestCase):
    def setUp(self):
        self.gittersect = GittersectService()

    # def test_returns_user_data_from_api(self):
    #     followers = self.gittersect.single_user('Berky115')
    #     self.assertEqual(3 == len(followers), True)

    # def test_returns_nothing_if_user_has_no_followers(self):
    #     followers = self.gittersect.single_user('Berky115Ghost')  #Berky115Ghost is a test account
    #     self.assertEqual(0 == len(followers), True)

    def test_returns_nothing_if_user_does_not_exist(self):
        ollowers = self.gittersect.single_user('Berky115GhosttheGREAT!')  #Berky115Ghost is a test account
        self.assertEqual(0 == len(followers), True)

if __name__ == '__main__':
    unittest.main()