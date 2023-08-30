#!/usr/bin/python3

def simple_delete(a_dictionary, key=""):
    if key in a_dictionary:
        del a_dictionary[key]
    return a_dictionary

# Function to print a sorted dictionary
def print_sorted_dictionary(a_dictionary):
    sorted_keys = sorted(a_dictionary.keys())
    for key in sorted_keys:
        print("{}: {}".format(key, a_dictionary[key]))
