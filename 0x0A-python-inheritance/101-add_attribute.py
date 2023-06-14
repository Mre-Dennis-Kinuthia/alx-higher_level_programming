#!/usr/bin/python3
""" add_attribute Module """


def add_attribute(obj, attribute, value):
    """ Adds a new attribute to an object if possible """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, attribute, value)
