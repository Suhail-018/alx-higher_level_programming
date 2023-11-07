#!/usr/bin/python3

"""
This module provides a function to read and print file (UTF8) to stdout.
"""


def read_file(filename=""):
    """
    Reads a text file (UTF8) and prints its contents to stdout.

    Args:
        filename (str): The name of the file to read.
    """
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            print(line, end='')
