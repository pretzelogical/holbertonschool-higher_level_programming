#!/usr/bin/python3
"""Defines a BaseGeometry class"""


class BaseGeometry:
    """BaseGeometry class"""
    def area(self):
        """TBA

        Raises:
            Exception: area has not been implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates value

        Args:
            name (str): name of the value
            value (int): integer value greater than zero

        Raises:
            TypeError: value was not an integer
            ValueError: value was less than or 0
        """
        if type(value) != int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
