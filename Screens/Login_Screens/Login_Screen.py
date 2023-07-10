import colors
from Profile import profile
from Screens.Change_Screen_Buttons import change_screen_button_rect
from Screens.Login_Screens.Login_bar import login_bar_screen
from draw import text_info


class login_screen(login_bar_screen):
    def __init__(self, screen_width: int, screen_height: int, profile: profile, user):
        super().__init__(screen_width, screen_height, profile, user)
        self.text_on_screen.append(text_info('Login', screen_width / 2, 80, 300, 80, colors.white, True))
        self.text_on_screen.append(text_info('Don\'t have an Account?', screen_width / 2, screen_height / 2 + 210, 300, 90, colors.white, True))
        self.buttons.append(change_screen_button_rect('start login', self, 20, screen_height - 70, 'Back', False))
        self.buttons.append(change_screen_button_rect('create account', self, screen_width / 2, screen_height / 2 + 300,
                                                      'Create Account', True))
        self.password_bar.stars_only = True

    def attempt_login(self):
        self.error_text.text = ' ' + self.user.login_attempt(self.username_bar.text_typed, self.password_bar.text_typed) + ' '
        self.error_text.on = True

"""
class guest_login_screen(login_screen):
    def __init__(self, user):
        super().__init__(user)
        self.buttons.pop(-1)
        self.buttons.pop(-1)
        self.buttons.append(change_screen_button_rect('home', self, 20, self.screen_height - 70, 'Back', False))
        self.buttons.append(change_screen_button_rect('create account', self, self.screen_width / 2, self.screen_height / 2 + 300,
                                                      'Create Account', True))
"""