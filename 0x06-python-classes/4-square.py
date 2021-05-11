#!/usr/bin/python3
"""
Module 4-square
Defines Square class with private attribute, size validation and area
accessible with setters and getters
"""


class Square:
    """
    class Square definition

    Args:
        size: size of side of square, default size is 0

    Functions:
        __init__self, size)
        size(self)
        size(self, value)
        area(self)
    """
    def __init__(self, size=0):
        """
        Initilization of square

        Attributes:
            size: size of side of square, default value is 0
        """
        self.size = size

    @property
    def size(self):
        """
        Getter
        Return: size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter
        Args:
        value: size is set to value when value is an int >= 0
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        Calculates are of a square

        Returns:
        area
        """
        return (self.__size)**2
