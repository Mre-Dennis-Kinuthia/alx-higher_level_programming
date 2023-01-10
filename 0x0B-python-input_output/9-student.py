#!/usr/bin/python3
"""_summary_
"""


class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age


def to_json(snt):
    json_obj = {}
    for key in snt.__dict__:
        if isinstance(snt.__dict__[key], (int, str, float, bool, list, dict)):
            json_obj[key] = snt.__dict__[key]
    return json_obj
