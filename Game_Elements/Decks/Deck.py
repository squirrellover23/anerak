import colors
import draw


class deck:
    def __init__(self):
        self.name = None
        self.hero = None
        self.card_types = []
        self.cards = []
        self.relics = []
        self.complete = False

    def add_hero(self, hero):
        self.hero = hero
        self.card_types = hero.card_types

    def show_deck_icon(self, screen, x, y):
        draw.rect(screen, colors.grey, x, y, 180, 200)
        draw.text(screen, x + 90, y + 30, self.name, 160, 30, colors.white, in_center=True)