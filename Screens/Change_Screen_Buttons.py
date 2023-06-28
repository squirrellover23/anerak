import colors
from Button_Stuff.Circle_Button import circle_button, circle_button_appearance
from Button_Stuff.Rect_Button import rect_button, rect_button_appearance

blue_rect_bstyle = rect_button_appearance(200, 50, colors.light_blue, colors.hov_light_blue, colors.white)
circle_button_ap = circle_button_appearance(30, colors.light_blue, colors.hov_light_blue, colors.white)


class change_screen_button_rect(rect_button):
    def __init__(self, screen_to, surface, x, y, text: str = '', in_center: bool = True, appearance: rect_button_appearance = blue_rect_bstyle):
        super().__init__(surface, x, y, appearance, text, in_center)
        self.screen_to = screen_to

    def command(self):
        self.screen.user.change_screen(self.screen_to)


class change_screen_button_circle(circle_button):
    def __init__(self, x, y, screen_to, screen, text, appearance: circle_button_appearance = circle_button_ap):
        super().__init__(screen, x, y, appearance, text_under=text)
        self.screen_to = screen_to

    def command(self):
        self.screen.user.change_screen(self.screen_to)
