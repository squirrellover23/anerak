import colors
import draw
from Button_Stuff.Rect_Button import rect_button_appearance, rect_button
from Game_Elements.Decks.Deck import deck
from Screens.Change_Screen_Buttons import change_screen_button_rect
from Screens.Home_Screens.Home_Screen_base import home_screen_base_page
from Profile import profile

ve_ap = rect_button_appearance(180, 45, colors.blue, colors.lighten_or_darken(colors.blue, 40), colors.white)
new_deck_ap = rect_button_appearance(180, 50, colors.green, colors.light_green, colors.white)
change_page_ap = rect_button_appearance(90, 30, colors.light_blue, colors.hov_light_blue, colors.white)
deck_icon_ap = rect_button_appearance(180, 200, colors.white, colors.white, colors.white)


class change_deck_page_button(rect_button):
    def __init__(self, screen: home_screen_base_page, x, text, page_diff):
        super().__init__(screen, x, screen.screen_height - 60, change_page_ap, text)
        self.page_diff = page_diff
        self.inactive_color = colors.dark_grey

    def command(self):
        self.screen.change_deck_page(self.page_diff)


class create_new_deck_button(change_screen_button_rect):
    def __init__(self, screen):
        super().__init__('select hero', screen, 10, 250, text='Create New Deck', in_center=False,
                         appearance=new_deck_ap, has_gradient=True)

    def command(self):
        super().command()
        self.screen.profile.deck_editing = deck()


class view_deck_button(change_screen_button_rect):
    def __init__(self, screen):
        super().__init__('view deck', screen, screen.screen_width - 125, screen.screen_height - 70, '  View Deck  ', appearance=ve_ap, has_gradient=True)


class edit_deck_button(change_screen_button_rect):
    def __init__(self, screen):
        super().__init__('edit deck', screen, screen.screen_width - 125, screen.screen_height - 135, '  Edit Deck  ', appearance=ve_ap, has_gradient=True)


class deck_icon(rect_button):
    def __init__(self, screen, x, y):
        super().__init__(screen, x, y, deck_icon_ap)
        self.alpha = 0
        self.deck = None
        self.selected = False
        self.selected_b_width = 2

    def draw(self):
        if self.deck is not None:
            if self.selected:
                draw.rect(self.screen, colors.blue, self.x, self.y, self.width, self.height, self.selected_b_width)
            self.deck.show_deck_icon(self.screen, self.x, self.y)

    def change_deck(self, deck):
        self.deck = deck
        self.selected = False

    def command(self):
        if self.deck is not None:
            self.screen.select_icon(self)


class home_deck_screen(home_screen_base_page):
    def __init__(self, screen_width: int, screen_height: int, profile: profile, user):
        super().__init__(screen_width, screen_height, profile, user)
        self.highlight_page_on.width = 125
        self.highlight_page_on.x = 455
        self.deck_page_on = 1
        self.deck_total_pages = int(len(self.profile.decks) / 12 + .999)
        if self.deck_total_pages == 0:
            self.deck_total_pages = 1
            self.text_on_screen.append(draw.text_info('Create Decks and they will appear here', 300, 120, 500, 60, colors.grey))
        self.rects.append(draw.rect_ob(colors.dark_grey, 0, 155, 200, 800))
        self.rects.append(draw.rect_ob(colors.dark_grey, screen_width - 250, 125, 250, 800))

        self.buttons.append(create_new_deck_button(self))
        self.text_on_screen.append(draw.text_info('My Decks', 10, 150, 180, 60, colors.white))
        self.page_text = draw.text_info(f'Page {self.deck_page_on} of {self.deck_total_pages}', screen_width - 420, screen_height - 130, 100, 50, colors.white)
        self.text_on_screen.append(self.page_text)

        self.previous_page_b = change_deck_page_button(self, screen_width - 460, 'Previous', -1)
        self.next_page_b = change_deck_page_button(self, screen_width - 360, 'Next', 1)
        self.buttons += [self.next_page_b, self.previous_page_b]
        self.deck_icons = []
        for row in range(0, 3):
            for col in range(0, 4):
                self.deck_icons.append(deck_icon(self, 300 + 210 * col, 140 + 210 * row))
        self.buttons += self.deck_icons
        self.change_deck_page(0)

        self.selected_icon = None
        self.s_deck_name_text = draw.text_info('', screen_width - 120, 160, 230, 50, colors.white, in_center=True)
        self.text_on_screen.append(self.s_deck_name_text)
        self.view_s_deck_button = view_deck_button(self)
        self.edit_s_deck_button = edit_deck_button(self)
        self.view_s_deck_button.on = False
        self.edit_s_deck_button.on = False
        self.buttons += [self.edit_s_deck_button, self.view_s_deck_button]

    def check_page_buttons(self):
        if self.deck_page_on == 1:
            self.previous_page_b.active = False
        else:
            self.previous_page_b.active = True
        if self.deck_page_on == self.deck_total_pages:
            self.next_page_b.active = False
        else:
            self.next_page_b.active = True

        self.previous_page_b.hover_update()
        self.next_page_b.hover_update()

    def change_deck_page(self, page_diff):
        self.deck_page_on += page_diff
        self.check_page_buttons()
        self.page_text.text = f'Page {self.deck_page_on} of {self.deck_total_pages}'
        start_d_index = (self.deck_page_on - 1) * 12

        for d in range(start_d_index, start_d_index + 12):
            if d >= len(self.profile.decks):
                self.deck_icons[d % 12].change_deck(None)
            else:
                self.deck_icons[d % 12]. change_deck(self.profile.decks[d])

    def select_icon(self, selected_icon: deck_icon):
        if self.selected_icon == selected_icon:
            selected_icon.selected = False
            self.selected_icon = None
            self.s_deck_name_text.text = ''
            self.view_s_deck_button.on = False
            self.edit_s_deck_button.on = False
        else:
            if self.selected_icon is not None:
                self.selected_icon.selected = False
            self.selected_icon = selected_icon
            self.s_deck_name_text.text = self.selected_icon.deck.name
            self.view_s_deck_button.on = True
            self.edit_s_deck_button.on = True
            self.selected_icon.selected = True

