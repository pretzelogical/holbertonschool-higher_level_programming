#!/usr/bin/python3
"""Class that represents a student"""


class Student:
    """Class that represents a student"""
    def __init__(self, first_name, last_name, age):
        """Initalises values"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """if attrs is not a list returns __dict__ of self
        else: returns only elements listed in attrs
        """
        out = dict()
        if type(attrs) is list:
            for attr in attrs:
                if type(attr) is not str:
                    return self.__dict__

                if attr in self.__dict__:
                    out[attr] = self.__dict__[attr]
            return out
        return self.__dict__

    def reload_from_json(self, json):
        """Replaces all attributes with json (dict)"""
        for name in json:
            if name in self.__dict__.keys():
                self.__dict__[name] = json[name]
