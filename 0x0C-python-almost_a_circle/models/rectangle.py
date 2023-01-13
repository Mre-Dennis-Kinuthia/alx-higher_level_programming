#!/usr/bin/python3
"""Decaring class"""
from models.base import Base


class Rectangle(Base):
    """ Class representing a rectangle"""


    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        return self.__width

    def width(self, value):
        self.__width = value

    @property
    def height(self):
        return self.__height

    def height(self, value):
        self.__height = value

    @property
    def x(self):
        return self.__x

    def x(self, value):
        self.__x = value

    @property
    def y(self):
        return self.__y

    def y(self, value):
        self.__y = value
