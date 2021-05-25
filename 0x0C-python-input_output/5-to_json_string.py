#!/usr/bin/python3
"""
to json string module
"""


def to_json_string(my_obj):
    """
    return JSON representation
    """
    import json

    return json.dumps(my_obj)
