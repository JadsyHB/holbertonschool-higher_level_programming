#!/usr/bin/python3
"""
Module 1-square
class Square defined with private attribute size
"""


class Square:
    """
    class Square

    Args:
        size: size of a side in a square
    """
    def __init__(self, size):
        """
        Initialization of square

        Attributes:
            size: size of a side of a square
        """
        self.__size = size
