import pygame
from pygame_tools import *

class ParticleTest(GameScreen):

    def __init__(self):
        pygame.init()
        size = Point(600, 600)
        super().__init__(pygame.display.set_mode(size), size, (size.x // 2, size.y // 2))
        self.center = Point(self.window_size.x // 2, self.window_size.y // 2)
        self.particles = [Particle(self.center, 10, 'grey', (1, 0), None, 1, 4)]

    def update(self):
        super().update()
        i = 0
        while i < len(self.particles):
            if not self.particles[i].alive:
                self.particles.remove(self.particles[i])
            else:
                self.particles[i].update()
                self.particles[i].draw(self.screen)
                i += 1

if __name__ == '__main__':
    ParticleTest().run()
