#!/usr/bin/python3
"""
Module class to JSON
"""


def class_to_json(obj):
    """
    return JSON serialization
    """
    return obj.__dict__
