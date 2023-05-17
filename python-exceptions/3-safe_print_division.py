#!/usr/bin/python3


def safe_print_division(a, b):
    """Divides two integers and prints the result
    in the finally clause"""
    out = None
    try:
        out = a / b
    except (TypeError, ZeroDivisionError):
        return out
    finally:
        print("Inside result: {}".format(out))
    return out
