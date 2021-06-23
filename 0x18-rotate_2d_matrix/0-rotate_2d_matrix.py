#!/usr/bin/python3
"""
rotate matrix
"""


def rotate_2d_matrix(m):
    """
    rotate in place
    """
    l = len(m)
    for i in range(l):
        for j in range(i+1,l):
            m[i][j], m[j][i] = m[j][i], m[i][j]
    for i in range(l//2):
        for j in range(l):
            m[j][i], m[j][l-i-1] = m[j][l-i-1],  m[j][i]
