#!/usr/bin/env python3

import pygame
from pygame_tools import *

class RotateTest(GameScreen):

    def __init__(self):
        pygame.init()
        size = Point(600, 600)
        super().__init__(pygame.display.set_mode(size), size, size // 2)
        self.center = self.window_size // 2
        self.pos1 = self.center + self.center * (1, 0)
        self.pos2 = self.center + self.center * (2, 0)

    def update(self):
        super().update()
        pygame.draw.line(
            self.screen,
            'red',
            self.center,
            self.pos2,
        )
        pygame.draw.line(
            self.screen,
            'white',
            self.center,
            self.pos1,
        )
        self.pos1 = self.pos1.rotate(0.1, self.center)

    def key_down(self, event: pygame.event.Event):
        match event.unicode.lower():
            case 'a':
                self.pos2 = self.pos2.rotate(math.pi / 2, self.center)
            case 's':
                self.pos2 = self.pos2.rotate_ccw(math.pi / 2, self.center)

if __name__ == '__main__':
    RotateTest().run()
