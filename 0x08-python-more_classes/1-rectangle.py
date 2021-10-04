#!/usr/bin/python3
"""
New class Rectangle
"""


class Rectangle:
    """ Defines a rectangle """

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    """ WIDTH """
    @property
    def width(self):
        return (self.__width)

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    """ HEIGHT """
    @property
    def height(self):
        return (self.__height)

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
