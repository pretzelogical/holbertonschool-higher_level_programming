#!/usr/bin/python3


def normalise_tuple(tuple=()):
    """Checks if tuple is smaller than two (or empty)
    and if so returns a normalised copy"""
    if len(tuple) is 1:
        return (tuple[0], 0)
    if len(tuple) is 0:
        return(0, 0)
    return tuple


def add_tuple(tuple_a=(), tuple_b=()):
    """Adds tuple_a & tuple_b only using the first
    two elements.
    If tuple is smaller than 2, 0 will be substitued
    for the missing integer"""
    a = normalise_tuple(tuple_a)
    b = normalise_tuple(tuple_b)
    return (a[0] + b[0], a[1] + b[1])
