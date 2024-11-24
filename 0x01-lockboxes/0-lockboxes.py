#!/usr/bin/python3
"""Solving lockboxes problem"""


def unlock(boxes, idx, keys):
    """recursively unlocks the boxes"""
    keys.append(idx)
    for i in boxes[idx]:
        if i >= 0 and i < len(boxes) and i not in keys:
            unlock(boxes, i, keys)
    return


def canUnlockAll(boxes):
    """Returns true if every box is unlocked"""
    keys = []
    unlock(boxes, 0, keys)
    return (len(keys) == len(boxes))
