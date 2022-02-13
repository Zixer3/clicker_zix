from interface_buttons.seed import Seed
from interface_buttons.name import Name
from interface_buttons.level import Level
from interface_buttons.shop_button import ShopButton

class Interface:
    def __init__(self):
        self.seed = Seed()
        self.name = Name()
        self.level = Level()
        self.shop_button = ShopButton()
        self.seed = Seed()
        self.name = Name()
        self.level = Level()
        self.is_shop = False
    def draw(self,screen):
        self.shop_button.draw(screen)
        self.seed.draw(screen)
        self.name.draw(screen)
        self.level.draw(screen)