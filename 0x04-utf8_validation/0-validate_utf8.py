#!/usr/bin/python3
"""
determines if a given data set represents a valid UTF-8 encoding."""


def validUTF8(data):
    """utf validating function"""
    metadata = {
                    '0': 0,
                    '110': 1,
                    '1110': 2,
                    '11110': 3
                }
    sbsqnt_byte = 0

    for char in data:
        bin = []
        header = ""

        for i in range(8):
            bin.append(char & 1)
            char >>= 1
        bin.reverse()

        for i in range(5):
            header += str(bin[i])
            if bin[i] == 0:
                break

        if header[-1] != '0':
            return False

        if sbsqnt_byte == 0:
            if header not in metadata.keys():
                return False
            sbsqnt_byte = metadata[header]

        elif sbsqnt_byte:
            if header != '10':
                return False
            sbsqnt_byte -= 1

    return True
