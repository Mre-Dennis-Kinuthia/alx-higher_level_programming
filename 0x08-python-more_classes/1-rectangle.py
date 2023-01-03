#!/usr/bin/python3
"""
This is an empty class
"""


class Rectangle:
    """
    create rectangle object
    """
    def width(self):
        def __init__ (self, value):
            if not isinstance(value, int):
                raise TypeError('width must be an integer')
            self.width = value
        if value < 0:
            raise ValueError('width must be >= 0')
        