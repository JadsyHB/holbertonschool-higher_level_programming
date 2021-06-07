#!/usr/bin/python3
"""
module 5 response
"""


from sys import argv
import requests


if __name__ == "__main__":
    r = requests.get(argv[1])
    print(r.headers.get("X-Request-Id"))
