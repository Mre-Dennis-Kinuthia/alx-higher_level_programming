#!/usr/bin/python3
""" is_same_class Module """


def is_same_class(obj, a_class):
    """ Checks if the object is exactly an instance of the specified class """
    return type(obj) == a_class
