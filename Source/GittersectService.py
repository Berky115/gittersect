import fire
import requests
import json

class GittersectService(object):
  """A means of comparing followers between two users"""

  def single_user(self, name):
    gh_session = requests.Session() #Session may come in handy later down the line , see https://gist.github.com/mxmader/8281851a99d0cfb53a363286246c08d8
    follower = json.loads(gh_session.get('https://api.github.com/users/Berky115/followers').text)

    for follower in follower:
      print(follower['login'])


def main():
    fire.Fire(GittersectService)

if __name__ == '__main__':
    main()