import colors
import draw
from Button_Stuff.Rect_Button import rect_button, rect_button_appearance
from Screens.Change_Screen_Buttons import change_screen_button_rect
from Screens.Page_Screen import page_screen, icon_information
from Screens.Screen import screen
from Profile import profile
from Game_Elements.Heros import hero

change_page_ap = rect_button_appearance(90, 30, colors.light_blue, colors.hov_light_blue, colors.white)
tab_button_ap = rect_button_appearance(180, 50, colors.black, colors.black, colors.white)
hero_icon_ap = rect_button_appearance(200, 300, colors.grey, colors.grey, colors.white)
choose_h_ap = rect_button_appearance(200, 50, colors.blue, colors.blue, colors.white)


class continue_button(change_screen_button_rect):
    def __init__(self, screen):
        super().__init__('add cards', screen, screen.screen_width - 165, screen.screen_height - 60, '  Continue  ',
                         has_gradient=True)

    def command(self):
        self.screen.profile.deck_editing.add_hero(self.screen.selected_icon.stored_info)
        super().command()


class change_tab_button(rect_button):
    def __init__(self, screen: screen, x, text):
        super().__init__(screen, x, 70, tab_button_ap, text)
        self.border_width = 0


class select_hero_screen(page_screen):
    def __init__(self, screen_width: int, screen_height: int, profile: profile, user):
        i_info = icon_information(2, 5, 20, 140, 200, 300, 15, 20)
        super().__init__(screen_width, screen_height, profile, user,
                         [draw.text_info('Anerak', 35, 30, 150, 60, colors.white, False)],
                         [change_tab_button(self, 230, 'Select A Hero  '),
                          change_tab_button(self, 412, '   Add Cards   ')], [], colors.black, hero.all_heroes,
                         i_info, screen_width - 500)
        self.rects += [draw.rect_ob(colors.dark_grey, 400, 70, screen_width - 400, 50,
                                    gradient_stuff=[(0, 70, 0, 120), [(0, colors.dark_grey), (1, colors.grey)]]),
                       draw.rect_ob(colors.black, 594, 70, screen_width - 594, 50),
                       draw.rect_ob(colors.grey, screen_width - 330, 120, 330, screen_height - 120),
                       draw.rect_ob(colors.black, 0, 20, screen_width, 50,
                                    gradient_stuff=[(0, 20, 0, 135), [(0, colors.black), (1, colors.light_grey)]]),
                       draw.poly_ob(colors.black, ((0, 20), (220, 20), (220, 70), (200, 120), (0, 120)),
                                    gradient_stuff=[(0, 20, 0, 135), [(0, colors.black), (1, colors.light_grey)]])]

        self.continue_button = continue_button(self)
        self.continue_button.on = False
        self.buttons.append(self.continue_button)
        self.s_hero_text = draw.text_info('', screen_width - 165, 150, 300, 40, colors.white, in_center=True,
                                          font_variation='bold')
        self.text_on_screen.append(self.s_hero_text)

    def icon_draw(self, icon):
        icon.stored_info.draw_hero_icon(self, icon.x, icon.y)

    def turn_on_info_bar(self, selected_icon):
        self.continue_button.on = True
        self.s_hero_text.text = selected_icon.stored_info.name

    def turn_off_info_bar(self):
        self.continue_button.on = False
        self.s_hero_text.text = ''
