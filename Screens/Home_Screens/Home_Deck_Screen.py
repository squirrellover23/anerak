import colors
import draw
from Button_Stuff.Rect_Button import rect_button_appearance, rect_button
from Screens.Change_Screen_Buttons import change_screen_button_rect
from Screens.Home_Screens.Home_Screen_base import home_screen_base_page
from Profile import profile

rect_ap = rect_button_appearance(180, 50, colors.light_blue, colors.hov_light_blue, colors.white)
rect_ap_2 = rect_button_appearance(100, 50, colors.light_blue, colors.hov_light_blue, colors.white)


class change_deck_page_button(rect_button):
    def __init__(self, screen, x, ):
        super().__init__(screen, x, screen.screen_height - 80, rect_ap_2, )


class create_new_deck_button(change_screen_button_rect):
    def __init__(self, screen):
        super().__init__('create new deck start', screen, 10, 250, text='Create New Deck', in_center=False,
                         appearance=rect_ap)


class home_deck_screen(home_screen_base_page):
    def __init__(self, screen_width: int, screen_height: int, profile: profile, user):
        super().__init__(screen_width, screen_height, profile, user)
        self.highlight_page_on.width = 125
        self.highlight_page_on.x = 455
        self.deck_page_on = 1
        self.deck_total_pages = int(len(self.profile.decks) / 9 + .999)
        if self.deck_total_pages == 0:
            self.deck_total_pages = 1
            # text for 0 decks
        self.rects.append(draw.rect_ob(colors.dark_grey, 0, 155, 200, 800))
        self.rects.append(draw.rect_ob(colors.dark_grey, screen_width - 250, 125, 250, 800))

        self.buttons.append(create_new_deck_button(self))
        self.text_on_screen.append(draw.text_info('My Decks', 10, 150, 180, 60, colors.white))
        self.text_on_screen.append(
            draw.text_info(f'Page {self.deck_page_on} of {self.deck_total_pages}', screen_width - 400,
                           screen_height - 130, 100, 50, colors.white))
