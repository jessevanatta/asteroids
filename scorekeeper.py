import pygame

class Score(pygame.sprite.Sprite):
    
    def __init__(self, score, font):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        self.score = score
        self.font = font
        self.surface = self.font.render(self.score, False, "white")

    def update(self, dt):
        pygame.Surface.blit(self.surface, screen)
    
    def draw(self, dt):
        pass