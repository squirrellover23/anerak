import colors
import draw
from Screens.Home_Screens.Home_Screen_base import home_screen_base_page, page_button
from Profile import profile


class account_page_button(page_button):
    def __init__(self, screen_to, surface, x, y, text):
        super().__init__(screen_to, surface, x, y, 200, text)
        self.height = 107


class account_screen_base(home_screen_base_page):
    def __init__(self, screen_width: int, screen_height: int, profile: profile, user, highlight_y):
        super().__init__(screen_width, screen_height, profile, user)
        self.highlight_page_on.width = 120
        self.highlight_page_on.x = 1290
        self.highlighted_account_page_y = highlight_y
        self.highlight_account_page = draw.rect_ob(colors.white, 0, self.highlighted_account_page_y, 200, 107,
                                                   gradient_stuff=[(0, self.highlighted_account_page_y, 0,
                                                                    self.highlighted_account_page_y + 107),
                                                                   [(0, colors.dark_red), (.5, colors.light_red),
                                                                    (1, colors.dark_red)]])
        self.highlight_account_page_2 = draw.rect_ob(colors.black, 0, self.highlighted_account_page_y, 200, 107,
                                                     alpha=0.2)
        self.rects += [draw.rect_ob(colors.dark_grey, 0, 140, 202, screen_height - 140)]
        for i in range(4):
            self.rects.append(draw.rect_ob(colors.black, 2, i * 110 + 142, 198, 107))
        self.rects += [self.highlight_account_page, self.highlight_account_page_2]
        self.buttons += [account_page_button('home account', self, 0, 140, 'Info'),
                         account_page_button('account social', self, 0, 250, 'Social'),
                         account_page_button('account stats', self, 0, 360, 'Stats'),
                         account_page_button('account settings', self, 0, 470, 'Settings')]
