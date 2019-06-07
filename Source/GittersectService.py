import fire
import requests
import json


class GittersectService(object):
    '''A commandline utility comparing followers between two users'''

    def single_user(self, name):
        gh_session = requests.Session()
        url = ''.join(['https://api.github.com/users/', name, '/followers'])
        followers = json.loads(gh_session.get(url).text)

        followers_login = []
        for follower in followers:
            if 'login' in follower:
                followers_login.append(follower['login'])

        return followers_login

    def compare_users(self, user1, user2):
        user1_followers = self.single_user(user1)
        user2_followers = self.single_user(user2)

        total = 0
        intersecting_followers = []
        for follower in user1_followers:
            if follower in user2_followers:
                intersecting_followers.append(follower)
                total += 1
        if total == 0:
            intersecting_followers.append('No matches found!')
        self.print_intersecting_users(intersecting_followers)
          
    def print_intersecting_users(self, followers):
        for follower in followers:
            print follower

#Note : Not a part of GittersectService class, likely refactor opportunity
# Delayed response, may need to optimize.


def main():
    fire.Fire(GittersectService)

if __name__ == '__main__':
    main()
