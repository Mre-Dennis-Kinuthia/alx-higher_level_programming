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
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
            return self.__dict__
