#!/usr/bin/python3

"""
This module provides a functionumber of characters written.
"""


def write_file(filename="", text=""):
    """
    Writes a string to a text fiumber of characters written.

    Args:
        filename (str): The name of the file to write to.
        text (str): The string to be written to the file.

    Returns:
        int: The number of characters written to the file.
    """
    with open(filename, 'w', encoding='utf-8') as file:
        num_characters_written = file.write(text)
    return num_characters_written
