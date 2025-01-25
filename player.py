import pygame
from circleshape import CircleShape
from constants import *

# Player ship class
class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen,):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt):
        keys = pygame.key.get_pressed()
        # Note to confused reviewers: keymapping is for dvorak layout.

        if keys[pygame.K_a]:
            self.rotate(-1 * dt)
        if keys[pygame.K_e]:
            self.rotate(dt)
        if keys[pygame.K_COMMA]:
            self.move(dt)
        if keys[pygame.K_o]:
            self.move(-1 * dt)

    def move(self, dt):
        forward = pygame.Vector2(0,1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt
