#!/usr/bin/python3
def remove_char_at(str, n):
    new = ""
    # Create counter for search the n
    i = 0
    for j in str:
        if i != n:
            # Copying in to the new string
            new = new + j
        i += 1
    return (new)
