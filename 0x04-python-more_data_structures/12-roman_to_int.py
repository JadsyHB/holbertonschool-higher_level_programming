#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) is not str or roman_string is None:
        return None
    elif roman_string == "":
        return 0
    else:
        
