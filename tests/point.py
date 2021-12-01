#!/usr/bin/env python3

import pygame
import sys
sys.path.append('/Users/shane/coding/python/pygame_tools/')
from src.pygame_tools import *
# from pygame_tools import *
import unittest

class TestPoint(unittest.TestCase):
    def test_add(self):
        self.assertEqual(Point(1, 2) + (2, 1), Point(3, 3))
        self.assertEqual((1, 2) + Point(2, 2), Point(3, 4))

    def test_sub(self):
        self.assertEqual(Point(1, 2) - (2, 1), Point(-1, 1))
        self.assertEqual((4, 2) - Point(2, 1), Point(2, 1))

    def test_mul(self):
        self.assertEqual(Point(1, 2) * 3, Point(3, 6))
        self.assertEqual(2 *  Point(1, 3), Point(2, 6))

    def test_div(self):
        self.assertEqual(Point(5, 4) / 2, Point(2.5, 2))
        self.assertEqual(10 /  Point(2, 4), Point(5, 2.5))
        self.assertEqual(Point(5, 4) // 2, Point(2, 2))
        self.assertEqual(10 //  Point(2, 4), Point(5, 2))

    def test_floor_ceil(self):
        p = Point(1.5, 2.5)
        self.assertEqual(math.floor(p), (1, 2))
        self.assertEqual(math.ceil(p), (2, 3))

    def test_eq(self):
        self.assertTrue(Point(1, 2) != Point(2, 3))
        self.assertTrue(Point(1, 2) == Point(1, 2))

    def test_distance(self):
        self.assertEqual(Point.distance((1, 1), (2, 2)), math.sqrt(2))

    def test_distance_from_line(self):
        self.assertEqual(Point.distance_from_line((0, 0), (1, 1), (0, 0)), 0)

if __name__ == '__main__':
    unittest.main()
