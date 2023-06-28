import draw
from Button_Stuff.Buttons import button


class rect_button_appearance:

    def __init__(self, width, height, normal_color, hovered_color, text_color):
        self.width = width
        self.height = height
        self.normal_color = normal_color
        self.hovered_color = hovered_color
        self.text_color = text_color


class rect_button(button):
    def __init__(self, screen, x, y, rect_appearance: rect_button_appearance, text: str = '', in_center: bool = False,
                 dose_move: bool = False):
        self.in_center = in_center
        super().__init__(screen, x, y, rect_appearance.normal_color, rect_appearance.hovered_color,
                         rect_appearance.text_color, text=text, dose_move=dose_move)
        self.width = rect_appearance.width
        self.height = rect_appearance.height
        self.alpha = 1

    def draw(self):
        if self.on:
            if self.in_center:
                draw.rect(self.screen, self.border_color, self.x, self.y, self.width + 2 * self.border_width,
                          self.height + 2 * self.border_width, layer=self.layer,
                          in_center=self.in_center, alpha=self.alpha)
            else:
                draw.rect(self.screen, self.border_color, self.x - self.border_width, self.y - self.border_width,
                          self.width + 2 *
                          self.border_width, self.height + 2 * self.border_width, layer=self.layer,
                          in_center=self.in_center, alpha=self.alpha)
            draw.rect(self.screen, self.color, self.x, self.y, self.width, self.height, layer=self.layer,
                      in_center=self.in_center, alpha=self.alpha)
            if len(self.text) > 0:
                if self.in_center:

                    draw.text(self.screen, self.x, self.y, self.text, self.width - 6, self.height - 2, self.text_color,
                              in_center=True, layer=self.layer)
                else:

                    draw.text(self.screen, self.x + self.width / 2, self.y + self.height / 2, self.text, self.width - 6,
                              self.height - 2,
                              self.text_color, in_center=True, layer=self.layer)

    def check_if_mouse_is_on(self, x, y):
        if self.in_center:
            if self.x - self.width / 2 <= x <= self.x + self.width / 2 and self.y - self.height / 2 <= y <= self.y + self.height / 2:
                self.hovered = True
            else:
                self.hovered = False
        else:
            if self.x <= x <= self.x + self.width and self.y <= y <= self.y + self.height:
                self.hovered = True
            else:
                self.hovered = False
