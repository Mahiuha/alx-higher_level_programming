#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    a = list(set_2 - set_1)
    b = list(set_1 - set_2)
    return (a + b)
