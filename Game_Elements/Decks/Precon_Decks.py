from Game_Elements.Decks.Deck import deck


class precon_deck(deck):
    all_precons = []

    def __init__(self, name):
        super().__init__(name)
        self.complete = True
        self.all_precons.append(self)


death_by_hate = precon_deck('Death By Hate')
ur_mom = precon_deck('Ur Mom')
runes_galore = precon_deck('Runes Galore')
