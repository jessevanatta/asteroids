import pygame
from constants import *
from circleshape import CircleShape
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

# Create groups
updatables = pygame.sprite.Group()
drawables = pygame.sprite.Group()
asteroids = pygame.sprite.Group()
Player.containers = (updatables, drawables)
Asteroid.containers = (asteroids, updatables, drawables)
AsteroidField.containers = (updatables,)

def main():
    # Initialize
    pygame.init()
    time = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    field = AsteroidField()

    #Create player
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    # Game loop
    while True:
        # Quit with window X
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # Update
        screen.fill((0, 0, 0))
        dt = time.tick(60) / 1000
        updatables.update(dt)

        # Draw
        for drawable in drawables:
            drawable.draw(screen)
        pygame.display.flip()

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

if __name__ == "__main__":
    main()
