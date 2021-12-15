#!/usr/bin/env python3

import pygame, unittest
from pygame_tools import *
from random import randint

class ManyOfTest(GameScreen):

    def __init__(self):
        pygame.init()
        size = Point(600, 600)
        super().__init__(pygame.display.set_mode(size), size, size // 2)
        self.text_box = ManyOf(
            TextBox,
            TextBox(
                ['this is text n1', 'This is the second text :)', 'THis is the final text'],
                Rect(0, self.window_size.y // 2, self.window_size.x, self.window_size.y // 2),
                pygame.Color(85, 85, 85),
                'white'
            ),
            TextBox(
                ['' for _ in range(3)],
                Rect(0, self.window_size.y // 2 - 10, self.window_size.x, 18),
                pygame.Color(17, 17, 17),
                border_radius = 0,
            ),
            TextBox(
                ['Title 1', 'A cool title', 'my boyf is hot'],
                Rect(0, self.window_size.y // 2 - 20, self.window_size.x, 20),
                pygame.Color(17, 17, 17),
                'white'
            )
        )

    def key_down(self, event: pygame.event.Event):
        self.text_box.update()

    def update(self):
        super().update()
        self.text_box.draw(self.screen)

class A:
    def add(self, a: int, b: int) -> int:
        return a + b

    def __str__(self):
        return 'This is an A object'

class ManyOfUnitTest(unittest.TestCase):
    m = ManyOf(A, A(), A(), A())
    def test_return(self):
        self.assertEqual(self.m.add(5, 6).obj_list, (11, 11, 11))

    def tests_dunder(self):
        str(self.m)
        repr(self.m)

if __name__ == '__main__':
    unittest.main()
    ManyOfTest().run()
