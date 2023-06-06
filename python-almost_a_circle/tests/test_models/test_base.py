#!/usr/bin/python3
import unittest
from models.base import Base
from models.rectangle import Rectangle
"""Unit test for class Base
NOTE: 'type: ignore' comment is used to ignore errors in vscode
"""


class TestBase(unittest.TestCase):
    """Test class for class Base"""

    def test_create_instance_no_id(self):
        """Test if an instance can be created with no id
        without specifying an id
        """
        b = Base()
        self.assertTrue(hasattr(b, 'id'))

    def test_create_instance_with_id(self):
        """Test if an instance can be created with an id
        """
        b = Base(1337)
        self.assertEqual(b.id, 1337)

    def test_to_json_string(self):
        """Test if to_json_string returns a string
        with the JSON representation of an object
        """
        r1 = Rectangle(10, 7, 2, 8, 1)
        dictionary = r1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        self.assertEqual(
            dictionary,
            {'id': 1, 'width': 10, 'height': 7, 'x': 2, 'y': 8})
        self.assertEqual(
            json_dictionary,
            '[{"id": 1, "width": 10, "height": 7, "x": 2, "y": 8}]')
        self.assertEqual(type(json_dictionary), str)

    def test_from_json_string(self):
        """Test if from_json_string returns a list
        of dictionaries with the JSON representation of an object
        """
        list_input = [
            {'id': 89, 'width': 10, 'height': 4},
            {'id': 7, 'width': 1, 'height': 7}
        ]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list_input, list_output)
        self.assertEqual(type(list_output), list)

    def test_save_to_file(self):
        """Test if saving to a file works"""
        r0 = Rectangle(10, 7, 2, 8, 1)
        r1 = Rectangle(2, 4, 0, 0, 2)
        Rectangle.save_to_file([r0, r1])

        with open("Rectangle.json", 'r') as json_file:
            self.assertEqual(json_file.read(),
                             (
                '[{"id": 1, "width": 10, "height": 7, "x": 2'
                ', "y": 8}, {"id": 2, "width": 2, '
                '"height": 4, "x": 0, "y": 0}]'
            ))

    def test_create(self):
        """Test if create returns a list of instances
        the correct attributes set
        """
        r1 = Rectangle(3, 5, 1, 0, 0)
        r1_dict = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dict)
        self.assertEqual(r1.__str__(), r2.__str__())
        self.assertEqual(r1.id, r2.id)
        self.assertEqual(type(r1), type(r2))


if __name__ == "__main__":
    unittest.main()
