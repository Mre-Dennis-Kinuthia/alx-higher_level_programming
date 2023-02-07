#!/usr/bin/python3
from models.base import Base


class Rectangle(Base):
    """
    Class Rectangle inherits from Base
    Private instance attributes, each with its own public getter and setter:
    __width -> width
    __height -> height
    __x -> x
    __y -> y
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Class constructor: def __init__(self, width, height,
        x=0, y=0, id=None):
        Call the super class with id -
        this super call with use the logic
        of the __init__ of the Base class
        Assign each argument width, height,
        area, x and y to the right attribute
        """
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        