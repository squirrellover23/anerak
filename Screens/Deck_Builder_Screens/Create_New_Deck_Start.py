import colors
import draw
from Button_Stuff.Rect_Button import rect_button, rect_button_appearance
from Screens.Screen import screen
from Profile import profile
from Game_Elements.Decks.Deck import deck
from Game_Elements.Heros import hero

tab_button_ap = rect_button_appearance(180, 50, colors.black, colors.black, colors.white)


class change_tab_button(rect_button):
    def __init__(self, screen: screen, x, text):
        super().__init__(screen, x, 70, tab_button_ap, text)
        self.border_width = 0


class create_new_deck_start(screen):
    def __init__(self, screen_width: int, screen_height: int, profile: profile, user):
        super().__init__(screen_width, screen_height, profile,
                         [draw.text_info('Anerak', 35, 30, 150, 60, colors.white, False)],
                         [change_tab_button(self, 230, 'Select A Hero  '),
                          change_tab_button(self, 412, '   Add Cards   ')], [], colors.black, user)
        self.rects += [draw.rect_ob(colors.dark_grey, 400, 70, screen_width - 400, 50,
                                    gradient_stuff=[(0, 70, 0, 120), [(0, colors.dark_grey), (1, colors.grey)]]),

                       draw.rect_ob(colors.black, 0, 20, screen_width, 50,
                                    gradient_stuff=[(0, 20, 0, 135), [(0, colors.black), (1, colors.light_grey)]]),
                       draw.poly_ob(colors.black, ((0, 20), (220, 20), (220, 70), (200, 120), (0, 120)),
                                    gradient_stuff=[(0, 20, 0, 135), [(0, colors.black), (1, colors.light_grey)]])]

        self.page_on = 'Select Hero'
        self.deck_building = deck()
        self.selected_hero = None

