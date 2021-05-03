#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if matrix is None:
        return None
    else:
        copy = []
        for i in matrix:
            copy.append(list(map(lambda x: x**2, i)))                
        return copy
