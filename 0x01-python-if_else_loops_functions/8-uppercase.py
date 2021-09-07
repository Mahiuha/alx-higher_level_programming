#!/usr/bin/python3
def uppercase(str):
    for i in str:
        convr = ord(i)
        if convr in range(97, 123):
            convr = convr - 32
        print("{:c}".format(convr), end="")
    print()
