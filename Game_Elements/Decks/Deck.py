import colors
import draw


class deck:
    def __init__(self):
        self.name = None
        self.Hero = None
        self.card_types = []
        self.cards = []
        self.relics = []
        self.complete = False

    def add_hero(self):
        pass

    def show_deck_icon(self, screen, x, y):
        draw.rect(screen, colors.grey, x, y, 180, 200)
        draw.text(screen, x + 90, y + 30, self.name, 160, 30, colors.white, in_center=True)