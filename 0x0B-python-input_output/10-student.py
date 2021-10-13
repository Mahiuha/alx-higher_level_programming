#!/usr/bin/python3
""" Student to JSON """


class Student:
    """ New class student """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is None:
            return (self.__dict__)
        else:
            dic = {}
            for nm in attrs:
                if hasattr(self, nm):
                    dic[nm] = getattr(self, nm)
            return (dic)
