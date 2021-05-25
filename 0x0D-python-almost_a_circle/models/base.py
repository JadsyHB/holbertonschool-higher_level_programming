#!/usr/bin/python3
"""
Base module
"""


class Base:
    """
    Base class
    Attributes: __nb_objects
    Functions: def __init__(self, id=None)
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        initialization
        """
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id
