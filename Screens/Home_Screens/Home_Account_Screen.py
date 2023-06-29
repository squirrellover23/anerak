import colors
import draw
from Screens.Home_Screens.Home_Screen_base import home_screen_base_page, page_button
from Profile import profile


class account_page_button(page_button):
    def __init__(self, screen_to, surface, x, y, text):
        super().__init__(screen_to, surface, x, y, 200, text)



class home_account_screen(home_screen_base_page):
    def __init__(self, screen_width: int, screen_height: int, profile: profile, user):
        super().__init__(screen_width, screen_height, profile, user)
        self.highlight_page_on.width = 120
        self.highlight_page_on.x = 1290
        self.highlighted_account_page_y = 140
        self.highlight_account_page = draw.rect_ob(colors.white, 0, self.highlighted_account_page_y, 200, 110, gradient_stuff=[(0, self.highlighted_account_page_y, 0, self.highlighted_account_page_y + 110), [(0, colors.dark_red), (.5, colors.light_red), (1, colors.dark_red)]])
        self.highlight_account_page_2 = draw.rect_ob(colors.black, 0, self.highlighted_account_page_y, 200, 110, alpha=0.2)
        self.rects += [draw.rect_ob(colors.dark_grey, 0, 140, 200, screen_height - 140)]
        for i in range(4):
            self.rects.append(draw.rect_ob(colors.black, 2, i * 110 + 142, 198, 96))

        self.rects += [self.highlight_account_page, self.highlight_account_page_2]
        self.text_on_screen.append(draw.text_info('Squirrel_lover', screen_width - 300, 100, 270, 60, colors.white))
        self.buttons += [account_page_button('home account', self, 0, 180, 'Info'), account_page_button('account social', self, 0, 290, 'Social'), account_page_button('account social', self, 0, 400, 'Stats'), account_page_button('account social', self, 0, 510, 'Settings')]
