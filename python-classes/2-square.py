#!/usr/bin/python3
"""Square class with private size"""


class Square:
    """Square class that does not allow a value that is not an
    integer or less than zero to be assigned to __size"""
    def __init__(self, size=0):
        """Initalizes the the __size variable checking if it is an
        integer and less than zero

        Args:
            size (int, optional): size of square, MUST be an int that is
            not less than 0. Defaults to 0.

        Raises:
            ValueError: size is not an integer
            ValueError: size is < 0
        """
        if type(size) is not int:
            raise ValueError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
