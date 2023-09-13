#!/usr/bin/python3

"""
This module provides a functio and returns the number of characters added.
"""


def append_write(filename="", text=""):
    """
    Appends a string to the ens the number of characters added.

    Args:
        filename (str): The name of the file to append to.
        text (str): The string to be appended to the file.

    Returns:
        int: The number of characters added to the file.
    """
    with open(filename, 'a', encoding='utf-8') as file:
        num_characters_added = file.write(text)
    return num_characters_added
