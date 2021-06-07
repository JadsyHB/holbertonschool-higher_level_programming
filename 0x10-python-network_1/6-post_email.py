#!/usr/bin/python3
"""
module 6 post email
"""


from sys import argv
import requests


if __name__ == "__main__":
    url = argv[1]
    values = {"email": argv[2]}
    r = requests.post(url, data=values)
    print(r.text)
