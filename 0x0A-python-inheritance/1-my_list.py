#!/usr/bin/python3
"""  New class """


class MyList(list):
    """ Mylist class that inherist from list """

    def print_sorted(self):
        """ Fucntion that prints a sorted list """
        print(sorted(self))
