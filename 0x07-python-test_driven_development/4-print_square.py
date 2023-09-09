#!/usr/bin/python3
"""
Module: 4-print_square

This module defines a function `print_square` that prints a squarewithchar'#'.
"""

def print_square(size):
    """
    Prints a square with the character #.

    Args:
        size (int): The size (side length) of the square.

    Raises:
        TypeError: If size is not an integer or if it's a float less than 0.
        ValueError: If size is less than 0.

    Example:
        >>> print_square(4)
        ####
        ####
        ####
        ####

        >>> print_square(10)
        ##########
        ##########
        ##########
        ##########
        ##########
        ##########
        ##########
        ##########
        ##########
        ##########

        >>> print_square(0)
        (no output)

        >>> print_square(1)
        #

        >>> print_square(-1)
        Traceback (most recent call last):
            ...
        ValueError: size must be >= 0
    """
    if not isinstance(size, int):
        if isinstance(size, float) and size.is_integer() and size >= 0:
            size = int(size)
        else:
            raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for _ in range(size):
        print("#" * size)
