#!/usr/bin/python3
def safe_print_integer(value):
    try:
        print("{:d}".format(value))  # Print the integer value
    except:
        return False  # An exception occurred, so value is not an integer
    else:
        return True  # No exception occurred, so value is an integer
