#!/usr/bin/python3
"""
Module 1-rectangle
"""


class Rectangle:
    """
    Defines class rectangle with width and height
    Args:
    width and height
    Functions:
    __init__(self, width, height)
    width(self)
    width(self, value)
    height(self)
    height(self, value)
    """
    @property
    def width(self):
        """
        Getter:
        returns width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        sets width to the value
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Getter:
        Returns height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter:
        sets height to value
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def __init__(self, width=0, height=0):
        """
        Initializes rectangle
        """
        self.width = width
        self.height = height
