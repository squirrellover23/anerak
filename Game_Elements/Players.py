from Game_Elements.Decks.Deck import deck
from Game_Elements.In_Game_Cards import in_game_card, in_game_relic
from Profile import profile
import random


class player:
    def __init__(self, profile: profile, deck: deck, game):
        self.deck = deck
        self.game = game
        self.profile = profile
        self.commander = deck.commander
        self.health = self.commander.health
        self.hand = []
        self.draw_pile = []
        self.level = 1
        for c in deck.cards:
            self.draw_pile.append(in_game_card(c))
        random.shuffle(self.draw_pile)
        self.relic_pile = []
        for r in deck.relics:
            self.relic_pile.append(in_game_relic(r))
        random.shuffle(self.relic_pile)
        self.discard = []
        self.ap = 2
        self.equipments = []
        self.runes = []
        self.before_triggers = {}
        self.after_triggers = {}
        self.effects = []

    def add_trigger(self, trigger_action, action_to_take):
        try:
            self.before_triggers[trigger_action].append(action_to_take)
        except KeyError:
            self.before_triggers[trigger_action] = [action_to_take]

    def take_action(self, action):
        action.execute(player)
        try:
            for t in self.before_triggers[action]:
                t.execute(player)
        except KeyError:
            pass
