#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):

    def test_max_integer(self):
        
        self.assertEqual(max_integer([1, 3, 4]), 4)
        self.assertEqual(max_integer([9, 1, -7]), 9)
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer([1, 6, 5]), 6)
        self.assertEqual(max_integer([-1]), -1)
        self.assertEqual(max_integer([-2, -3, -9]), -2)
        self.assertEqual(max_integer([8]), 8)


if __name__ == '__main__':
   unittest.main()
