#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if matrix is None:
        return None
    else:
        return (list(map(lambda x: x**2, list)) for list in matrix)
