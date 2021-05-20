#!/usr/bin/python3
"""
Defines class with no attributes
can only create first_name instance
"""


class LockedClass:
    """
    prevent user from making any other attributes
    other than first_name
    """
    __slots__ = "first_name"
