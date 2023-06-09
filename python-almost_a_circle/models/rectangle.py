#!/usr/bin/python3
"""Module for a class that represents a Rectangle.
Inherits from base.py
"""
from models.base import Base


class Rectangle(Base):
    """Class that represents a Rectangle.

    Args:
        Base (Class): Helper class to keep track of instances
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes a Rectangle instance.

        Args:
            width (int): Width of the rectangle. Must be int over 0
            height (int): Height of the rectangle. Must be int over 0
            x (int): X coordinate of the rectangle. Must be non-negative int
            y (int): Y coordinate of the rectangle. Must be non-negative int
            id (int): Id of the rectangle
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @staticmethod
    def input_validator(name, value):
        """Validates value according to name string

        Args:
            name (string): name of attribute to validate for
            value (int): integer to validate for

        Raises:
            ValueError: width/height was below or 0
            ValueError: x/y was below 0

        Returns:
            int: if validation successful the value,
            else nothing
        """
        if type(value) != int:
            raise TypeError(f"{name} must be an integer")
        if (name == "width" or
                name == "height"):
            if not value > 0:
                raise ValueError(f"{name} must be > 0")
            else:
                return value
        elif (name == "x" or
                name == "y"):
            if not value >= 0:
                raise ValueError(f"{name} must be >= 0")
            else:
                return value
        return

    # getters and setters
    @property
    def x(self):
        """Get the private x attribute.

        Returns:
            int: private x attribute.
        """
        return self.__x

    @x.setter
    def x(self, value):
        """Set the private x attribute.

        Args:
            value (int): value to set the private x attribute.
        """
        self.__x = self.input_validator("x", value)

    @property
    def y(self):
        """Get the private y attribute.

        Returns:
            int: private y attribute.
        """
        return self.__y

    @y.setter
    def y(self, value):
        """Set the private y attribute.

        Args:
            value (int): value to set the private y attribute.
        """
        self.__y = self.input_validator("y", value)

    @property
    def width(self):
        """Get the private width attribute.

        Returns:
            int: private width attribute.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Set the private width attribute.

        Args:
            value (int): value to set the private width attribute.
        """
        self.__width = self.input_validator("width", value)

    @property
    def height(self):
        """Get the private height attribute.

        Returns:
            int: private height attribute.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Set the private height attribute.

        Args:
            value (int): value to set the private height attribute.
        """
        self.__height = self.input_validator("height", value)

    # methods
    def area(self):
        """Returns the area of the rectangle.

        Returns:
            int: area of the rectangle
        """
        return self.__width * self.__height  # type: ignore

    def display(self):
        """Prints the rectangle in #'s to stdout."""
        if self.__width == 0 or self.__height == 0:
            return
        for i in range(self.__y):  # type: ignore
            print()
        for i in range(self.__height):  # type: ignore
            print(" " * self.__x, end="")  # type: ignore
            print("#" * self.__width)  # type: ignore

    def update(self, *args, **kwargs):
        """Update the Rectangle with the attribute and value
        if args is present use args else use kwargs
        """
        keys = ["id", "width", "height", "x", "y"]
        if not args:
            for key, value in kwargs.items():
                if key in keys:
                    self.__setattr__(key, value)
        else:
            for idx, elem in enumerate(args):
                self.__setattr__(keys[idx], elem)

    def to_dictionary(self):
        """Returns a dictionary representation of the Rectangle."""
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }

    def __str__(self):
        """Returns a string representation of the rectangle."""
        return (f"[Rectangle] ({self.id}) {self.x}/{self.y} "
                + f"- {self.width}/{self.height}")
