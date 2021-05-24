#!/usr/bin/python3
"""
module inherits from
"""


def inherits_from(obj, a_class):
    """
    return True if subclass from class
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
