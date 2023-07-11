import colors
import draw
from Button_Stuff.Rect_Button import rect_button, rect_button_appearance
from Screens.Screen import screen
from Profile import profile

change_page_ap = rect_button_appearance(90, 30, colors.light_blue, colors.hov_light_blue, colors.white)


class change_page_button(rect_button):
    def __init__(self, screen: screen, x, text, page_diff):
        super().__init__(screen, x, screen.screen_height - 60, change_page_ap, text)
        self.page_diff = page_diff
        self.inactive_color = colors.dark_grey

    def command(self):
        self.screen.change_page(self.page_diff)


class icon(rect_button):
    def __init__(self, screen, x, y, icon_ap):
        super().__init__(screen, x, y, icon_ap)
        self.stored_info = None
        self.selected = False
        self.selected_b_width = 3

    def draw(self):
        if self.stored_info is not None:
            if self.selected:
                draw.rect(self.screen, colors.blue, self.x, self.y, self.width, self.height, self.selected_b_width)
            self.screen.icon_draw(self)

    def change_info(self, info):
        self.stored_info = info
        self.selected = False

    def command(self):
        if self.stored_info is not None:
            self.screen.select_icon(self)


class icon_information:
    def __init__(self, rows, cols, icon_start_x, icon_start_y, icon_width, icon_height, icon_distance_x, icon_distance_y):
        self.rows, self.cols, self.start_x, self.start_y, self.width, self.height, self.distance_x, self.distance_y = rows, cols, icon_start_x, icon_start_y, icon_width, icon_height, icon_distance_x, icon_distance_y


class page_screen(screen):
    def __init__(self, screen_width: int, screen_height: int, profile: profile, user, text: [draw.text_info], buttons, movement: list, color, list_of_info_for_icons,
                 icon_info: icon_information, page_buttons_x):

        super().__init__(screen_width, screen_height, profile, text, buttons, movement, color, user)
        icon_ap = rect_button_appearance(icon_info.width, icon_info.height, colors.white, colors.white, colors.white)
        self.rows = icon_info.rows
        self.cols = icon_info.cols
        self.icons_per_page = self.rows * self.cols
        self.page_on = 1
        self.info_for_icons = list_of_info_for_icons
        self.total_pages = int(len(self.info_for_icons) / self.icons_per_page + .999)
        if self.total_pages == 0:
            self.total_pages = 1

        self.page_text = draw.text_info(f'Page {self.page_on} of {self.total_pages}', page_buttons_x,
                                        screen_height - 130, 100, 50, colors.white)
        self.text_on_screen.append(self.page_text)
        self.previous_page_b = change_page_button(self, page_buttons_x - 40, 'Previous', -1)
        self.next_page_b = change_page_button(self, page_buttons_x + 60, 'Next', 1)
        self.buttons += [self.next_page_b, self.previous_page_b]

        self.selected_icon = None
        self.icons = []
        for row in range(self.rows):
            for col in range(self.cols):
                self.icons.append(icon(self, icon_info.start_x + col * (icon_info.width + icon_info.distance_x), icon_info.start_y + row* (icon_info.height + icon_info.distance_y), icon_ap))
        self.buttons += self.icons
        self.change_page(0)

    def select_icon(self, s_icon: icon):
        if self.selected_icon == s_icon:
            s_icon.selected = False
            self.selected_icon = None
            self.turn_off_info_bar()
        else:
            if self.selected_icon is not None:
                self.selected_icon.selected = False
            self.selected_icon = s_icon
            self.selected_icon.selected = True
            self.turn_on_info_bar(self.selected_icon)

    def turn_on_info_bar(self, selected_icon):
        pass

    def turn_off_info_bar(self):
        pass

    def icon_draw(self, icon):
        pass

    def check_page_buttons(self):
        if self.page_on == 1:
            self.previous_page_b.active = False
        else:
            self.previous_page_b.active = True
        if self.page_on == self.total_pages:
            self.next_page_b.active = False
        else:
            self.next_page_b.active = True

        self.previous_page_b.hover_update()
        self.next_page_b.hover_update()

    def change_page(self, page_diff):
        self.page_on += page_diff
        self.check_page_buttons()
        self.page_text.text = f'Page {self.page_on} of {self.total_pages}'
        start_d_index = (self.page_on - 1) * self.icons_per_page

        for d in range(start_d_index, start_d_index + self.icons_per_page):
            if d >= len(self.info_for_icons):
                self.icons[d % self.icons_per_page].change_info(None)
            else:
                self.icons[d % self.icons_per_page].change_info(self.info_for_icons[d])
