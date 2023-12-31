#!/usr/bin/python3
"""
This module contains the Rectangle class.
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

        Raise a TypeError if value is not an integer with the message".
        Raise a ValueError if value is less than or equal to 0 with the messag
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """
    Rectangle class that inherits from BaseGeometry.
    """

    def __init__(self, width, height):
        """
        Initialize a Rectangle with width and height.

        Args:
            width: The width of the rectangle.
            height: The height of the rectangle.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        Calculate and return the area of the Rectangle.

        Returns:
            The area of the rectangle (width * height).
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Return a string representation of the Rectangle.
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
