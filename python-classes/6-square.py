#!/usr/bin/python3
"""Square class with private size and position"""


class Square:
    """Square class that does not allow a value that is not an
    integer or less than zero to be assigned to __size
    """

    def __init__(self, size=0, position=(0, 0)):
        """Initializes the private size and position variables

        Args:
            size (int, optional): MUST be a positive int. Defaults to 0.
            position (tuple, integer, optional): MUST be two positive ints.
                                                    Defaults to (0, 0).
        """
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        """Returns the position of the square"""
        return self.__position

    @position.setter
    def position(self, value):
        if type(value) is not tuple:
            raise TypeError("position must be a tuple of 2 positive integers")

        if len(value) is not 2:
            raise TypeError("position must be a tuple of 2 positive integers")

        if ((type(value[0]) is not int
                and type(value[1]) is not int)
                or (value[0] < 0
                    and value[1] < 0)):
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = value

    def my_print(self):
        """Prints the square
        size ** 2 = amount of #
        position[0] = amount of ' ' before #
        position[1] = amount of '\n' before square
        """
        print("\n" * self.__position[1])
        for i in range(self.__size):
            print(" " * self.__position[0], end="")
            print("#" * self.__size, end="")
            if i is not self.__size - 1:
                print()
        print()
