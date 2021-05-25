#!/usr/bin/python3
"""
add all arguments to python list
"""


from sys import argv
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file

filename = "add_item.json"

try:
    content = load_from_json_file(filename)
except FileNotFoundError:
    content = []

save_to_json_file(content + argv[1:], filename)
