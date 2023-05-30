#!/usr/bin/python3
"""Defines a Rectangle class that inherits from
the BaseGeometry class in 7-base_geometry
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Class that represents a rectangle

    Args:
        BaseGeometry (class): Class to inherit from
    """
    def __init__(self, width, height):
        """initalises width and height

        Args:
            width (int): integer value above 0
            height (int): integer value above 0
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height

    def area(self):
        """returns the area of the rectangle

        Returns:
            int: width * height = area
        """
        return self.__width * self.__height

    def __str__(self):
        """Returns the string representation of the rectangle

        Returns:
            string: string representation of the rectangle
        """
        return f"[Rectangle] {self.__width}/{self.__height}"
