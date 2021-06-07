#!/usr/bin/python3
"""
module 9 github
"""


from sys import argv
import requests
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    url = 'https://api.github.com/user'
    req = requests.get(url, auth=HTTPBasicAuth(argv[1], argv[2]))
    print(req.json().get('id'))
