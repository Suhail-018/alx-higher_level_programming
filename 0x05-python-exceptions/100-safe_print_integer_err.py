#!/usr/bin/python3
import sys

def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))  # Print the integer value
    except ValueError as ve:
        print("Exception: {}".format(ve), file=sys.stderr)
        return False  # An exception oicand return False
    else:
        return True  # No exception occurred, so value is an integer
