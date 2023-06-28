import colors


class button:
    def __init__(self, screen, x, y,  norm_color, hov_color, text_color, text: str = '', text_under: str = '', dose_move: bool = False):
        self.x = x
        self.y = y
        self.text = text
        self.text_under = text_under
        self.screen = screen
        self.normal_color = norm_color
        self.hovered_color = hov_color
        self.text_color = text_color
        self.color = self.normal_color
        self.layer = 2
        if dose_move:
            self.layer = 1
        self.border_width = 2
        self.default_border_color = colors.white
        self.border_color = self.default_border_color
        self.hovered = False
        self.active = True
        self.on = True
        self.hov_before = False
        self.hov_change = False
        self.inactive_color = colors.black
        self.inactive_border_color = colors.grey

    def update_attributes(self, x_to: int = None, y_to: int = None, border_color=None, text: str = None,
                          text_color=None):
        if x_to is not None:
            self.x = x_to
        if y_to is not None:
            self.y = y_to
        if text_color is not None:
            self.text_color = text_color
        if border_color is not None:
            self.border_color = border_color
        if text is not None:
            self.text = text

    def draw(self):
        pass

    def hover_update(self):
        if not self.active:
            self.color = self.inactive_color
            self.border_color = self.inactive_border_color
        elif self.hovered:
            self.color = self.hovered_color
            self.border_color = self.default_border_color
        else:
            self.color = self.normal_color
            self.border_color = self.default_border_color

    def check_if_mouse_is_on(self, x, y):
        self.hovered = False

    def handle_mouse_motion(self, mouse_pos, new_pos):
        if self.on:
            if self.active:
                if self.layer == 2:
                    x = mouse_pos[0]
                    y = mouse_pos[1]
                else:
                    x = new_pos[0]
                    y = new_pos[1]
                self.check_if_mouse_is_on(x, y)
                if not self.hovered == self.hov_before:
                    self.hover_update()
                    self.draw()
                    self.hov_before = self.hovered
            else:
                self.hover_update()

    def handle_mouse_click(self):
        if self.active:
            if self.hovered:
                self.command()
                self.screen.button_clicked = True
                self.hovered = False
                self.hover_update()

    def command(self):
        pass



