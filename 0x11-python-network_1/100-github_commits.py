#!/usr/bin/python3
"""[summary]
"""
import requests
from sys import argv


if __name__ == "__main__":
    url = "https://api.github.com/repos/{}/{}/commits".format(argv[1], argv[2])
    r = requests.get(url)
    x = 0
    for i in r.json():
        x += 1
        if x == 11:
            break
        print("{}: {}".format(i.get('sha'), i.get('author').get('login')))
