

class hero:
    all_heroes = []

    def __init__(self, health, speed, card_types):
        self.health = health
        self.speed = speed
        self.card_types = card_types
        self.basic_attack = None
        self.abilities = []
        self.abilities_text = ''
        self.all_heroes.append(self)

    def draw_icon(self):
        pass
