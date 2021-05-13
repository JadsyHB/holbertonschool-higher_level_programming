#!/usr/bin/python3
"""
Module 3-say_my_name
prints your name
"""


def say_my_name(first_name, last_name=""):
    """
    prints the name by the elements given
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    elif not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    else:
        print("My name is {:s} {:s}".format(first_name, last_name))
