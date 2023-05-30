#!/usr/bin/python3
"""Class that defines a rectangle"""


class Rectangle:
    """Class that represents a rectangle

    Attributes
    ----------
    height : Non-negative int
        height of the Rectangle
    width : Non-negative int
        width of the Rectangle
    ----------

    Methods
    -------
    __init__(self, width=0, height=0):
        Initializes all the rectangle attributes both private
        and with getter and setter functions

        Parameters
        ----------
        width : Non-negative int
            width of the Rectangle
        height : Non-negative int
            height of the Rectangle
        ----------

    area(self):
        Calculates and returns the area of the rectangle

    perimeter(self):
        Calculates and returns the area of the rectangle

    -------
    """
    def __init__(self, width=0, height=0):
        """Initialize the Rectangle object

        Args:
            width (int, optional): width of the rectangle.
            MUST be a non-negative integer. Defaults to 0.
            height (int, optional): height of the rectangle.
            MUST be a non-negative integer. Defaults to 0.
        """
        self.height = height
        self.width = width

    @property
    def height(self):
        """returns the private instance attribute __height

        Returns:
            int: height of Rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """sets the private instance attribute __height

        Args:
            value (int): Non-negative integer value

        Raises:
            TypeError: value was not an integer
            ValueError: value was a negative integer
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if not value >= 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def width(self):
        """returns the private instance attribute __width

        Returns:
            int: width of rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """sets the private instance attribute __height

        Args:
            value (int): Non-negative integer value

        Raises:
            TypeError: value was not an integer
            ValueError: value was a negative integer
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if not value >= 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    def area(self):
        """calculates the area of the rectangle

        Returns:
            int: area of the rectangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """calculates thhe perimeter of the rectangle

        Returns:
            int: perimeter of the rectangle
        """
        if (self.__width == 0
                or self.__height == 0):
            return 0

        return 2 * (self.__width + self.__height)
