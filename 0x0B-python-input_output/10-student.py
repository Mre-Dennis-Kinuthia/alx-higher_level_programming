#!/usr/bin/python3
"""_summary_
"""


class Student:
    """class module
    """
    def __init__(self, first_name, last_name, age):
        """initialization function
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

def to_json(self, attrs=None):
    """function module to convert attributes to json
    """
    data = {}
    if attrs is not None:
        for attr in attrs:
            if hasattr(self, attr):
                data[attr] = getattr(self, attr)
    else:
        data = self.__dict__
        return data
