#!/usr/bin/python3
"""
This module contains the Square class.
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

        Raise a TypeError if value is not ame> must be an integer".
        Raise a ValueError if value is les"<name> must be greater than 0".
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


class Square(Rectangle):
    """
    Square class that inherits from Rectangle.
    """

    def __init__(self, size):
        """
        Initialize a Square with size.

        Args:
            size: The size of the square.
        """
        self.integer_validator("size", size)
        self.__size = size
       
    def __str__(self):
        """
        Return a string representation of the Square.
        """
        return "[Rectangle] {}/{}".format(self.__size, self.__size)
