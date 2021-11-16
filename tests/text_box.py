#!/usr/bin/env python3

import pygame
import sys
from pygame_tools import *
from random import randint

class TextBoxTest(GameScreen):

    def __init__(self):
        pygame.init()
        size = Point(600, 600)
        super().__init__(pygame.display.set_mode(size), size, (size.x // 2, size.y // 2))
        self.center = Point(self.window_size.x // 2, self.window_size.y // 2)
        self.text_box = TextBox(
            [
                "Hello world! Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet.",
                "This is the second slide",
                'Third slide!!!',
            ],
            Rect(10, self.center.y, self.window_size.x - 20, self.center.y - 10),
            'grey'
        )

    def key_down(self, _event: pygame.event.Event):
        self.text_box.update()

    def update(self):
        super().update()
        self.text_box.draw(self.screen)

if __name__ == '__main__':
    TextBoxTest().run()
