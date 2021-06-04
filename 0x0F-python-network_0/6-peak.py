#!/usr/bin/python3
"""
find peak module
"""


def find_peak(list_of_integers):
    """
    returns peak
    """
    l = list_of_integers
    leng = len(l)
    if leng == 0:
        return None
    max = 0
    for i in range(len(l) - 2):
        if l[i+1] >= l[i] and l[i+1] >= l[i+2]:
            max = l[i+1]
    return max
