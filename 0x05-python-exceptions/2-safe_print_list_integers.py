#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    i = 0
    for elem in range(x):
        try:
            print("{:d}".format(my_list[elem]), end="")
            i += 1
        except (TypeError, ValueError):
            pass
    print()
    return (i)
