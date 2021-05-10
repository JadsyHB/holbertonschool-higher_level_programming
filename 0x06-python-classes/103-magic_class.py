#!/usr/bin/python3
import math


class MagicClass:
    """Initializes and define are and circumference"""
    def __init__(self, radius=0):
        self.__radius = 0
        
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a numner")
        self.__radius = radius
        
    def area(self):
        """Calculate area"""
        return self.__radius ** 2 * math.pi
    
    def circumference(self):
        """Calculate curcumference"""
        return 2 * math.pi * self.__radius
