#!/usr/bin/env python3

import pygame
from functools import partial
from pygame_tools import *
from enum import Enum, auto
from typing import Callable

class State(Enum):
    CHARACTER_TALKING = auto()
    PLAYER_TALKING = auto()
    CHARACTER_RESPONSE = auto()

class VisualNovelTest(MenuScreen):

    def __init__(self):
        pygame.init()
        size = Point(600, 600)
        super().__init__(pygame.display.set_mode(size), size, (size.x // 2, size.y // 2))
        self.font = pygame.font.SysFont(pygame.font.get_default_font(), 20)
        self.center = Point(self.window_size.x // 2, self.window_size.y // 2)
        self.text_box = TextBox(
            [
                "Hello, I am mister red rectangle!",
                "This is the second slide I can say things"
            ],
            Rect(10, self.center.y, self.window_size.x - 20, self.center.y - 10),
            font = self.font,
        )
        self.state = State.CHARACTER_TALKING
        size = Point(self.window_size.x - 20, 20)
        self.buttons = [
            Button(
                self.respond(f'\'{text}\' Chosen'),
                text,
                Rect(10, self.center.y + i * (10 + size.y), *size),
                self.font
            ) for i, text in enumerate([
                'I hate you mister rectangle',
                'Marry me mister rectangle',
                '*fortnite dances*',
                'fourth option',
            ])
        ]
        self.chosen = None

    def respond(self, response: any) -> Callable[[], None]:
        def f():
            self.chosen = response
        return f

    def key_down(self, event: pygame.event.Event):
        match self.state:
            case State.CHARACTER_TALKING:
                self.text_box.update()
                if self.text_box.done:
                    self.state = State.PLAYER_TALKING
            case State.PLAYER_TALKING:
                super().key_down(event)
                if self.chosen is not None:
                    # TODO do something with that info
                    print(self.chosen)
                    self.state = State.CHARACTER_RESPONSE
                    self.text_box = TextBox(
                        [
                            '...',
                            'Freak',
                        ],
                        self.text_box.rect,
                        font = self.font
                    )
            case State.CHARACTER_RESPONSE:
                self.text_box.update()

    def update(self):
        self.screen.fill((0, 0, 100))
        size = self.window_size * (1 / 3, 2 / 3)
        pygame.draw.rect(
            self.screen,
            'red',
            Rect(
                self.center.x - size.x // 2,
                self.center.y - size.y // 2,
                *size
            )
        )
        match self.state:
            case State.CHARACTER_TALKING | State.CHARACTER_RESPONSE:
                self.text_box.draw(self.screen)
            case State.PLAYER_TALKING:
                self.draw_buttons()

    def mouse_button_down(self, event: pygame.event.Event):
        if self.state == State.PLAYER_TALKING:
            super().mouse_button_down(event)

if __name__ == '__main__':
    VisualNovelTest().run()
