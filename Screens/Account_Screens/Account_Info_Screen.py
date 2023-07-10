import colors
import draw
from Screens.Account_Screens.Account_Screen_Base import account_screen_base
from Profile import profile


class account_info_screen(account_screen_base):
    def __init__(self, screen_width: int, screen_height: int, profile: profile, user):
        super().__init__(screen_width, screen_height, profile, user, 140)
        self.text_on_screen.append(draw.text_info('Squirrel_lover', screen_width - 300, 100, 270, 60, colors.white))
