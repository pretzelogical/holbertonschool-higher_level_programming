#!/usr/bin/python3
"""Function that writes a string to a text file"""


def write_file(filename="", text=""):
    """Writes text to filename
    and return bytes written
    """
    with open(filename, 'w', encoding='utf-8') as f:
        return f.write(text)
