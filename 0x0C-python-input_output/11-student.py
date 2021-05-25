#!/usr/bin/python3
"""
Student class module
"""


class Student:
    """
    Args:
    first_name, last_name, age
    def __init__(self, first_name, last_name, age):
    def to_json(self):
    """
    def __init__(self, first_name, last_name, age):
        """
        initialization
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        class to json
        """
        return self.__dict__
