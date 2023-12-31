#!/usr/bin/python3
"""
This module contains the inherits_from function.
"""


def inherits_from(obj, a_class):
    """
    Check if an object is an instance of a class that inherited.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        True if obj is an instance of a subclass of a_class; otherwise, False.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
