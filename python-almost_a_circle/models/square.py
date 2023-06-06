#!/usr/bin/python3
"""Module for a class that represents a Square
Inherits from rectangle.py
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Class that represents a Square
    """
    def __init__(self, size, x=0, y=0, id=None):
        """Initializes the Square"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """String representation of the Square"""
        return (f"[Square] ({self.id}) {self.x}/{self.y} - "
                + f"{self.width}")
