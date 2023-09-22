import unittest
from unittest.mock import patch
from models.rectangle import Rectangle
from models.base import Base
import io

class TestRectangle(unittest.TestCase):
    # ... other test methods ...

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
