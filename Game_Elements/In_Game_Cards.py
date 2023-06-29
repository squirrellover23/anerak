

class in_game_card:
    def __init__(self, card_effect):
        self.location = 'library'
        self.effect = card_effect
        self.playable = False


class in_game_relic:
    def __init__(self, relic_effect):
        self.location = 'relic pile'
        self.effect = relic_effect
        self.playable = False
