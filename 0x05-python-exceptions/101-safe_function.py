#!/usr/bin/python3
import sys

def safe_function(fct, *args):
    try:
        result = fct(*args)  # Call the provided functi given arguments
    except Exception as e:
        print("Exception:", e, file=sys.stderr)
        return None  # An exception occurred, print then None
    else:
        return result  # No exception occurred, return 
