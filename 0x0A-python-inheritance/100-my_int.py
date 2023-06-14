#!/usr/bin/python3
""" Contains the class MyInt """


class MyInt(int):
    """ Sub Class of int that subverts two methods"""

    def __new__(cls, *args, **kwargs):
        """creates a new instance of the class"""
        return super(MyInt, cls).__new__(cls, *args, **kwargs)

    def __ne__(self, other):
        """ Equal (==) is now Not Equal (!=) """
        return int(self) == other

    def __eq__(self, other):
        """ Not Equal (=!) is now Equal (==) """
        return int(self) != other
