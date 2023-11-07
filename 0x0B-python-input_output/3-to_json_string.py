#!/usr/bin/python3

"""
This module provides a functionto its JSON representation (string).
"""

import json


def to_json_string(my_obj):
    """
    Converts an object to its JSON representation (string).

    Args:
        my_obj: The object to be converted to JSON.

    Returns:
        str: The JSON representation of the object.
    """
    return json.dumps(my_obj)
