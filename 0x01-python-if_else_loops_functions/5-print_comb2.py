#!/usr/bin/python3
for i in range(00, 100):
    if i is not 99:
        print("{:02d}".format(i), end=", ")
    else:
        print("{:02d}".format(i))
