#!/usr/bin/python3
"""
create object from JSON file
"""


def load_from_json_file(my_obj, filename):
    """
    create object from json file
    """
    import json

    with open(filename, "r") as f:
        return json.load(f)
