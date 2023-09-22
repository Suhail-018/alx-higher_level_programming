#!/usr/bin/python3
import unittest
from models.square import Square
from models.rectangle import Rectangle
from models.base import Base

class TestSquare(unittest.TestCase):
    def setUp(self):
        self.square1 = Square(5)
        self.square1.id = 1

    def tearDown(self):
        del self.square1

    def test_init(self):
        self.assertEqual(self.square1.size, 5)
        self.assertEqual(self.square1.x, 0)
        self.assertEqual(self.square1.y, 0)
        self.assertEqual(self.square1.id, 1)

        square2 = Square(3, 1, 2, 7)
        self.assertEqual(square2.size, 3)
        self.assertEqual(square2.x, 1)
        self.assertEqual(square2.y, 2)
        self.assertEqual(square2.id, 7)

    def test_size_setter_getter(self):
        square = Square(4)
        square.size = 7
        self.assertEqual(square.size, 7)

        with self.assertRaises(ValueError):
            square.size = -2

        with self.assertRaises(TypeError):
            square.size = "string"

    def test_str(self):
        square = Square(3, 2, 1, 8)
        expected_output = "[Square] (8) 2/1 - 3"
        self.assertEqual(str(square), expected_output)

    def test_update_with_args(self):
        square = Square(5, 2, 3, 9)
        square.update(7, 4, 1, 8)

        self.assertEqual(square.id, 7)
        self.assertEqual(square.size, 4)
        self.assertEqual(square.x, 1)
        self.assertEqual(square.y, 8)

    def test_update_with_kwargs(self):
        square = Square(5, 2, 3, 9)
        square.update(id=7, size=4, x=1, y=8)

        self.assertEqual(square.id, 7)
        self.assertEqual(square.size, 4)
        self.assertEqual(square.x, 1)
        self.assertEqual(square.y, 8)

    def test_to_dictionary(self):
        square = Square(4, 2, 3, 7)
        expected_dict = {
            "id": 7,
            "size": 4,
            "x": 2,
            "y": 3
        }
        self.assertEqual(square.to_dictionary(), expected_dict)

if __name__ == "__main__":
    unittest.main()
