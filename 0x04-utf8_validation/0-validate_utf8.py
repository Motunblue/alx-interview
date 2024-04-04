#!/usr/bin/python3
"""UFTF-8 Validation"""


def validUTF8(data):
    """Validate UTF-8 encoding"""
    seq_after = 0

    for byte in data:
        if byte < 128:  # Single-byte character
            if seq_after > 0:
                return False
        else:
            seq = byte // 128 + 1
            if seq_after == 0:
                if seq < 2 or seq > 4:
                    return False
                seq_after = seq - 1
            else:
                if seq != 1:
                    return False

            seq_after -= 1
            if seq_after < 0:
                return False
    return seq_after == 0
