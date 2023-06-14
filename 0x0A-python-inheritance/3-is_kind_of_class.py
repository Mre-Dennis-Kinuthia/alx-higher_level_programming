#!/usr/bin/python3
""" is_kind_of_class Module """


def is_kind_of_class(obj, a_class):
    """ Checks if the object is an instance, or if the object is an instance of
    a class that inherited from the specified class """
    return isinstance(obj, a_class)
