#!/usr/bin/python3
""" Rectangle Module """


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Rectangle Sub Class of BaseGeometry """

    def __init__(self, width, height):
        """ Initializes data for the rectangle class """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
