#!/usr/bin/python3
""" New class """
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """ New class Rectangle that inherist from Base Geometry"""
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """ Print rectangle """
        return (self.__height * self.__width)

    def __str__(self):
        """ Return str """
        return("[{}] {}/{}".format(
            self.__class__.__name__, self.__width, self.__height))
