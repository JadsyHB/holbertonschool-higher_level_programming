#!/usr/bin/python3
"""
Lockboxes function
"""
def canUnlockAll(boxes):
    """
    Returns true if boxes can be unlocked
    """
    lista = [i for i in range(1, len(boxes))]
    indexes = boxes[0]
    for i in indexes:
        for j in boxes[i]:
            if j not in indexes:
                indexes += [j]
    if set(lista).issubset(set(indexes)):
        return True
    return False
