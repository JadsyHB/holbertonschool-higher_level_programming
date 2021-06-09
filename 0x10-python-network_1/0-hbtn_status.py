#!/usr/bin/python3
"""
Module 0 status
"""


import urllib.request


if __name__ == "__main__":
    with urllib.request.urlopen('https://intranet.hbtn.io/status') as r:
        req = r.read()
        print('Body response:')
        print("\t- type: {}".format(type(req)))
        print("\t- content: {}".format(req))
        print("\t- utf8 content: {}".format(req.decode('utf-8')))
