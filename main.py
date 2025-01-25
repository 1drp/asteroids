import pygame
from constants import *

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    # main game loop
    while True:
        # Exit Condition
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        # Fill background
        screen.fill((0,0,0))
        pygame.display.flip()
        dt = clock.tick(60) / 1000
        
        # DEBUG: Uncomment line below to print FPS to console
        #print(clock.get_fps())


if __name__ == "__main__":
    main()
