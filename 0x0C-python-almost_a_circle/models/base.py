#!/usr/bin/python3
"""class declaration"""


class Base:

    """
    Class Base has a class variable
    __nb_objects to keep track of the number of objects
    """

    __nb_objects = 0

    def __init__(self, id=None):
        if id is None:
            Base.__nb_objects += 1
            id = Base.__nb_objects
        self.id = id
