#!/usr/bin/python3
def no_c(my_string):
    remove = ""
    for i in my_string:
        if i != 'c' and i != 'C':
            remove += i
    return (remove)
