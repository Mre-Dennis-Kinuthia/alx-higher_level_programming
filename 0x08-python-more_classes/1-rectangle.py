#!/usr/bin/python3
"""
This is an empty class
"""


class Rectangle:
    """
    create rectangle object
    """
    def width(self):
        def __init__(self, value):
            if not isinstance(value, int):
                raise TypeError('width must be an integer')
            self.width = value
        if value < 0:
            raise ValueError('width must be >= 0')
    
    def height(self):
        def __init__(self, value):
            if not isinstance(value, int):
                raise TypeError('height must be an integer')
            self.height = value
            if value < 0:
                raise ValueError('height must be >= 0')
