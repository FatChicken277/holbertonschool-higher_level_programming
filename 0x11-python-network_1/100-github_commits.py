#!/usr/bin/python3
"""[summary]
"""
import requests
from sys import argv


if __name__ == "__main__":
    url = "https://api.github.com/repos/{}/{}/commits".format(argv[2], argv[1])
    r = requests.get(url)
    for i in r.json()[:10]:
        print("{}: {}".format(
            i.get('sha'), i.get('commit').get('author').get('name')))
