import pygame
from circleshape import *


def Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__()

    def draw(self, x, y, radius, screen):
        pygame.draw.circle(screen, "black", (self.x, self.y),
                           self.radius, width=2)

    def update(self):
        self.position += (self.velocity * dt)
