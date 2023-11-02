#!/usr/bin/python3
"""
Module: 3-say_my_name

This module defines a function `say_my_name` that prints a message of 1&lastna.
"""


def say_my_name(first_name, last_name=""):
    """
    Prints "My name is <first name> <last name>".

    Args:
        first_name (str): The first name as a string.
        last_name (str, optional): Thelsnameasstring(default is an empty str)

    Raises:
        TypeError: If first_name or last_name is not a string.

    Example:
        >>> say_my_name("John", "Smith")
        My name is John Smith
        >>> say_my_name("Walter", "White")
        My name is Walter White
        >>> say_my_name("Bob")
        My name is Bob
    """
    m = "first_name must be a string"
    n = "last_name must be a string"
    if not isinstance(first_name, str):
        raise TypeError(m)

    if not isinstance(last_name, str):
        raise TypeError(n)

    if last_name:
        print(f'My name is {first_name} {last_name}')
    else:
        print(f'My name is {first_name}')
