#!/usr/bin/env python3

import pygame
import sys
from pygame_tools import *
from random import randint

class CenterTextTest(GameScreen):

    def __init__(self):
        pygame.init()
        size = Point(600, 600)
        super().__init__(pygame.display.set_mode(size), size, (size.x // 2, size.y // 2))
        self.center = Point(self.window_size.x // 2, self.window_size.y // 2)
        self.input_box = InputBox(
            Rect(10, self.center.y, self.window_size.x - 20, self.center.y - 10),
            'grey',
            center_text = True
        )
        self.getting_input = False

    def key_down(self, event: pygame.event.Event):
        if self.getting_input:
            self.input_box.update(event)
            if self.input_box.done:
                print(self.input_box.get_value())
                self.input_box.reset()
                self.getting_input = False
        else:
            match event.unicode.lower():
                case 'i':
                    self.getting_input = True

    def update(self):
        super().update()
        if self.getting_input:
            self.input_box.draw(self.screen)

if __name__ == '__main__':
    CenterTextTest().run()
