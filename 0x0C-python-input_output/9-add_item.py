#!/usr/bin/python3
"""
add all arguments to python list
"""


from sys import argv
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file

file = load_from_json_file("add_item.json")
save_to_json_file(file + argv[1:], "add_item.json")
