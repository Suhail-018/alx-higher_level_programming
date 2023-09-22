#!/usr/bin/python3
import unittest
from models.rectangle import Rectangle
from models.base import Base
import io
from unittest.mock import patch


class TestRectangle(unittest.TestCase):
    def setUp(self):
        self.Rectangle = None

    def test_init(self):
        rect1 = Rectangle(5, 7, 1, 1)
        self.assertEqual(rect1.width, 5)
        self.assertEqual(rect1.height, 7)
        self.assertEqual(rect1.x, 1)
        self.assertEqual(rect1.y, 1)

        with self.assertRaisesRegex(TypeError, r"width must be an integer"):
            Rectangle("w", 9)

        with self.assertRaisesRegex(ValueError, r"height must be > 0"):
            Rectangle(7, -2)

        with self.assertRaisesRegex(ValueError, r"x must be >= 0"):
            Rectangle(7, 8, -9)

    def test_area(self):
        rect1 = Rectangle(5, 7, 1, 1)
        self.assertEqual(rect1.area(), 35)

    def test_display(self):
        rect3 = Rectangle(2, 2)
        expected_output = "##\n##\n"
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            rect3.display()
            self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_display_with_coordinates(self):
        rect4 = Rectangle(2, 2, 2, 2)
        expected_output = "\n\n  ##\n  ##\n"
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            rect4.display()
            self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_str(self):
        r2 = Rectangle(5, 5, 1, 0)
        r2.id = 0
        expected_str = "[Rectangle] (0) 1/0 - 5/5"
        self.assertEqual(str(r2), expected_str)

    def test_update_with_args(self):
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(89, 20, 30, 40, 50)

        self.assertEqual(r1.id, 89)
        self.assertEqual(r1.width, 20)
        self.assertEqual(r1.height, 30)
        self.assertEqual(r1.x, 40)
        self.assertEqual(r1.y, 50)

    def test_update_with_kwargs(self):
        kwargs = {"x": 8, "height": 7, "y": 6, "width": 9}
        r6 = Rectangle(10, 10, 10, 10)
        r6.update(**kwargs)

        self.assertEqual(r6.width, 9)
        self.assertEqual(r6.height, 7)
        self.assertEqual(r6.x, 8)
        self.assertEqual(r6.y, 6)

if __name__ == "__main__":
    unittest.main()
