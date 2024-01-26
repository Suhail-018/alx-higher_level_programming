#!/usr/bin/python3
"""Finds a peak in a list of unsorted integers
"""


def find_peak(list_of_integers):
    """Finds a peak in a list of unsorted integers
    """

    if type(list_of_integers) is not list:
        return (None)

    li_length = len(list_of_integers)
    if li_length == 0:
        return (None)

    list_of_integers.sort()
    return (list_of_integers[-1])
