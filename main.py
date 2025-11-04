"""Entry module of the application"""

import pygame
from src.window import Window
from src.character import Character


def main():
    """Entry point of the application"""
    pygame.init()
    window = Window("Dungeon Crawler")
    running = True
    player = Character(100, 100)

    moving_left = False
    moving_right = False
    moving_up = False
    moving_down = False

    while running:
        window.clear_color()

        dx = 0
        dy = 0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    moving_left = True
                if event.key == pygame.K_d:
                    moving_right = True
                if event.key == pygame.K_w:
                    moving_up = True
                if event.key == pygame.K_s:
                    moving_down = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    moving_left = False
                if event.key == pygame.K_d:
                    moving_right = False
                if event.key == pygame.K_w:
                    moving_up = False
                if event.key == pygame.K_s:
                    moving_down = False

        if moving_right:
            dx = 5
        if moving_left:
            dx = -5
        if moving_up:
            dy = -5
        if moving_down:
            dy = 5

        player.move(dx, dy)
        player.draw(window.get_surface())

        window.flip()

    pygame.quit()


if __name__ == "__main__":
    main()
