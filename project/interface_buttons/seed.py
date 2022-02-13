import pygame


class Seed:
    def __init__(self):
        self.count = 0
        self.image = pygame.image.load('img/seed.png')
        self.pos = (750,0)
    def draw(self,screen):
        screen.blit(self.image, self.pos)