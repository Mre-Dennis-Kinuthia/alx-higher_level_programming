#!/usr/bin/python3
""" script that fetches https://alx-intranet.hbtn.io/status """
from urllib.request import urlopen


if __name__ == "__main__":
    with urlopen("https://alx-intranet.hbtn.io/status") as response:
        in_bytes = response.read()
        in_utf = in_bytes.decode()
        print("Body response:\n\t- type: {}\n\t- content: {}\n\
\t- utf8 content: {}".format(type(in_bytes), in_bytes, in_utf))
