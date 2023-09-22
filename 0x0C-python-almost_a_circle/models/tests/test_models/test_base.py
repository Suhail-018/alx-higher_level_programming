#!/usr/bin/python3
import unittest
from ..base import Base
from ..rectangle import Rectangle
from ..square import Square


class TestBase(unittest.TestCase):
    def test_init_with_id(self):
        base = Base(5)
        self.assertEqual(base.id, 5)

    def test_init_without_id(self):
        base1 = Base()
        base2 = Base()
        self.assertEqual(base1.id, 1)
        self.assertEqual(base2.id, 2)

    def test_to_json_string_empty_list(self):
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_to_json_string_with_dicts(self):
        dicts = [{'key1': 'value1'}, {'key2': 'value2'}]
        json_str = Base.to_json_string(dicts)
        self.assertEqual(json_str, '[{"key1": "value1"}, {"key2": "value2"}]')

    def test_to_json_string_with_none(self):
        self.assertEqual(Base.to_json_string(None), "[]")

    def test_save_to_file(self):
        base1 = Base(1)
        base2 = Base(2)
        Base.save_to_file([base1, base2])
        with open("Base.json", "r") as file:
            json_str = file.read()
            self.assertEqual(json_str, '[{"id": 1}, {"id": 2}]')

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
