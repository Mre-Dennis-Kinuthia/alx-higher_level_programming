#!/usr/bin/python3
"""
script to list 10 commits (from the most recent to oldest) of
the repository “rails” by the user “rails”
"""
from sys import argv
import requests


if __name__ == "__main__":
    usr = argv[2]
    repo = argv[1]
    url = "https://api.github.com/repos/" + usr + "/" + repo + "/commits"
    r = requests.get(url)
    result = r.json()

    for i in range(10):
        sha = result[i].get("sha")
        author_name = result[i].get("commit").get("author").get("name")
        print("{}: {}".format(sha, author_name))
