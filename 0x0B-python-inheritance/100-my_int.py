#!/usr/bin/python3
"""
My Int class
"""


class MyInt(int):
    """
    rebel class
    """
    def __init__(self, number):
        """
        initialize
        """
        self.number = number

    def __eq__(self, other):
        """
        returns not equal
        """
        return self.number != other.number

    def __ne__(self, other):
        """
        returns equal
        """
        return self.number == other.number
