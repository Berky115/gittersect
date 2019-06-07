import fire
import requests
import json


class GittersectService(object):
    '''A means of comparing followers between two users'''

    def single_user(self, name):
        print(name + " ??????????")
        gh_session = requests.Session()  # Session may come in handy later down the line , see https://gist.github.com/mxmader/8281851a99d0cfb53a363286246c08d8
        url = ''.join(['https://api.github.com/users/', name, '/followers'])
        followers = json.loads(gh_session.get(url).text)
        print('_______________________')
        print followers
        followers_login = []

        for follower in followers:
            followers_login.append(follower['login'])

        return followers_login

    def compare_users(self, user1, user2):
        user1_followers = self.single_user(user1)
        user2_followers = self.single_user(user2)

        total = 0
        for follower in user1_followers:
            if follower in user2_followers:
                print(follower)
                total += 1
        if total == 0:
            print('No matches found!')

#Note : Not a part of GittersectService class, likely refactor opportunity
# Delayed response, may need to optimize.
def main():
    fire.Fire(GittersectService)

if __name__ == '__main__':
    main()
