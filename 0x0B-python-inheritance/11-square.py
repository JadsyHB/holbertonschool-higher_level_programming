#!/usr/bin/python3
"""
Method Square
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    class square that inherits from Rectangle
    """
    def __init__(self, size):
        """
        Args: size
        """
        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """
        returns area
        """
        return self.__size ** 2

    def __str__(self):
        """
        prints string
        """
        return "[{:s}] {:d}/{:d}".format(self.__class__.__name__,
                                         self.__size, self.__size)
