#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if matrix is None:
        return None
    else:
        return[[elem**2 in row] for row in matrix]
