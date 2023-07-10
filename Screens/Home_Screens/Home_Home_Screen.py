from Screens.Home_Screens.Home_Screen_base import home_screen_base_page
from Profile import profile


class home_home_screen(home_screen_base_page):
    def __init__(self, screen_width: int, screen_height: int, profile: profile, user):
        super().__init__(screen_width, screen_height, profile, user)

