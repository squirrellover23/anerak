from Screens.Account_Screens.Account_Screen_Base import account_screen_base
from Profile import profile


class account_social_screen(account_screen_base):
    def __init__(self, screen_width: int, screen_height: int, profile: profile, user):
        super().__init__(screen_width, screen_height, profile, user, 250)
