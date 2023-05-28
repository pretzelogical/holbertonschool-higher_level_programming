#!/usr/bin/python3
"""Class with one method that raises an exception"""


class BaseGeometry:
    """One method"""
    def area(self):
        """Raises an exception"""
        raise Exception("area() is not implemented")
