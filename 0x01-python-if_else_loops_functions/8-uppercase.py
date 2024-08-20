#!/usr/bin/python3
def uppercase(str):
    for c in str:
        item = c
        if ord(c) >= 97 and ord(c) <= 123:
            item = chr(ord(c) - 32)
        print("{}".format(item), end='')
    print()
