import draw
from Global import screen_height, screen_width
from Button_Stuff.Rect_Button import rect_button_appearance, rect_button
import colors

blue_rect_bstyle = rect_button_appearance(200, 50, colors.light_blue, colors.hov_light_blue, colors.white)
small_grey_bstyle = rect_button_appearance(100, 50, colors.light_grey, colors.white, colors.grey)


class confirmM_button(rect_button):
    def __init__(self, menu):
        self.menu = menu
        super().__init__(menu, menu.topL_x + menu.width - 205, menu.topL_y + menu.height - 55, blue_rect_bstyle, 'Confirm')

    def command(self):
        self.menu.confirm_command()


class closeM_button(rect_button):
    def __init__(self, menu):
        self.menu = menu
        super().__init__(menu, menu.topL_x + 5, menu.topL_y + menu.height - 55, small_grey_bstyle, 'Back')

    def command(self):
        self.menu.screen.current_menu = None
        self.menu.screen.draw_screen()


class menu:
    def __init__(self, screen, x, y, width: int, height: int, text_on_menu, color, buttons: list, confirm_action: bool = False, in_center: bool = False, border_color=None, border_width: int = 6):
        self.x = x
        self.y = y
        self.topL_x = x
        self.topL_y = y
        self.width = width
        self.height = height
        self.in_center = in_center
        if in_center:
            self.topL_x = x - self.width/2
            self.topL_y = y - self.height/2
        self.color = color
        self.text_on_menu = text_on_menu
        self.border_color = border_color
        self.border_width = border_width
        self.close_b = closeM_button(self)
        self.buttons = buttons
        self.buttons.append(self.close_b)
        self.right_bound = screen_width
        self.lower_bound = screen_height
        self.screen = screen
        self.confirm = confirm_action
        self.confirm_b = confirmM_button(self)
        if self.confirm:
            self.buttons.append(self.confirm_b)
        else:
            self.confirm_b.on = False

    def confirm_command(self):
        pass

    def draw(self):
        if self.border_color is not None:
            draw.rect(self.border_color, self.topL_x - self.border_width, self.topL_y - self.border_width, self.width + 2 * self.border_width, self.height + 2 * self.border_width, layer=2)
            draw.rect(self.color, self.topL_x, self.topL_y, self.width, self.height, layer=2)
        for i in self.text_on_menu:
            i.draw_text()
        for i in self.buttons:
            if i.on:
                i.draw()

    def button_mouse_motion(self, mouse_pos, new_pos):
        for i in self.buttons:
            if i.on:
                i.handle_mouse_motion(mouse_pos, new_pos)

    def handle_mouse_click(self):
        for i in self.buttons:
            if i.on:
                i.handle_mouse_click()
