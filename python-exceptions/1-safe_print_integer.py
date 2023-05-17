#!/usr/bin/python3


def safe_print_integer(value):
    """Prints an integer
    Returns True if succesful, else false"""
    try:
        print(":d".format(value))
        return True
    except (TypeError, ValueError):
        return False
