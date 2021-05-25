#!/usr/bin/python3
"""
module Rectangle
"""


from models.base import Base


class Rectangle(Base):
    """
    Attributes: __width, __height, __x, __y
    Functions: def __init__(self, width, height, x=0, y=0, id=None)
    getters and setters
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        initialization
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
        gets width
        """
        return self.__width

    @property
    def height(self):
        """
        gets height
        """
        return self.__height

    @property
    def x(self):
        """
        gets x
        """
        return self.__x

    @property
    def y(self):
        """
        gets y
        """
        return self.__y

    @width.setter
    def width(self, width):
        """
        sets width
        """
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @height.setter
    def height(self, height):
        """
        sets height
        """
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @x.setter
    def x(self, x):
        """
        sets x
        """
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @y.setter
    def y(self, y):
        """
        sets y
        """
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """
        returns area
        """
        return self.__width * self.__height

    def display(self):
        """
        print rectangle to stdout with #
        """
        print("\n" * self.__y +
              "\n".join(" " * self.__x + "#" * self.__width
                        for i in range(self.__height)))

    def __str__(self):
        """
        string representation
        """
        return "[{:s}] ({:d}) {:d}/{:d} - {:d}/{:d}".format(
            self.__class__.__name__, self.id, self.__x, self.__y,
            self.__width, self.__height)
