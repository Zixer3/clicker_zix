import pygame

class Shop:
    def __init__(self):
        self.button_return = pygame.image.load(r'img/cross.png')
        self.button_return_pos = (0, 0)
        self.button_click = pygame.image.load(r'img/click.png')
        self.button_click_pos = (50, 100)
        self.button_autoclick = pygame.image.load(r'img/bog.png')
        self.button_autoclick_pos = (50, 350)
        self.click_cost = 26
        self.DPS_cost = 100
    def try_to_buy(self, type, balance):
        if type == 'click':
            if balance >= self.click_cost:
                self.click_cost *= 2
                return balance - self.click_cost / 2
            return balance
    def draw(self, screen, balance):
        screen.blit(self.button_return, self.button_return_pos)
        screen.blit(self.button_click, self.button_click_pos)
        screen.blit(self.button_autoclick, self.button_autoclick_pos)
        self.write(screen, balance)
    def write(self, screen, balance):
        font = pygame.font.Font(None, 40)
        text = font.render(f"Seeds: {balance} ", True, [255, 255, 255])
        screen.blit(text, (60, 0))
