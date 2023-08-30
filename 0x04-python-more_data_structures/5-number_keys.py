#!/usr/bin/python3

def number_keys(a_dictionary):
    num_keys = len(a_dictionary)
    return num_keys

# Test the function
a_dictionary = { 'language': "C", 'number': 13, 'track': "Low level" }
nb_keys = number_keys(a_dictionary)
print("Number of keys: {:d}".format(nb_keys))
