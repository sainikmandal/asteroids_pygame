import pygame
from circleshape import CircleShape
from constants import *

class Player(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.rotation = 0  # Initialize rotation attribute

    def draw(self, screen):
        # Draw the player using a white triangle
        pygame.draw.polygon(screen, (255, 255, 255), self.triangle(), 2)
    
    def triangle(self):
        # Calculate the points of the triangle based on position and rotation
        forward = pygame.Vector2(0, -1).rotate(self.rotation)
        right = pygame.Vector2(0, -1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    def rotate(self, dt):
        # Rotate the player based on the turn speed and delta time
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            # Rotate left by using negative dt
            self.rotate(-dt)
        if keys[pygame.K_d]:
            # Rotate right by using positive dt
            self.rotate(dt)
