#!/usr/bin/python3
""" Square Module """


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Square Sub Class of Rectangle """

    def __init__(self, size):
        """ Initializes data for the square class """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """ Returns the area of a square """
        return super().area()

    def __str__(self):
        """ Defines print output """
        return "[Square] {}/{}".format(self.__size, self.__size)
