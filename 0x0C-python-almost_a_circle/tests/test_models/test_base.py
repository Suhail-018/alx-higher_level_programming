#!/usr/bin/python3
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
from unittest.mock import mock_open, patch


class TestBase(unittest.TestCase):
    def setUp(self):
        self.base1 = Base()
        self.base2 = Base()
        self.base = Base(5)
        self.rec1 = Rectangle(1, 3)
        self.rec2 = Rectangle(2, 4)
        print("working")

    def test_init_with_id(self):
        self.assertEqual(self.base.id, 5)

    def tearDown(self):
        # This method is called after each test method
        del self.base
        del self.base1
        del self.base2
        del self.rec1
        del self.rec2
        print("dine")

    def test_init_without_id(self):
        self.assertEqual(self.base1.id, 27)
        self.assertEqual(self.base2.id, 28)

    def test_to_json_string_empty_list(self):
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_to_json_string_with_dicts(self):
        dicts = [{'key1': 'value1'}, {'key2': 'value2'}]
        json_str = Base.to_json_string(dicts)
        self.assertEqual(json_str, '[{"key1": "value1"}, {"key2": "value2"}]')

    def test_to_json_string_with_none(self):
        self.assertEqual(Base.to_json_string(None), "[]")
    
    def test_save_to_file(self):
        with patch('builtins.open', mock_open()) as mock_file:
             Rectangle.save_to_file([self.rec1, self.rec2])

        # Assert that the file was opened in write mode with the correct filename
             mock_file.assert_called_once_with('Rectangle.json', mode='w')
        # Assert that the 'write' method of the file with the argument '[]'
             mock_file().write.assert_called_once_with('[{"id": 33, "width": 1, "height": 3, "x": 0, "y": 0}, {"id": 34, "width": 2, "height": 4, "x": 0, "y": 0}]')
    def test_from_json_string_empty_string(self):
        self.assertEqual(Base.from_json_string(""), [])

    def test_from_json_string_with_json(self):
        json_str = '[{"id": 1}, {"id": 2}]'
        dicts = Base.from_json_string(json_str)
        self.assertEqual(dicts, [{"id": 1}, {"id": 2}])

    def test_from_json_string_with_none(self):
        self.assertEqual(Base.from_json_string(None), [])

    def test_create_rectangle(self):
        rect_dict = {"id": 3, "width": 10, "height": 5, "x": 2, "y": 1}
        rect = Rectangle.create(**rect_dict)
        self.assertEqual(rect.id, 3)
        self.assertEqual(rect.width, 10)
        self.assertEqual(rect.height, 5)
        self.assertEqual(rect.x, 2)
        self.assertEqual(rect.y, 1)
        self.assertEqual(rect.__class__.__name__, "Rectangle")

    def test_create_square(self):
        square_dict = {"id": 4, "size": 7, "x": 3, "y": 2}
        square = Square.create(**square_dict)
        self.assertEqual(square.id, 4)
        self.assertEqual(square.size, 7)
        self.assertEqual(square.x, 3)
        self.assertEqual(square.y, 2)
        self.assertEqual(square.__class__.__name__, "Square")

if __name__ == "__main__":
    unittest.main()
