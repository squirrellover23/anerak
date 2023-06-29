

class deck:
    def __init__(self, name):
        self.name = name
        self.commander = None
        self.card_types = []
        self.cards = []
        self.relics = []
        self.complete = False