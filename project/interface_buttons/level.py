import pygame.image

class Level:
    def __init__(self):
        self.value = 1
        self.image = pygame.image.load('img/level.png')
        self.pos = (50,0)
    def draw(self,screen):
        screen.blit(self.image, self.pos)