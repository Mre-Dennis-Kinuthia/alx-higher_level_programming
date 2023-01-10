#!/usr/bin/python3
"""_summary_
"""


class Student:
    '''module class student
    '''
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(snt):
        """_summary_

    Args:
        obj (_type_): _description_

    Returns:
        _type_: _description_
    """
        return self.__dict__
