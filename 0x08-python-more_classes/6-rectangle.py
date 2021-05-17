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
    number_of_instances = 0

    @property
    def width(self):
        """
        Getter:
        returns width
        """
        return __width

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
        return __height

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
        type(self).number_of_instances += 1

    def area(self):
        """
        returns area
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        returns perimeter
        """
        if self.__height == 0 or self__.width == 0:
            return 0
        return 2 * self.width + 2 * self.height

    def __str__(self):
        """ print rectangle with # """
        if self.__width == 0 or self.__height == 0:
            return ""
        rec = "\n".join(["#" * self.__width for rows in range(self.__height)])
        return rec

    def __repr__(self):
        """string representation"""
        return "Rectangle({:d}, {:d})".format(self.width, self.height)

    def __del__(self):
        """message when delete"""
        print("Bye rectangle...")
        type(self).number_of_instances -= 1
