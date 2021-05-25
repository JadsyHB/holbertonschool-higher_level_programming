#!/usr/bin/python3
"""
Module 0, read file
"""


def read_file(filename=""):
    """
    read file and print it to stdout
    """
    with open(filename, "r") as f:
        print(f.read(), end="")
