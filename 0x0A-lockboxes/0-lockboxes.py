#!/usr/bin/python3
"""
Lockboxes function
"""


def canUnlockAll(boxes):
    """ determine if all boxes can be opened """
    for key in range(1, len(boxes) - 1):
        check = False
        for index in range(len(boxes)):
            check = key in boxes[index] and key != index
            if check:
                break
        if check is False:
            return check
    return True
