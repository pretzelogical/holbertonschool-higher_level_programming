#!/usr/bin/python3
import unittest
from models.rectangle import Rectangle
"""Unit test for class Rectangle
NOTE: 'type: ignore' comment is used to ignore errors in vscode
"""


class TestRectangle(unittest.TestCase):
    """Test class for class Rectangle"""

    def test_create_instance_no_id(self):
        """Test Rectangle instance creation with no id"""
        r0 = Rectangle(0, 1)
        self.assertEqual(r0.id, 2)
        self.assertEqual(r0.width, 0)
        self.assertEqual(r0.height, 1)
        self.assertEqual(Rectangle._Base__nb_objects, 2)  # type: ignore
        r1 = Rectangle(3, 2, 10, 15)
        self.assertEqual(r1.width, 3)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 10)
        self.assertEqual(r1.y, 15)
        self.assertEqual(Rectangle._Base__nb_objects, 3)  # type: ignore

    def test_create_instance_with_id(self):
        """Test Rectangle instance creation with id"""
        r = Rectangle(10, 10, id=1337)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 10)
        self.assertEqual(r.id, 1337)
