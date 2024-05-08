#!/usr/bin/python3
"""UFTF-8 Validation"""


def validUTF8(data):
    """Validate if data is a valid UTF-8 char sequence"""
    num_bytes = 0
    
    for byte in data:
      if num_bytes == 0: #start of sequence or single character
        if byte >> 7 == 0b0:
          num_bytes = 0
        elif byte >> 5 == 0b110:
          num_bytes = 1
        elif byte >> 4 == 0b1110:
          num_bytes = 2
        elif byte >> 3 == 0b11110:
          num_bytes = 3
        else:
          return False
      else:
        if byte >> 6 != 0b10:
          return False
        num_bytes -= 1

    if num_bytes != 0:
      return False
    
    return True
    