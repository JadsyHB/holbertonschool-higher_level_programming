#!/usr/bin/python3
"""
Module count lines
"""


def number_of_lines(filename=""):
    """
    returns number of lines
    """
    with open(filename, "r") as f:
        return len(f.readLines())
