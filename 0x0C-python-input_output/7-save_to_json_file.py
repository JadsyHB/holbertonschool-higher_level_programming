#!/usr/bin/python3
"""
write object to text using json
"""


def save_to_json_file(my_obj, filename):
    """
    write to file using json
    """
    import json

    with open(filename, "w") as f:
        json.dump(my_obj, f)
