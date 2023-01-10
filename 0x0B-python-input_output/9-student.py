#!/usr/bin/python3
"""_summary_
"""


class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age


def to_json(self):
    json_obj = {}
    for key in self.__dict__:
        if isinstance(self.__dict__[key], (int, str, float, bool, list, dict)):
            json_obj[key] = self.__dict__[key]
    return json_obj
