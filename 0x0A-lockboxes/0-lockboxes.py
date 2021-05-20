#!/usr/bin/python3
"""
Lockboxes function
"""
def canUnlockAll(boxes):
    """
    Returns true if boxes can be unlocked
    """
    if not isinstance(boxes, list):
        return False
    lista = [i for i in range(1, len(boxes))]
    indexes = boxes[0]
    for i in indexes:
        if not isinstance(i, list):
            return False
        for j in boxes[i]:
            if j not in indexes:
                indexes += [j]
    if set(lista).issubset(set(indexes)):
        return True
    return False
