#!/usr/bin/python3
"""Base class for all other classes in the project"""


class Base:
    """Base class for all other classes in the project"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes the Base class

        Args:
            id (int, optional): id to be assigned to keep track
            of object if id is None increments __nb_objects by one
            and assigns it to the object id. Defaults to None.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
