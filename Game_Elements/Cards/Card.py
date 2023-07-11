import random

import colors
import draw
from Game_Elements.Cards import Card_Types

class cards:
    all_cards = []

    def __init__(self, name, ap_cost, card_type: Card_Types.card_type, abilities):
        self.all_cards.append(self)
        self.name = name
        self.ap_cost = ap_cost
        self.card_type = card_type
        self.abilities = abilities
        self.card_type.cards.append(self)

    def draw_card_icon(self, screen, x, y, width, height):
        draw.rect(screen, colors.grey, x, y, width, height)
        draw.text(screen, x + width/2, y + height/10, self.name, width*3/4, height/10, colors.white, in_center=True)
        draw.text(screen, x + width - width/10, y + height/10, self.ap_cost, width/10, height/10, colors.white, in_center=True)


for i in range(10):
    c = cards(f'card s{i}', random.randint(1, 3), Card_Types.standard, [])
for i in range(15):
    c = cards(f'card sp{i}', random.randint(1, 3), Card_Types.spell, [])
