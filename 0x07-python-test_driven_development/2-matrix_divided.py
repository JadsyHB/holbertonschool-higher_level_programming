#!/usr/bin/python3
"""
Module 2-matrix_divided
divides matrix (list of lists) by a number
"""


def matrix_divided(matrix, div):
    """
    returns matrix divided by the number div
    """
    if not isinstance(div, (float, int)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    err = "matrix must be a matrix (list of lists) of integers/floats"
    if type(matrix) is not list or len(matrix) == 0 or len(matrix[0]) == 0:
        raise TypeError(err)

    sameLen = len(matrix[0])
    new_matrix = []
    for i in matrix:
        if type(i) is not list:
            raise TypeError(err)
        if len(i) != sameLen:
            raise TypeError("Each row of the matrix must have the same size")
        new_list = []
        for elem in i:
            if not isinstance(elem, (int, float)):
                raise TypeError(err)
            new_list.append(round(elem/div, 2))
        new_matrix.append(new_list)
    return new_matrix
