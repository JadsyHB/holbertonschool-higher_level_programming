#!/usr/bin/python3
"""
Module append to file
"""


def append_write(filename="", text=""):
    """
    append into file
    """
    with open(filename, "a") as f:
        f.write(text)
    return len(text)
