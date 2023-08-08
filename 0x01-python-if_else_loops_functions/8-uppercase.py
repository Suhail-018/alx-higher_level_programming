#!/usr/bin/python3
def uppercase(s):
 for char in s:
     if 'a' <= char <= 'z':
            print(chr(ord(char) - ord('a') + ord('A')), end="")
     else:
            print(char, end="")
print()  
