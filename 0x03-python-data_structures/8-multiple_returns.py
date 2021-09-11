#!/usr/bin/python3
def multiple_returns(sentence):
    lenght = len(sentence)
    if lenght > 0:
        first = sentence[0]
    else:
        first = None
    return (lenght, first)
