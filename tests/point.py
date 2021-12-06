#!/usr/bin/env python3

import pygame
from pygame_tools import *
import unittest

class TestPoint(unittest.TestCase):
    def test_neg(self):
        self.assertEqual(-Point(1, 2), (-1, -2))
        self.assertEqual(-Point(-1, 0), (1, 0))
        self.assertEqual(-Point(-1, -1), (1, 1))

    def test_add(self):
        self.assertEqual(Point(1, 2) + 5, (6, 7))
        self.assertEqual(4 + Point(4, 2), (8, 6))
        self.assertEqual(Point(1, 2) + (2, 1), Point(3, 3))
        self.assertEqual((1, 2) + Point(2, 2), Point(3, 4))

    def test_sub(self):
        self.assertEqual(Point(3, 1) - 3, (0, -2))
        self.assertEqual(5 - Point(3, 2), (2, 3))
        self.assertEqual(Point(1, 2) - (2, 1), Point(-1, 1))
        self.assertEqual((4, 2) - Point(2, 1), Point(2, 1))

    def test_mul(self):
        self.assertEqual(Point(1, 2) * 3.1, Point(3.1, 6.2))
        self.assertEqual(2 *  Point(1, 3), Point(2, 6))
        self.assertEqual(Point(2, 3) * (3, 1), (6, 3))

    def test_div(self):
        self.assertEqual(Point(5, 4) / 2, Point(2.5, 2))
        self.assertEqual(10 /  Point(2, 4), Point(5, 2.5))
        self.assertEqual(Point(3, 2) / (2, 3), (3 / 2, 2 / 3))
        self.assertEqual((3, 1) / Point(4, 3), (3 / 4, 1 / 3))
        self.assertEqual(Point(5, 4) // 2, Point(2, 2))
        self.assertEqual(10 //  Point(2, 4), Point(5, 2))
        self.assertEqual(Point(3, 2) // (2, 3), (3 // 2, 2 // 3))
        self.assertEqual((3, 1) // Point(4, 3), (3 // 4, 1 // 3))

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
