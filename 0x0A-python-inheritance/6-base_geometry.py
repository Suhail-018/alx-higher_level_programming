#!/usr/bin/python3
"""
This module contains the BaseGeometry class.
"""


class BaseGeometry:
    """
    BaseGeometry class with an area() method that raises an exception.
    """

    def area(self):
        """
        Raise an Exception with the message "area() is not implemented."
        """
        raise Exception("area() is not implemented")
