import colors


class card_type:
    all_card_types = []

    def __init__(self, name, border_color):
        self.name = name
        self.border_color = border_color
        self.all_card_types.append(self)
        self.cards = []

    def draw_card_border(self, screen, x, y, width, height):
        pass


class card_subtype:
    def __init__(self, name, super_type: card_type):
        self.name = name
        self.super_type = super_type


standard = card_type('Standard', colors.black)
artifact = card_type('Artifact', colors.black)
weapon = card_type('Weapon', colors.black)
spell = card_type('Spell', colors.black)
ritual = card_type('Ritual', colors.black)
rune = card_type('Rune', colors.black)
equipment = card_type('Equipment', colors.black)
relic = card_type('Relic', colors.black)
