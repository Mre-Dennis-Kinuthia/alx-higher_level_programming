#!/usr/bin/python3
"""Program that creates an
Object from a “JSON file”:
"""

import json


def load_from_json_file(filename):
    """function that creates an
    Object from a “JSON file”:
    """
    with open(filename, encoding="utf-8") as json_file:
        json_data = json_file.read()
        return json.loads(json_data)
