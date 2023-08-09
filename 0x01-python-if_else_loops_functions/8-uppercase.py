#!/usr/bin/python3
def uppercase(s):
    result = ""
    for char in s:
        if 'a' <= char <= 'z':
            result += "{}".format(chr(ord(char) - ord('a') + ord('A')))
        else:
            result += "{}".format(char)
    print(result)
