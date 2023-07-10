import colors
from Button_Stuff.Rect_Button import rect_button, rect_button_appearance
from Screens.Account_Screens.Account_Screen_Base import account_screen_base
from Profile import profile

ap = rect_button_appearance(200, 60, colors.red, colors.hov_red, colors.white)


class log_out_button(rect_button):
    def __init__(self, screen):
        super().__init__(screen, screen.screen_width - 220, screen.screen_height - 80, ap, text='  Log Out  ', in_center=False)

    def command(self):
        self.screen.user.change_profile(self.screen.user.login_prof)


class account_settings_screen(account_screen_base):
    def __init__(self, screen_width: int, screen_height: int, profile: profile, user):
        super().__init__(screen_width, screen_height, profile, user, 470)
        self.buttons.append(log_out_button(self))
