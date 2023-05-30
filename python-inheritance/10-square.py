#!/usr/bin/python3
"""Class that represents a square (inherits Rectangle)"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Class that represents a square

    Args:
        Rectangle (class): inherited class from 9-rectangle
    """
    def __init__(self, size):
        """intialises size attribute

        Args:
            size (int): size of the square
            MUST be an int over 0
        """
        self.integer_validator("size", size)

        self.__size = size

    def area(self):
        """Returns the area of the square

        Returns:
            int: size times size is the area
        """
        return self.__size * self.__size
