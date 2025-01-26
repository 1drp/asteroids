import pygame
import random
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += (self.velocity * dt)
    
    def split(self):
        # kill original
        self.kill()
        
        # stop if already a small asteroid
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        # split larger asteroids
        splitAngle = random.uniform(20,50)
        path1 = self.velocity.rotate(splitAngle)
        path2 = self.velocity.rotate(-1 * splitAngle)
        splitRadius = self.radius - ASTEROID_MIN_RADIUS
        split1 = Asteroid(self.position.x, self.position.y, splitRadius)
        split1.velocity = path1 * 1.2
        split2 = Asteroid(self.position.x, self.position.y, splitRadius)
        split2.velocity = path2 * 1.2

