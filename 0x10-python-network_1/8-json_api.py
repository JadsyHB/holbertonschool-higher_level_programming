#!/usr/bin/python3
"""
module json api 8
"""


from sys import argv
import requests


if __name__ == "__main__":
    if len(argv) < 2:
        value = ""
    else:
        value = argv[1]
    url = "http://0.0.0.0:5000/search_user"
    values = {"q": letter}
    r = requests.post(url, data=values)
    try:
        req = r.json()
        if req:
            print("[{}] {}".format(req["id"], req["name"]))
        else:
            print("No result")
    except ValueError as e:
        print("Not a valid JSON")
