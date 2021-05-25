#!/usr/bin/python3
"""
Module count lines
"""


def number_of_lines(filename=""):
    """
    returns number of lines
    """
    with open(filename, "r") as f:
        count = 0
        for line in f:
            count += 1
    return count
