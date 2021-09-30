#!/usr/bin/python3
"""
    Module containing ``say_my_name``` function.
"""


def say_my_name(first_name, last_name=""):
    """ Function prints `first_name` and `last_name`

    Args:
        first_name (string): First name.
        last_name (string): Last name.
    """

    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is {:s} {:s}".format(first_name, last_name))
