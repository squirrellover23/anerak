import colors
import draw
from Screens.Change_Screen_Buttons import change_screen_button_rect, rect_button_appearance
from Screens.Screen import screen, profile

pb_rect_style = rect_button_appearance(250, 70, colors.white, colors.white, colors.white)


class page_button(change_screen_button_rect):
    def __init__(self, screen_to, surface, x, y, width, text):
        super().__init__(screen_to, surface, x, y, text=text, in_center=False, appearance=rect_button_appearance(width, 35, colors.white, colors.white, colors.white))
        self.alpha = 0
        self.border_width = 0
        self.text = ' ' + self.text + ' '


class home_screen_base_page(screen):
    def __init__(self, screen_width: int, screen_height: int, profile: profile, user):
        super().__init__(screen_width, screen_height, profile, [
            draw.text_info('Anerak', 35, 30, 150, 60, colors.white, False)],
                         [], [], colors.black, user)
        self.highlight_page_on = draw.rect_ob(colors.white, 230, 20, 100, 70, alpha=.2)
        self.rects += [draw.rect_ob(colors.black, 0, 20, screen_width, 70, gradient_stuff=[(0, 20, 0, 135), [(0, colors.black), (1, colors.light_grey)]]),
                       draw.poly_ob(colors.black, ((0, 20), (230, 20), (230, 90), (200, 120), (0, 120)), gradient_stuff=[(0, 20, 0, 135), [(0, colors.black), (1, colors.light_grey)]]), self.highlight_page_on]
        self.buttons = [page_button('home base', self, 230, 40, 100, 'Home'), page_button('home games', self, 330, 40, 125, 'Games'), page_button('home decks', self, 455, 40, 125, 'Decks'), page_button('home account', self, 1300, 40, 100, 'Account')]
