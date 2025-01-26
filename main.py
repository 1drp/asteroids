import sys
import pygame
from constants import *
from circleshape import CircleShape
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # Initialize Game
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    # pygame groups for organization
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updateable, drawable)
    Asteroid.containers = (asteroids, updateable, drawable)
    AsteroidField.containers = updateable
    Shot.containers = (shots, drawable, updateable)

    me = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    field = AsteroidField()

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

        # Check for collisions
        for rock in asteroids:
            for bullet in shots:
                if rock.collision(bullet):
                    rock.split()
                    bullet.kill()
            if rock.collision(me):
                print("Game over!")
                sys.exit()

        pygame.display.flip()
        dt = clock.tick(60) / 1000
        
        # DEBUG: Uncomment line below to print FPS to console
        #print(clock.get_fps())


if __name__ == "__main__":
    main()
