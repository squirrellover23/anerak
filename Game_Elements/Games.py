

class game:
    def __init__(self, board_type):
        self.board_type = board_type
        self.turn = 1
        self.players = []
        self.board = []
        self.stack = []
        self.current_player_action = None
        self.current_player = None
        self.current_phase = None

    def add_player(self, profile, deck):
        pass

    def start_game(self):
        pass

    def run_game(self):
        pass