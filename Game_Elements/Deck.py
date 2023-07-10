import colors
import draw


class deck:
    def __init__(self, name):
        self.name = name
        self.commander = None
        self.card_types = []
        self.cards = []
        self.relics = []
        self.complete = False

    def show_deck_icon(self, screen, x, y):
        draw.rect(screen, colors.grey, x, y, 100, 100)
