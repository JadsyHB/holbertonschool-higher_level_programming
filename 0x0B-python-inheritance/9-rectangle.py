#!/usr/bin/python3
"""
Rectangle class inheriting from BaseGeometry
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    __init__(self, width, height)
    """
    def __init__(self, width, height):
        """
        width and height validated
        assigned as private values
        """
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """
        returns the area
        """
        return self.__width * self.__height

    def __str__(self):
        """
        prints string
        """
        return "[{:s}] {:d}/{:d}".format(self.__class__.__name__,
                                         self.__width, self.__height)
