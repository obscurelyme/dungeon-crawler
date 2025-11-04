"""Window management module for the application"""

import pygame

_SCREEN_WIDTH = 1920
_SCREEN_HEIGHT = 1080


class Window:
    """Manages the window of the application"""

    def __init__(self, title="Application", borderless=False):
        """Initialize the window with optional borderless mode."""
        window_flags = (
            pygame.DOUBLEBUF | pygame.NOFRAME if borderless else pygame.DOUBLEBUF
        )
        self._screen = pygame.display.set_mode(
            (_SCREEN_WIDTH, _SCREEN_HEIGHT), window_flags, 0, 0, 1
        )
        pygame.display.set_caption(title)

    def get_surface(self) -> pygame.Surface:
        """Gets the window's surface"""
        return self._screen

    def clear_color(self):
        """Clears the screen to black"""
        self._screen.fill((0, 0, 0, 0))

    def flip(self):
        """Update the display of the surface within the Window"""
        pygame.display.flip()
