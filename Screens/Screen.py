import colors
import draw
from Profile import profile


class screen:
    all_screens = []

    def __init__(self, screen_width: int, screen_height: int, profile: profile, text: [draw.text_info], buttons, movement: list, color, user):
        self.profile = profile
        self.user = user
        self.screen_width = screen_width
        self.screen_height = screen_height

        self.reset_x = 0
        self.reset_y = 0
        self.update_screen = 3
        self.x = 0
        self.y = 0
        self.zoom = 1
        self.speed = 4
        self.lower_bound = screen_height
        self.right_bound = screen_width

        self.change_zoom = 0
        self.change_y = 0
        self.change_x = 0
        self.background_color = color
        self.images = []
        self.menus = []
        self.rects = [draw.rect_ob(colors.light_grey, 0, 0, screen_width, 20)]
        self.text_on_screen = text + [draw.text_info('Mages of the Mountain', 3, 0, screen_width, 15, colors.black, font_variation='850', small_caps=True)]
        self.movement = movement
        self.buttons = buttons
        self.current_menu = None
        self.button_clicked = False
        self.draw_info = []

    def button_mouse_motion(self, mouse_pos, screen_pos, zoom):
        new_pos = [(mouse_pos[0] - screen_pos[0]) / zoom, (mouse_pos[1] - screen_pos[1]) / zoom]
        self.update_screen = 2
        if self.current_menu is not None:
            self.current_menu.button_mouse_motion(mouse_pos, new_pos)
        else:
            for i in self.buttons:
                if i.on:
                    i.handle_mouse_motion(mouse_pos, new_pos)

    def handle_text_typed(self, text):
        pass

    def handle_mouse_click(self, mouse_pos, screen_pos, zoom):
        self.update_screen = 2

        if self.current_menu is not None:
            self.current_menu.handle_mouse_click()
        else:
            for i in self.buttons:
                if i.on:
                    i.handle_mouse_click()

    def draw_screen(self):
        self.draw_info = []
        if self.current_menu is not None:
            self.current_menu.draw()
        else:
            draw.fill_window(self, self.background_color)
            for r in self.rects:
                r.draw(self)
            for i in self.text_on_screen:
                i.draw_text(self)
            for i in self.buttons:
                i.draw()
        return self.draw_info


# this is a thing
pass





















