#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        c = a / b

    except (ZeroDivisionError, TypeError, ValueError):
        c = None

    finally:
        print("Inside result: {}".format(c))

    return (c)
