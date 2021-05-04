#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) is not str or roman_string is None:
        return None
    elif roman_string == "":
        return 0
    else:
        total = 0
        dic = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        for i in range(0, len(roman_string)-1):
            char1 = roman_string[i]
            char2 = roman_string[i+1]
            if char1 not in dic.keys():
                return 0
            elif dic[char1] < dic[char2]:
                total -= dic[char1]
            else:
                total += dic[char1]
        total += dic[roman_string[-1]]
        return total
