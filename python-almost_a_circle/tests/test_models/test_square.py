#!/usr/bin/python3
import unittest
from models.square import Square
"""Unit test for class Square"""


class TestSquare(unittest.TestCase):

    def test_create_instance(self):
        """Test instance creation"""
        s = Square(10, 3, 3, 5)
        self.assertEqual(s.width, 10)
        self.assertEqual(s.height, 10)
        self.assertEqual(s.x, 3)
        self.assertEqual(s.y, 3)
        self.assertEqual(s.id, 5)
        """Test instance creation with incorrect argument value"""
        self.assertRaises(ValueError, Square, -1)
        self.assertRaises(ValueError, Square, 1, 3, -5)
        """Test instance creation with incorrect argument type"""
        self.assertRaises(TypeError, Square, "str")
        self.assertRaises(TypeError, Square, 1, (2, 3))

    def test_str(self):
        """Test __str__ method"""
        s = Square(10, 3, 3, 5)
        self.assertEqual(str(s), "[Square] (5) 3/3 - 10")
