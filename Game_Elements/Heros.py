import colors
import draw
from Game_Elements.Cards import Card_Types as ct

class hero:
    all_heroes = []

    def __init__(self, name, health, speed, card_types):
        self.name = name
        self.health = health
        self.speed = speed
        self.card_types = card_types
        self.basic_attack = None
        self.abilities = []
        self.abilities_text = ''
        self.all_heroes.append(self)

    def draw_hero_icon(self, screen, x, y):
        draw.rect(screen, colors.grey, x, y, 200, 300)
        draw.polygon(screen, colors.tan,
                     ((x + 2, y), (x + 198, y), (x + 190, y + 25), (x + 10, y + 25)))
        draw.polygon(screen, colors.dark_grey,
                     ((x + 2, y), (x + 198, y), (x + 190, y + 25), (x + 10, y + 25)), 2)
        draw.text(screen, x + 100, y + 12, self.name, 180, 25, colors.white, in_center=True, font_variation='bold')
        draw.rect(screen, colors.light_grey, x + 10, y + 30, 180, 100)
        draw.polygon(screen, colors.tan, ((x+2, y+30), (x+12, y+30), (x+2, y+30), (x+2, y+30), (x+2, y+30), (x+2, y+30),))

        draw.text(screen, x + 50, y + 50, f'HP:{self.health}', 70, 20, colors.white, in_center=True)
        draw.text(screen, x + 140, y + 50, f'Speed:{self.speed}', 70, 20, colors.white, in_center=True)

        draw.rect(screen, colors.lighten_or_darken(colors.grey, -20), x + 8, y + 150, 184, 20)


ur_mother = hero('ur mother', 20, 5, [ct.spell])


