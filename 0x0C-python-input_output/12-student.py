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

    def to_json(self, attrs=None):
        """
        class to json
        """
        if attrs is None:
            return self.__dict__
        else:
            dic = {}
            for elem in attrs:
                if elem in self.__dict__.keys():
                    dic[elem] = self.__dic__[elem]
            return dic
