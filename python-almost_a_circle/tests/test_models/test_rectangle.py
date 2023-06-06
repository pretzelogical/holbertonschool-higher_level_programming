#!/usr/bin/python3
from io import StringIO
import unittest
import sys
from unittest import mock
from models.rectangle import Rectangle
"""Unit test for class Rectangle
NOTE: 'type: ignore' comment is used to ignore errors in vscode
"""


class TestRectangle(unittest.TestCase):
    """Test class for class Rectangle"""

    def test_create_instance_no_id(self):
        """Test Rectangle instance creation with no id"""
        r0 = Rectangle(10, 15)
        self.assertEqual(r0.id, 2)
        self.assertEqual(r0.width, 10)
        self.assertEqual(r0.height, 15)
        self.assertEqual(Rectangle._Base__nb_objects, 2)  # type: ignore
        r1 = Rectangle(3, 2, 10, 15)
        self.assertEqual(r1.width, 3)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 10)
        self.assertEqual(r1.y, 15)
        self.assertEqual(Rectangle._Base__nb_objects, 3)  # type: ignore

    def test_create_instance_with_id(self):
        """Test Rectangle instance creation with id"""
        r = Rectangle(10, 10, 3, 4, 1337)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 10)
        self.assertEqual(r.x, 3)
        self.assertEqual(r.y, 4)
        self.assertEqual(r.id, 1337)
        self.assertEqual(Rectangle._Base__nb_objects, 3)  # type: ignore

    def test_getting_and_setting(self):
        """Test getter and setter methods"""
        r = Rectangle(10, 10, 3, 4, 1337)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 10)
        self.assertEqual(r.x, 3)
        self.assertEqual(r.y, 4)
        self.assertEqual(r.id, 1337)
        r.width = 20
        r.height = 30
        r.x = 40
        r.y = 50
        self.assertEqual(r.width, 20)
        self.assertEqual(r.height, 30)
        self.assertEqual(r.x, 40)
        self.assertEqual(r.y, 50)

    def test_area(self):
        """Test area method"""
        r = Rectangle(10, 10, 3, 4, 1337)
        self.assertEqual(r.area(), 100)
        r.width = 20
        r.height = 30
        self.assertEqual(r.area(), 600)

    def test_display(self):
        """Test display method"""
        r = Rectangle(3, 3)
        with mock.patch('sys.stdout', new=StringIO()) as fake_out:
            r.display()
            self.assertEqual(fake_out.getvalue(), "###\n###\n###\n")
        r = Rectangle(3, 3, 1, 1)
        with mock.patch('sys.stdout', new=StringIO()) as fake_out:
            r.display()
            self.assertEqual(fake_out.getvalue(), "\n ###\n ###\n ###\n")

    def test_error_raise(self):
        """Test conditions for error raising"""
        """Test incorrect type"""
        self.assertRaises(TypeError, Rectangle, 10, "10")
        self.assertRaises(TypeError, Rectangle, 10, 10, "str", 30)
        """Test incorrect value"""
        self.assertRaises(ValueError, Rectangle, 10, 0, 10, 20)
        self.assertRaises(ValueError, Rectangle, 10, 10, 0, -10)

    def test_update_method(self):
        """Test the update method"""
        """Test *args"""
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(89)
        self.assertEqual(r.id, 89)
        r.update(89, 2)
        self.assertEqual(r.width, 2)
        r.update(89, 2, 3)
        self.assertEqual(r.height, 3)
        r.update(89, 2, 3, 4)
        self.assertEqual(r.x, 4)
        r.update(89, 2, 3, 4, 5)
        self.assertEqual(r.y, 5)
        """Test **kwargs"""
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(width=2)
        self.assertEqual(r.width, 2)
        r.update(x=4)
        self.assertEqual(r.x, 4)
        r.update(y=5)
        self.assertEqual(r.y, 5)
        r.update(89, width=2)
        self.assertEqual(r.id, 89)
        """Test fail cases"""
        self.assertRaises(ValueError, r.update, 89, -2)
        self.assertRaises(ValueError, r.update, 89, 2, -3)
        self.assertRaises(ValueError, r.update, x=-1)
        self.assertRaises(TypeError, r.update, 89, "str")
        self.assertRaises(TypeError, r.update, width="the dollar")

    def test_str(self):
        """Test __str__ of rectangle"""
        r = Rectangle(3, 3, 9, 10, 9000)
        self.assertEqual(str(r), '[Rectangle] (9000) 9/10 - 3/3')
