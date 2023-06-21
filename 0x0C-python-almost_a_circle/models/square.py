#!/usr/bin/python3
""" Square Class Module """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Square Class, Subclass of Class Rectangle """

    def __init__(self, size, x=0, y=0, id=None):
        """ Initializes a square with size attributes """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ Returns a string representation of the Square class """
        return "[{}] ({}) {}/{} - {}".format(type(self).__name__, self.id,
                                             self.x, self.y, self.width)

    @property
    def size(self):
        """ Returns the size attribute """
        return self.width

    @size.setter
    def size(self, size):
        """ Sets the size attribute """
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        """ Assigns an argument to each attribute """
        if args and len(args) != 0:
            for i, arg in enumerate(args):
                if i == 0:
                    self.id = arg
                if i == 1:
                    self.size = arg
                if i == 2:
                    self.x = arg
                if i == 3:
                    self.y = arg
        else:
            if kwargs:
                for key, arg in kwargs.items():
                    if key == "id":
                        self.id = arg
                    if key == "size":
                        self.size = arg
                    if key == "x":
                        self.x = arg
                    if key == "y":
                        self.y = arg

    def to_dictionary(self):
        """ Returns a dictionary representation of the Square Class """
        class_dict = {'id': self.id, 'size': self.width,
                      'x': self.x, 'y': self.y}
        return class_dict
