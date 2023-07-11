import colors
import draw
from Button_Stuff.Rect_Button import rect_button, rect_button_appearance
from Game_Elements.Cards import Card_Types
from Game_Elements.Cards.Card import cards
from Screens.Deck_Builder_Screens.Select_Hero_Screen import change_tab_button
from Screens.Page_Screen import page_screen, icon_information
from Profile import profile

ct_ap = rect_button_appearance(200, 100, colors.red, colors.red, colors.white)


class card_type_button(rect_button):
    def __init__(self, screen: page_screen, y, card_type: Card_Types.card_type):
        super().__init__(screen, 0, y, ct_ap, text=card_type.name, has_gradient=True)
        self.selected = False
        self.def_gradient_stuff = self.gradient_stuff
        self.card_type = card_type
        self.text_height = 30
        self.border_width = 0

    def draw(self):
        if self.selected:
            self.color = self.normal_color
            self.gradient_stuff = self.def_gradient_stuff
        else:
            self.color = colors.black
            self.gradient_stuff = []
        super().draw()

    def command(self):
        if not self.selected:
            self.screen.select_card_type(self)


class add_cards_screen(page_screen):
    def __init__(self, screen_width: int, screen_height: int, profile: profile, user,):
        i_info = icon_information(2, 4, 240, 140, 200, 300, 15, 20)
        super().__init__(screen_width, screen_height, profile, user,
                         [draw.text_info('Anerak', 35, 30, 150, 60, colors.white, False)],
                         [change_tab_button(self, 230, 'Select A Hero  '),
                          change_tab_button(self, 412, '   Add Cards   ')], [], colors.black, Card_Types.standard.cards,
                         i_info, screen_width - 500)
        self.rects += [draw.rect_ob(colors.dark_grey, 400, 70, screen_width - 400, 50,
                                    gradient_stuff=[(0, 70, 0, 120), [(0, colors.dark_grey), (1, colors.grey)]]),
                       draw.rect_ob(colors.black, 594, 70, screen_width - 594, 50),
                       draw.rect_ob(colors.grey, screen_width - 330, 120, 330, screen_height - 120),
                       draw.rect_ob(colors.black, 0, 20, screen_width, 50,
                                    gradient_stuff=[(0, 20, 0, 135), [(0, colors.black), (1, colors.light_grey)]]),
                       draw.poly_ob(colors.black, ((0, 20), (220, 20), (220, 70), (200, 120), (0, 120)),
                                    gradient_stuff=[(0, 20, 0, 135), [(0, colors.black), (1, colors.light_grey)]]),
                       draw.rect_ob(colors.dark_grey, 0, 135, 200, screen_height - 135)]
        self.standard_card_type = card_type_button(self, 135, Card_Types.standard)
        self.buttons.append(self.standard_card_type)
        num_of_types = 1
        for c in self.profile.deck_editing.card_types:
            self.buttons.append(card_type_button(self, 135 + num_of_types * 105, c))
            num_of_types += 1
        self.buttons.append(card_type_button(self, 135 + num_of_types * 105, Card_Types.relic))
        self.selected_type = self.standard_card_type
        self.select_card_type(self.standard_card_type)
        self.cards_added = []

    def icon_draw(self, icon):
        icon.stored_info.draw_card_icon(self, icon.x, icon.y, 200, 300)

    def select_card_type(self, card_type: card_type_button):
        self.selected_type.selected = False
        self.selected_type = card_type
        self.selected_type.selected = True
        self.info_for_icons = self.selected_type.card_type.cards
        self.total_pages = int(len(self.info_for_icons) / self.icons_per_page + .999)
        if self.total_pages == 0:
            self.total_pages = 1
        self.change_page(0)
