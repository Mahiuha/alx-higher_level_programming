#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    arg = sys.argv

    sum = 0
    if len(arg) > 1:
        for i in arg:
            if i != arg[0]:
                sum += int(i)

    print("{}".format(sum))
