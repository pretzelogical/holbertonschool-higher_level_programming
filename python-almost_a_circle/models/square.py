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

    # getters and setters
    @property
    def size(self):
        """Getter for size"""
        return self.width

    @size.setter
    def size(self, value):
        """Setter for size"""
        self.input_validator("width", value)
        self.width = value
        self.height = value

    # methods
    def update(self, *args, **kwargs):
        """Updates the Square"""
        keys = ["id", "size", "x", "y"]
        if not args:
            for key, value in kwargs.items():
                if key in keys:
                    setattr(self, key, value)
        else:
            for idx, elem in enumerate(args):
                self.__setattr__(keys[idx], elem)

    def to_dictionary(self):
        """Returns the dictionary representation of the Square"""
        return {"id": self.id, "size": self.size, "x": self.x, "y": self.y}
