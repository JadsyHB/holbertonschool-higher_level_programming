#!/usr/bin/python3
"""
module 3 error code
"""


from sys import argv
import urllib.request

if __name__ == "__main__":
    try:
        with urllib.request.urlopen(argv[1]) as response:
            print(response.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
