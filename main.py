import pygame
from constants import *
from circleshape import CircleShape
from player import Player

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    # pygame groups for organization
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updateable, drawable)

    me = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    # main game loop
    while True:
        # Exit Condition
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        # Fill background
        screen.fill((0,0,0))

        # Update groups
        for ud in updateable:
            ud.update(dt)
        for dw in drawable:
            dw.draw(screen)


        pygame.display.flip()
        dt = clock.tick(60) / 1000
        
        # DEBUG: Uncomment line below to print FPS to console
        #print(clock.get_fps())


if __name__ == "__main__":
    main()
