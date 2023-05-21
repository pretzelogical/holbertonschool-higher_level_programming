#!/usr/bin/python3
"""Simple square class with private variable"""


class Square:
    """Square with private size variable"""
    def __init__(self, size):
        """Initializes a square with a private size variable

        Args:
            size (int): variable to be assigned to __size
        """
        self.__size = size
