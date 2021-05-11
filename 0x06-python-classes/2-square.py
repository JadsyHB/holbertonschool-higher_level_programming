#!/usr/bin/python3
"""
Module 2-square
Defines class square with optional instantiation
"""

class Square:
    """
    class Square definition
    
    Args:
        size: size of side of square, default size is 0
    """
    def __init__(self, size=0):
        """
        Initilization of square
        
        Attributes:
            size: size of side of square, default value is 0
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
