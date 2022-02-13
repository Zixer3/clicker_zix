import pygame
import sys
from pygame.color import THECOLORS


from interface import Interface
from boss import Boss
from shop import Shop


class Main:
    def __init__(self):
        pygame.init()
        self.WINDOW_WIDTH = 800
        self.WINDOW_HEIGHT = 600
        self.screen = pygame.display.set_mode((self.WINDOW_WIDTH, self.WINDOW_HEIGHT))
        self.interface = Interface()
        self.boss = Boss(1)
        self.player_damage = 5
        self.damage_per_second = 1
        self.active_window = 'game'
        self.shop = Shop()
    def draw(self):
        if self.active_window == 'game':
            self.screen.fill((0, 0, 0))
            self.interface.draw(self.screen)
            self.boss.draw(self.screen)
            self.draw_hp_bar()
        elif self.active_window == 'shop':
            self.screen.fill((0,0,0))
            self.shop.draw(self.screen, self.interface.seed.count)
    def try_to_click(self, pos):
        if self.active_window == 'game':
            if 100 < pos[0] < 700  and 200 < pos[1] < 600:
                self.interface.seed.count += self.boss.hurt(self.player_damage)
            if 0 < pos[0] < 50 and 0 < pos[1] < 50:
                self.active_window = 'shop'
        elif self.active_window == 'shop':
            if 0 < pos[0] < 50 and 0 < pos[1] < 50:
                self.active_window = 'game'
            elif 50 < pos[0] < 750 and 100 < pos[1] < 300:
                first_balance = self.interface.seed.count
                self.interface.seed.count = self.shop.try_to_buy('click', self.interface.seed.count)
                if first_balance > self.interface.seed.count:
                    self.player_damage += 10


    def start(self):
        self.draw()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return 0
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.try_to_click(event.pos)
            self.draw()
            pygame.display.flip()
    def draw_hp_bar(self):
        k = self.boss.hp / (50 * self.boss.level)
        w = 400 * k
        pygame.draw.rect(self.screen, (0, 255, 0), (200, 100, int(w), 50), 0)


main = Main()
main.start()

