#!/usr/bin/env python3

import pygame
from pygame_tools import *
from random import randint

class BezierTest(GameScreen):

    def __init__(self):
        pygame.init()
        size = Point(600, 600)
        super().__init__(pygame.display.set_mode(size), size, size // 2)
        self.center = self.window_size // 2

    def update(self):
        super().update()
        pygame.draw.lines(
            self.screen,
            'white',
            False,
            get_bezier_curve_points((0, self.window_size.y), (0, 0), self.get_scaled_mouse_pos(), 100)
        )

if __name__ == '__main__':
    BezierTest().run()
