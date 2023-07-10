import colors
from Button_Stuff.Rect_Button import rect_button, rect_button_appearance
from Screens.Change_Screen_Buttons import change_screen_button_rect
from Screens.Screen import screen
from draw import text_info


class con_as_guest_b(rect_button):
    def __init__(self, screen: screen, x, y, rect_appearance: rect_button_appearance):
        super().__init__(screen, x, y, rect_appearance)

    def command(self):
        self.screen.user.change_profile()


class start_login_screen(screen):
    def __init__(self, screen_width: int, screen_height: int, profile, user):
        super().__init__(screen_width, screen_height, profile, [text_info('Welcome To Anerak', screen_width / 2, 100, screen_width - 200, 100, colors.white, True)], [
            change_screen_button_rect('login', self, screen_width / 2, 300, 'Login'),
            change_screen_button_rect('create account', self, screen_width / 2, 425, 'Create Account')
        ], [], colors.black, user)

