#!/usr/bin/python3
"""
This module contains the BaseGeometry class.
"""

class BaseGeometry:
    """
    BaseGeometry class with area() and integer_validator methods.
    """

    def area(self):
        """
        Raise an Exception with the message "area() is not implemented."
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validate the value:
        - name: A string representing the name of the value.
        - value: The value to validate.

        Raise a TypeError if valueis not an integer with the messageer".
        Raise a ValueError if value is less than or equal to 0 with an 0".
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
