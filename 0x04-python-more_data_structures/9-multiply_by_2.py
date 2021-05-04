#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    if a_dictionary is None:
        return None
    else:
        new_dict = {}
        for key, value in a_dictionary.items():
            new_dict[key] = value*2
        return new_dict
