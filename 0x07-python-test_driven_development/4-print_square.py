#!/usr/bin/python3
"""
Module 4-print_square
"""


def print_square(size):
    """
    prints square with #
    """
    if isinstance(size, float) or not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size == 0:
        print("", end="")
    else:
        for i in range(size):
            print("#" * size)
