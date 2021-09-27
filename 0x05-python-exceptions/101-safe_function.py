#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        func = fct(*args)

    except Exception as error:
        func = None
        sys.stderr.write("Exception: {}\n".format(error))

    return (func)
