#!/usr/bin/python3
# Range for Lowercase alphabet in reverse
for i in range(122, 96, -1):
    # We use this condition for search every number and print it
    if i % 2 == 0:
        print("{:c}".format(i), end="")
    else:
        # We print the left letters in uppercase
        print("{:c}".format(i - 32), end="")
