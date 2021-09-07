#!/usr/bin/python3
# We use i for the first digit and j for the second
for i in range(0, 9):
    for j in range(i + 1, 10):
        if i is not 8 or j is not 9:
            print("{:d}{:d}".format(i, j), end=", ")
        else:
            print("{:d}{:d}".format(i, j))
