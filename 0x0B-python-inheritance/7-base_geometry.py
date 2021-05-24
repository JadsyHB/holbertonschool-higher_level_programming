#!/usr/bin/python3
"""
BaseGeometry class
"""


class BaseGeometry:
    """
    area(self) that raises error
    integer_validator(self, name, value)
    """
    def area(self):
        """
        raise error
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        validates value
        """
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
