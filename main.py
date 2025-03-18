import pygame
from pygame.color import Color
from pygame.surface import Surface
from constants import *


def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    # starting game loop
    while(True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        surface = Surface(size=(SCREEN_WIDTH,SCREEN_HEIGHT))
        surface.fill(color=(0,0,0))
        pygame.display.flip()


if __name__ == "__main__":
    main()
