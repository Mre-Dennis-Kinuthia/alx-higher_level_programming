#!/usr/bin/python3
"""
script that takes your GitHub credentials (username and password)
and uses the GitHub API to display your id
"""
import requests
from sys import argv


if __name__ == "__main__":
    url = "https://api.github.com/user"
    headers = {"Accept": "application/vnd.github+json"}
    r = requests.get(url, headers=headers, auth=(argv[1], argv[2]))
    user_id = r.json().get('id')
    print(user_id)
