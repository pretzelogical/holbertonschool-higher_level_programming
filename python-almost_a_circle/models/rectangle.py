#!/usr/bin/python3
from models.base import Base
"""Class that represents a Rectangle"""


class Rectangle(Base):
    """Class that represents a Rectangle.

    Args:
        Base (Class): Helper class to keep track of instances
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes a Rectangle instance.

        Args:
            width (int): Width of the rectangle
            height (int): Height of the rectangle
            x (int): X coordinate of the rectangle
            y (int): Y coordinate of the rectangle
            id (int): Id of the rectangle
        """
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.x = x
        self.__y = y

    # getters and setters
    @property
    def x(self):
        """Get the private x attribute"""
        return self.__x

    @x.setter
    def x(self, value):
        """Set the private x attribute"""
        self.__x = value

    @property
    def y(self):
        """Get the private y attribute"""
        return self.__y

    @y.setter
    def y(self, value):
        """Set the private y attribute"""
        self.__y = value

    @property
    def width(self):
        """Get the private width attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the private width attribute"""
        self.__width = value

    @property
    def height(self):
        """Get the private height attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the private height attribute"""
        self.__height = value
