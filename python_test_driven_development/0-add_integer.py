#!/usr/bin/python3


def add_integer(a, b=98):
    if type(a) is not float or int:
        raise TypeError("a must be an integer")
    if type(b) is not float or int:
        raise TypeError("b must be an integer")

    a, b = int(a), int(b)

    return a + b
