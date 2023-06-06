#!/usr/bin/python3
"""Base class for all other classes in the project"""
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries.

        Args:
            list_dictionaries (list): list of dictionaries

        Returns:
            string: JSON string representation of list_dictionaries
        """
        if not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """Return the list of the JSON representation"""
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to a file"""
        filename = cls.__name__ + ".json"
        with open(filename, 'w') as jsonfile:
            if list_objs is None:
                jsonfile.write('[]')
            else:
                list_dicts = [obj.to_dictionary() for obj in list_objs]
                jsonfile.write(Base.to_json_string(list_dicts))

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set"""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)  # type: ignore
        else:
            dummy = cls(1)
        dummy.update(**dictionary)  # type: ignore
        return dummy
