#!/usr/bin/python3


def no_c(my_string):
    """Removes all 'c' & 'C' characters from a string"""
    c_char = str.maketrans("", "", "cC")
    return my_string.translate(c_char)
