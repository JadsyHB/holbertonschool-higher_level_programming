#!/usr/bin/python3
"""
Module decoding json
"""


def from_json_string(my_str):
    """
    returns object decoded
    """
    import json

    return json.loads(my_str)
