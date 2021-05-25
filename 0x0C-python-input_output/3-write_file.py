#!/usr/bin/python3
"""
Module write to file
"""


def write_file(filename="", text=""):
    """
    write into file
    """
    with open(filename, "w") as f:
        f.write(text)
