#!/usr/bin/python3
"""_summary_
"""


class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

def to_json(self, attrs=None):
    data = {}
    if attrs is not None:
        for attr in attrs:
            if hasattr(self, attr):
                data[attr] = getattr(self, attr)
    else:
        data = self.__dict__
        return data
