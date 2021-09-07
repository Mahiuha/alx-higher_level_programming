#!/usr/bin/python3
def print_last_digit(number):
    last = int(repr(number)[-1])
    print("{:d}".format(last), end="")
    return (last)
