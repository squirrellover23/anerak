import colors
from Profile import profile
from Button_Stuff.Rect_Button import rect_button, rect_button_appearance
from Screens.Screen import screen
from draw import text_info

blue_rect_bstyle = rect_button_appearance(200, 50, colors.light_blue, colors.hov_light_blue, colors.white)
text_bar_ap = rect_button_appearance(300, 50, colors.white, colors.white, colors.black)


class login_button(rect_button):
    def __init__(self, screen: screen, x, y):
        super().__init__(screen, x, y, blue_rect_bstyle, 'Continue', True)

    def command(self):
        self.screen.attempt_login()


class text_bar(rect_button):
    def __init__(self, x, y, surface: screen, rect_appearance: rect_button_appearance = text_bar_ap, in_center: bool = True):
        super().__init__(surface, x, y, rect_appearance, in_center=in_center)
        self.stars_only = False
        self.text_typed = ''

    def handle_mouse_click(self):
        if self.screen.selected_typing_bar == self and not self.hovered:
            self.screen.selected_typing_bar = None
            self.screen.user.is_typing = False
        super().handle_mouse_click()

    def command(self):
        self.screen.selected_typing_bar = self
        self.screen.user.is_typing = True

    def handle_text_update(self, text):
        if len(text) == 1:
            self.text_typed += text
        elif text == 'Backspace':
            self.text_typed = self.text_typed[:-1]

    def draw(self):
        if self.screen.selected_typing_bar == self:
            self.border_color = colors.black
            self.border_width = 4
        else:
            self.border_color = colors.white
            self.border_width = 2
        if self.stars_only:
            self.text = '*' * len(self.text_typed)
        else:
            self.text = self.text_typed
        if self.screen.selected_typing_bar == self:
            self.text += '|'
        super().draw()


class login_bar_screen(screen):
    def __init__(self, screen_width: int, screen_height: int, profile: profile, user):
        self.login_button = login_button(self, screen_width/2, screen_height/2 + 80)
        self.username_bar = text_bar(screen_width / 2, screen_height / 2 - 150, self)
        self.password_bar = text_bar(screen_width / 2, screen_height / 2, self)
        self.error_text = text_info('', screen_width / 2, screen_height / 2 + 140, 300, 50, colors.white, True,
                                    background_color=colors.red)
        self.error_text.on = False
        super().__init__(screen_width, screen_height, profile,
                         [text_info('Username', screen_width / 2, screen_height / 2 - 220, 250, 50, colors.white, True),
                          text_info('Password', screen_width / 2, screen_height / 2 - 70, 250, 50, colors.white, True),
                          self.error_text],
                         [self.password_bar, self.username_bar, self.login_button], [], colors.black, user)
        self.selected_typing_bar = None

    def handle_text_typed(self, text):
        if text == 'Enter':
            self.attempt_login()
        if text == 'Tab':
            print('switch')
            if self.selected_typing_bar == self.username_bar:
                self.selected_typing_bar = self.password_bar
            if self.selected_typing_bar == self.password_bar:
                self.selected_typing_bar = self.username_bar
        if self.selected_typing_bar is not None:
            self.selected_typing_bar.handle_text_update(text)
            self.update_screen = 1

    def attempt_login(self):
        pass
