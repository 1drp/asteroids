import pygame
from constants import *

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # main game loop
    while True:
        # Exit Condition
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        # Fill background
        screen.fill((0,0,0))
        pygame.display.flip()


if __name__ == "__main__":
    main()
