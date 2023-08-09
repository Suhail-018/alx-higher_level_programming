#!/usr/bin/python3
for char_code in range(ord('z'), ord('a') - 1, -1):
    char = chr(char_code)
    if char_code % 2 == 1:
        print("{}".format(char.upper()), end="")
    else:
        print("{}".format(char), end="")
