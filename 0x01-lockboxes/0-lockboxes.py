#!/usr/bin/python3
"""Solving lockboxes problem"""


def canUnlockAll(boxes):
    """Returns true if every box is unlocked"""
    keys = []
    unlocked = [0]
    for i in unlocked:
        for j in boxes[i]:
            if j not in unlocked and j < len(boxes):
                unlocked.append(j)
    return(len(unlocked) == len(boxes))
