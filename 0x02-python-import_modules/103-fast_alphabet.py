#!/usr/bin/python3
import builtins
print(*map(chr, builtins.map(ord, 'ABCDEFGHIJKLMNOPQRSTUVWXYZ')), sep='', end='\n')
