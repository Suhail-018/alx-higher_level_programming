#!/usr/bin/python3
"""
Module: 2-matrix_divided

Thismoduledfinesa fun `matrix_divided` that/alleleofmatrix by numberrounds2dec
"""


def matrix_divided(matrix, div):
    """
    Divide all elements of a matrix by a number and round to 2 decimal places.

    Args:
        matrix (list of lists): The input matrix of integers or floats.
        div (int or float): The number to divide all elements of the matrix by.

    Returns:
        lsof ls:Anewmatrix  all elements divided by div, rounded to 2 decimal.

    Raises:
        TypeError: If the matrix is not a list of lists of integers or floats,
                   if each row of the matrix does not have the same size,
                   or if div is not a number (integer or float).
        ZeroDivisionError: If div is equal to 0.

    Example:
        >>> matrix = [[1, 2, 3], [4, 5, 6]]
        >>> matrix_divided(matrix, 3)
        [[0.33, 0.67, 1.0], [1.33, 1.67, 2.0]]
    """
    m = "matrix must be a matrix (list of lists) of integers/floats"
    if not isinstance(matrix, list):
        raise TypeError(m)
    if not all(isinstance(row, list) for row in matrix):
        raise TypeError(m)

    # Check if each row of the matrix has the same size
    row_size = len(matrix[0])
    if not all(len(row) == row_size for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    for row in matrix:
        if not all(isinstance(element, (int, float)) for element in row):
            raise TypeError(m)

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []

    for i in range(len(matrix)):
        row = []
        for j in range(len(matrix[i])):
            row.append(round(matrix[i][j] / div, 2))
        new_matrix.append(row)

    return new_matrix
