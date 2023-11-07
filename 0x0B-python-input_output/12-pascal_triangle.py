#!/usr/bin/python3
"""
12-pascal_triangle

This module defines a function to generate Pascal's triangle up to n rows.

Pascal's triangle is a mathematical triangle where each number is the t.
It starts with a single 1 at the top and continues to build downwards, numbers.


"""


def pascal_triangle(n):
    """
    Generates Pascal's triangle up to n rows.

    Args:
        n (int): The number of rows to generate.

    Returns:
        list of list of int: A list of lists representing Pascal's triangle.
    """
    if n <= 0:
        return []

    triangle = []

    for i in range(n):
        row = []
        for j in range(i + 1):
            if j == 0 or j == i:
                row.append(1)
            else:
                row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        triangle.append(row)

    return triangle
