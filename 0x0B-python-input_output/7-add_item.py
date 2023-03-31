#!/usr/bin/python3
"""
Declearing function
"""
import json
import os
import importlib
from sys import argv


def save_to_json_file(my_obj, filename):
    with open(filename, 'w') as f:
        json.dump(my_obj, f)


def load_from_json_file(filename):
    with open(filename) as f:
        return json.load(f)


if __name__ == "__main__":
    args = []
    filename = "add_item.json"
    if os.path.exists(filename):
        args = load_from_json_file(filename)
    for elem in argv[1:]:
        args.append(elem)
    save_to_json_file(args, filename)
