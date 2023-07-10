import colors
import draw
from Screens.Screen import screen
from Profile import profile


class create_new_deck_start(screen):
    def __init__(self, screen_width: int, screen_height: int, profile: profile, user):
        super().__init__(screen_width, screen_height, profile, text, buttons, [], colors.black, user)
