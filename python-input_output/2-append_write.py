#!/usr/bin/python3
"""Function that appends a string at the end of a text file"""


def append_write(filename="", text=""):
    """Appends a string to the end of a text file
    and return bytes written
    """
    with open(filename, 'a') as f:
        return f.write(text)
