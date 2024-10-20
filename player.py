import pygame
from circleshape import CircleShape

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
