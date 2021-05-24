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
