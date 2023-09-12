#!/usr/bin/python3
"""
This module contains the is_kind_of_class function.
"""


def is_kind_of_class(obj, a_class):
    """
    Check if an object is an instancenherited from, the specified class.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        True if objan instance of a_class or its subclass; otherwise, False.
    """
    return isinstance(obj, a_class)
