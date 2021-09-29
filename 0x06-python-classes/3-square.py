#!/usr/bin/python3
"""
New class Square
"""


class Square:
    """ Defines a Square """
    def __init__(self, size=0):
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """ Define area of square"""
        return (self.__size ** 2)
