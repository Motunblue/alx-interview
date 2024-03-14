#!/usr/bin/python3
"""Lock boxes"""

def openBox(boxes, idx, opened):
  """Open box"""
  if (idx > (len(boxes)) - 1):
    return True
  if (idx not in opened):
    return False
  opened.update(boxes[idx])
  return True and openBox(boxes, idx + 1, opened)


def canUnlockAll(boxes):
  """Unlock boxes"""
  opened = set(boxes[0])
  return openBox(boxes, 1, opened)
