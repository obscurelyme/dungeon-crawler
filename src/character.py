"""Basic character module"""

import pygame

_CHARACTER_WIDTH = 40
_CHARACTER_HEIGHT = 40


class Character:
    """Character"""

    def __init__(self, x, y):
        self._rect = pygame.Rect(0, 0, _CHARACTER_WIDTH, _CHARACTER_HEIGHT)
        self._rect.center = (x, y)

    def draw(self, surface: pygame.Surface):
        """Draws the character onto the given surface"""
        pygame.draw.rect(surface, (255, 0, 0, 255), self._rect)

    def move(self, x, y):
        """Moves the character's rect"""
        self._rect.x += x
        self._rect.y += y
