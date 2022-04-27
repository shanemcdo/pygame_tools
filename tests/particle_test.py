#! /usr/bin/env python3

import pygame
from pygame_tools import *
from random import randint

class ParticleTest(GameScreen):

    def __init__(self):
        pygame.init()
        size = Point(600, 600)
        super().__init__(pygame.display.set_mode(size), size, (size.x // 2, size.y // 2))
        self.center = Point(self.window_size.x // 2, self.window_size.y // 2)
        self.particles = []

    def update(self):
        super().update()
        i = 0
        while i < len(self.particles):
            if not self.particles[i].alive:
                self.particles.remove(self.particles[i])
            else:
                self.particles[i].update()
                # gravity
                self.particles[i].velocity.y += 9.8 / 50
                self.particles[i].draw(self.screen)
                i += 1
        self.add_particle()

    def add_particle(self):
        color_val = randint(150, 255)
        self.particles.append(Particle(
            self.center,
            randint(4, 12),
            (color_val, color_val, color_val),
            (randint(-3, 3), randint(-3, 3)),
            None,
            1,
            randint(2, 6)
        ))

if __name__ == '__main__':
    ParticleTest().run()
