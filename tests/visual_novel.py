#!/usr/bin/env python3

import pygame
from pygame_tools import *
from enum import Enum, auto
from typing import Callable

class Speaker(Enum):
    PLAYER = auto()
    RED_RECT = auto()
    BLUE_RECT = auto()

class State(Enum):
    RED_RECT_TALKING = auto()
    PLAYER_TALKING = auto()
    RED_RECT_RESPONSE_INSULTED = auto()
    RED_RECT_RESPONSE_DISGUST = auto()
    RED_RECT_RESPONSE_DANCE = auto()
    RED_RECT_RESPONSE_CONFUSED = auto()
    BLUE_RECT_TALKING = auto()
    RED_RECT_FINAL = auto()
    END = auto()

    def get_speaker(self) -> Speaker:
        match self:
            case State.RED_RECT_TALKING \
                | State.RED_RECT_RESPONSE_INSULTED \
                | State.RED_RECT_RESPONSE_DISGUST \
                | State.RED_RECT_RESPONSE_DANCE \
                | State.RED_RECT_RESPONSE_CONFUSED \
                | State.RED_RECT_FINAL:
                return Speaker.RED_RECT
            case State.PLAYER_TALKING | State.END:
                return Speaker.PLAYER
            case State.BLUE_RECT_TALKING:
                return Speaker.BLUE_RECT
        raise ValueError(f'No speaker found for state {self}')

CHARACTER_STATES_TABLE = {
    State.RED_RECT_TALKING: ([
        "Hello, I am mister red rectangle!",
        "This is the second slide I can say things"
    ], State.PLAYER_TALKING),
    State.RED_RECT_RESPONSE_INSULTED: ([
        'Rude.',
    ], State.BLUE_RECT_TALKING),
    State.RED_RECT_RESPONSE_DISGUST: ([
        '...',
        'Weirdo',
    ], State.END),
    State.RED_RECT_RESPONSE_DANCE: ([
        '*fortnite dances back*',
    ], State.END),
    State.RED_RECT_RESPONSE_CONFUSED: ([
        'I have no idea what that means man.',
    ], State.END),
    State.BLUE_RECT_TALKING: ([
        'Hey! Leave my man alone! Back off!',
        'Me? I\'m also mister rectangle! We\'re Husbands!',
        'Bigot!',
    ], State.RED_RECT_FINAL),
    State.RED_RECT_FINAL: ([
        'You tell em babe!',
    ], State.END),
}

PLAYER_STATES_TABLE = {
    State.PLAYER_TALKING: {
        'I hate you mister rectangle': State.RED_RECT_RESPONSE_INSULTED,
        'Marry me mister rectangle': State.RED_RECT_RESPONSE_DISGUST,
        '*fortnite dances*': State.RED_RECT_RESPONSE_DANCE,
        'fourth option': State.RED_RECT_RESPONSE_CONFUSED,
    },
    State.END: None,
}

class VisualNovelTest(MenuScreen):

    def __init__(self):
        pygame.init()
        size = Point(600, 600)
        super().__init__(pygame.display.set_mode(size), size, (size.x // 2, size.y // 2))
        self.font = pygame.font.SysFont(pygame.font.get_default_font(), 20)
        self.center = Point(self.window_size.x // 2, self.window_size.y // 2)
        self.text_box_rect = Rect(10, self.center.y, self.window_size.x - 20, self.center.y - 10)
        self.text_box = TextBox(
            [],
            self.text_box_rect,
            font = self.font,
        )
        self.set_state(State.RED_RECT_TALKING)

    def set_state(self, state: State):
        self.state = state
        self.speaker = self.state.get_speaker()
        match self.speaker:
            case Speaker.PLAYER:
                self.update_buttons()
            case _:
                self.update_text_box()
                self.color = 'red' if self.speaker == Speaker.RED_RECT else 'blue'

    def update_buttons(self):
        table = PLAYER_STATES_TABLE[self.state]
        if table is None:
            self.buttons = []
            return
        size = Point(self.window_size.x - 20, 20)
        self.buttons = [
            Button(
                self.respond(state),
                text,
                Rect(10, self.center.y + i * (10 + size.y), *size),
                self.font
            ) for i, (text, state) in enumerate(table.items())
        ]

    def update_text_box(self):
        lines, self.next_state = CHARACTER_STATES_TABLE[self.state]
        self.text_box = TextBox(
            lines,
            self.text_box_rect,
            font = self.font,
        )

    def respond(self, response: any) -> Callable[[], None]:
        def f():
            self.set_state(response)
        return f

    def key_down(self, event: pygame.event.Event):
        match self.speaker:
            case Speaker.RED_RECT | Speaker.BLUE_RECT:
                self.text_box.update()
                if self.text_box.done:
                    self.set_state(self.next_state)
            case Speaker.PLAYER:
                super().key_down(event)

    def update(self):
        self.screen.fill((0, 0, 100))
        size = self.window_size * (1 / 3, 2 / 3)
        pygame.draw.rect(
            self.screen,
            self.color,
            Rect(
                self.center.x - size.x // 2,
                self.center.y - size.y // 2,
                *size
            )
        )
        match self.speaker:
            case Speaker.RED_RECT | Speaker.BLUE_RECT:
                self.text_box.draw(self.screen)
            case Speaker.PLAYER:
                self.draw_buttons()

    def mouse_button_down(self, event: pygame.event.Event):
        if self.speaker == Speaker.PLAYER:
            super().mouse_button_down(event)

if __name__ == '__main__':
    VisualNovelTest().run()
