#!/usr/bin/python3
""" Rectangle Class Module """
from models.base import Base


class Rectangle(Base):
    """ Rectangle Class, Subclass of Class Base """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Initializes a rectangle with size attributes """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """ Returns width of rectangle """
        return self.__width

    @width.setter
    def width(self, value):
        """ Sets width of rectangle """
        if not type(value) == int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        """ Returns height of rectangle """
        return self.__height

    @height.setter
    def height(self, value):
        """ Sets height of rectangle """
        if not type(value) == int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        """ Returns x """
        return self.__x

    @x.setter
    def x(self, value):
        """ Sets x """
        if not type(value) == int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        """ Returns y """
        return self.__y

    @y.setter
    def y(self, value):
        """ Sets y """
        if not type(value) == int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        """ Returns area of rectangle """
        return self.__width * self.__height

    def display(self):
        """ Prints the rectangle to stdout using # """
        for i in range(self.__y):
            print("")
        for i in range(self.__height):
            print(" " * self.__x + "#" * self.__width)

    def __str__(self):
        """ Returns a string representation of the Rectangle class """
        return "[{}] ({}) {}/{} - {}/{}".format(type(self).__name__, self.id,
                                                self.__x, self.__y,
                                                self.__width, self.__height)

    def update(self, *args, **kwargs):
        """ Assigns an argument to each attribute """
        if args and len(args) != 0:
            for i, arg in enumerate(args):
                if i == 0:
                    self.id = arg
                if i == 1:
                    self.width = arg
                if i == 2:
                    self.height = arg
                if i == 3:
                    self.x = arg
                if i == 4:
                    self.y = arg
        else:
            if kwargs:
                for key, arg in kwargs.items():
                    if key == "id":
                        self.id = arg
                    if key == "width":
                        self.width = arg
                    if key == "height":
                        self.height = arg
                    if key == "x":
                        self.x = arg
                    if key == "y":
                        self.y = arg

    def to_dictionary(self):
        """ Returns a dictionary representation of the Rectangle Class """
        class_dict = {'id': self.id, 'width': self.width,
                      'height': self.height, 'x': self.x, 'y': self.y}
        return class_dict
