#!/usr/bin/python3
"""
validate utf-8
"""


def validUTF8(data):
    """
    returns boolean
    """
    bytes = 0
    for num in data:
        if num < 128:
            bytes += 1
        else:
            binary = format(num, '08b')
            if bytes == 0:
                for bit in binary:
                    if bit == "0":
                        break
                    bytes += 1
                if bytes > 4:
                    return False
            else:
                if binary[0] != "1" and binary[1] != "0":
                    return False
        bytes -= 1
    return bytes == 0
