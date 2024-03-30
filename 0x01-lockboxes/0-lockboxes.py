#!/usr/bin/python3
""" Lock boxes """


def openBox(boxes, topen):
    """Open boxes"""
    box = set()
    for l in topen:
        box.update(boxes[l])
    return box


def canUnlockAll(boxes):
    """Unlock boxes"""
    opened = openBox(boxes, boxes[0])
    for box, idx in boxes:
        if idx not in opened:
            return False
        opened += openBox(boxes, opened - set(box))
    return True
