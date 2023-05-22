#!/usr/bin/python3
"""Square class with private size"""


class Square:
    """Square class that does not allow a value that is not an
    integer or less than zero to be assigned to __size"""
    def __init__(self, size=0):
        """Initalizes the size variable"""
        self.__size = size

    def area(self):
        """Gets the area of the Square

        Returns:
            int: __size * __size
        """
        return self.__size * self.__size

    @property
    def size(self):
        """Return the size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        """sets the size of the square

        Args:
            value (int): value representing the size of
            the square, MUST be a non-negative int

        Raises:
            TypeError: non integer type
            TypeError: negative integer
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise TypeError("size must be >= 0")
        else:
            self.__size = value

    def my_print(self):
        """Prints the square with the character #"""
        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end="")
            if i is not self.__size - 1:
                print()
        print()
