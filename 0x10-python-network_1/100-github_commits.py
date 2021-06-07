#!/usr/bin/python3
"""
module 100 commits
"""


from sys import argv
import requests


if __name__ == "__main__":
    repo = argv[1]
    user = argv[2]
    url = "https://api.github.com/repos/{}/{}/commits".format(user, repo)
    r = requests.get(url)
    commits = r.json()
    for i in commits[0:10]:
        print(i.get('sha'), end=': ')
        print(i.get('commit').get('author').get('name'))
