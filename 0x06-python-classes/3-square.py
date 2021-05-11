#!/usr/bin/python3
"""
Module 3-square
Defines Square class with private attribute, size validation and area
"""


class Square:
    """
    class Square definition

    Args:
        size: size of side of square, default size is 0

    Functions:
        __init__self, size)
        area(self)
    """
    def __init__(self, size=0):
        """
        Initilization of square

        Attributes:
            size: size of side of square, default value is 0
        """
        if size < 0:
            raise ValueError("size must be >= 0")
        elif type(size) is not int:
            raise TypeError("size must be an integer")
        else:
            self.__size = size

    def area(self):
        """
        Calculates are of a square
    
        Returns:
            area
        """
        return (self.__size)**2
