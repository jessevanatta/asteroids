import pygame
import sys
from constants import *
from scorekeeper import Score
from circleshape import CircleShape
from player import Player, Shot
from asteroid import Asteroid
from asteroidfield import AsteroidField

# Create groups
updatables = pygame.sprite.Group()
drawables = pygame.sprite.Group()
asteroids = pygame.sprite.Group()
shots = pygame.sprite.Group()
Player.containers = (updatables, drawables)
Asteroid.containers = (asteroids, updatables, drawables)
AsteroidField.containers = (updatables,)
Shot.containers = (shots, updatables, drawables)
Score.containers = (updatables, drawables)

def main():
    # Initialize
    pygame.init()
    time = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    field = AsteroidField()
    score_font = pygame.font.Font()
    score = Score(0, score_font)

    #Create player
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    # Game loop
    while True:
        # Quit with window X
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        # Quit with Q
        keys = pygame.key.get_pressed()
        if keys[pygame.K_q]:
            pygame.quit()
            sys.exit(1)

        # Update
        screen.fill((0, 0, 0))
        dt = time.tick(60) / 1000
        updatables.update(dt)

        # Collisions
        for a in asteroids:
            if a.collide(player):
                print("Game over!")
                sys.exit(1)
            for s in shots:
                if a.collide(s):
                    a.split()
                    s.kill()

        # Draw
        for drawable in drawables:
            drawable.draw(screen)
        pygame.display.flip()

if __name__ == "__main__":
    main()
