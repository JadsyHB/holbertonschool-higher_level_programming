#!/usr/bin/python3
"""
module pascal triangle
"""


def pascal_triangle(n):
    """
    return list of lists
    """
    pascal = []
    if n <= 0:
        return pascal
    else:
        for row in range(n+1):
            subset = [1]
            for column in range(1, row):
                subset.append(pascal[row-1][column-1] + pascal[row-1][column])
            if row != 0:
                subset.append(1)
            pascal.append(subset)
        return pascal
