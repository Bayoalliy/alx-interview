#!/usr/bin/python3
"""
determines if a given data set represents a valid UTF-8 encoding."""


def validUTF8(data):
    """utf-8 validating function"""
    for ch in data:
        i = 0
        tmp_ch = ch
        while ch > 0:
            ch >>= 1
            i += 1
        ch = tmp_ch
        if ch < 128:
            continue
        elif ch < 2048 and i != 16:
            return False
        elif ch < 65536 and i != 24:
            return False
        elif ch > 65535 and i != 32:
            return False

    return True
