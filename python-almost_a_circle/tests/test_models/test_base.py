#!/usr/bin/python3
import unittest
from models.base import Base
"""Unit test for class Base
NOTE: 'type: ignore' comment is used to ignore errors in vscode
"""


class TestBase(unittest.TestCase):
    """Test class for class Base"""
    def test_create_instance_no_id(self):
        """Test if an instance can be created with no id
        without specifying an id
        (and test Base._Base__nb_objects)
        """
        b = Base()
        self.assertEqual(b.id, 1)
        self.assertEqual(Base._Base__nb_objects, 1)  # type: ignore

    def test_create_instance_with_id(self):
        """Test if an instance can be created with an id
        (and test Base._Base__nb_objects)
        """
        b = Base(1337)
        self.assertEqual(b.id, 1337)
        self.assertEqual(Base._Base__nb_objects, 1)  # type: ignore


if __name__ == "__main__":
    unittest.main()
