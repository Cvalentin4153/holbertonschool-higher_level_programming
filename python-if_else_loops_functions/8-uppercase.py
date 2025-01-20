#!/usr/bin/python3

def uppercase(str):
    for c in str:
        if 97 <= ord(c) <= 122:
            c = chr(ord(c) - 32)
        print("{:s}".format(c), end="")
    print()
