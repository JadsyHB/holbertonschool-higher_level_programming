#!/usr/bin/python3
def number_keys(a_dictionary):
    if a_dictionary is None:
        return 0
    else:
        return len(a_dictionary.keys())
