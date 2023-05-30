#!/usr/bin/python3
"""Class that represents a student"""


class Student:
    """Class that represents a student"""
    def __init__(self, first_name, last_name, age):
        """Initalises values"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Returns __dict__ of self"""
        return self.__dict__
