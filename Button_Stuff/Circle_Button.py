import math
from Button_Stuff.Buttons import button
import draw


def lineLength(pos1, pos2):
    x1, y1 = pos1
    x2, y2 = pos2
    x_squared = (x2 - x1) * (x2 - x1)
    y_squared = (y2 - y1) * (y2 - y1)
    length = math.sqrt(x_squared + y_squared)
    return length


class circle_button_appearance:
    def __init__(self, radius, normal_color, hovered_color, text_color):
        self.radius = radius
        self.normal_color = normal_color
        self.hovered_color = hovered_color
        self.text_color = text_color


class circle_button(button):
    def __init__(self, screen, x, y, appearance: circle_button_appearance, text: str = '', text_under: str = '',
                 dose_move: bool = False):
        self.radius = appearance.radius
        super().__init__(screen, x, y, appearance.normal_color, appearance.hovered_color, appearance.text_color,
                         text=text, text_under=text_under, dose_move=dose_move)
        self.text_under_height = self.radius / 2
        self.text_under_width = self.radius * 2

    def draw(self):
        if self.on:
            draw.circle(self.screen, self.border_color, (self.x, self.y), self.radius + self.border_width,
                        layer=self.layer)
            draw.circle(self.screen, self.color, (self.x, self.y), self.radius, layer=self.layer)
            if len(self.text) > 0:
                draw.text(self.screen, self.x, self.y, self.text, self.radius * 1.6, self.text_under_height, self.text_color,
                          in_center=True, layer=self.layer)
            if len(self.text_under) > 0:
                draw.text(self.screen, self.x, self.y + self.radius + self.text_under_height / 2 + 2, self.text_under,
                          self.text_under_width,
                          self.text_under_height - 2, self.text_color, in_center=True, layer=self.layer)

    def check_if_mouse_is_on(self, x, y):
        if lineLength((self.x, self.y), (x, y)) <= self.radius:
            self.hovered = True
        else:
            self.hovered = False
