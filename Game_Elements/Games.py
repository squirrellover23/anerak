
class stack_object:
    def __init__(self, player, triggers):
        self.player = player
        self.triggers = triggers
        self.ordered_events = []

    def order_triggers(self):
        if len(self.ordered_events) == 0:
            pass


class game:
    def __init__(self, board_type):
        self.board_type = board_type
        self.turn = 1
        self.players = []
        self.play_turn_order = []
        self.play_order_index = 0
        self.board = []
        self.stack = []
        self.current_player_action = None
        self.current_player_turn = None
        self.current_phase = None

    def add_player(self, profile, deck):
        pass

    def start_game(self):
        pass

    def run_game(self):
        pass

    def handle_stack(self):
        for e in self.stack:
            pass

    def attempt_to_add_action_to_stack(self, action, triggers):
        pass

    def make_player_select(self, player):
        pass
