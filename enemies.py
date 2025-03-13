import pygame
from config import RED

class Enemy:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)
        self.speed = 3
    
    def move(self):
        self.rect.x += self.speed
        if self.rect.x >= 700 or self.rect.x <= 100:
            self.speed *= -1  # Cambia de dirección al llegar a los límites
    
    def draw(self, screen):
        pygame.draw.rect(screen, RED, self.rect)
