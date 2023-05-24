#!/usr/bin/python3
"""add two integers """

def add_integer(a, b=98):
    """Returns the integer addition of a + b

    Args:
        a (int): first operand
        b (int, optional): second operand. Defaults to 98.

    Raises:
        TypeError: a was not a float or an integer
        TypeError: b was not a floar or an integer

    Returns:
        int: integer addition of a + b
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")

    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
