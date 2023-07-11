import colors

'''
Gradient Stuff for all draw functions goes as this
[
    (start_x, start_y, finish_x, finish_y),     
    [
        (0, color1),
        any number of (int in range 0.0 - 1.0, color),
        (1, color2)
    ] 
]

'''


def fill_window(screen, color):
    screen.draw_info.append([1, 'fill_screen', [list(color)]])


class text_info:
    def __init__(self, text, x, y, width, height, color, in_center: bool = False, does_move: bool = False,
                 background_color=None, font_variation: str = 'normal', small_caps: bool = False, gradient_stuff=None):

        if gradient_stuff is None:
            gradient_stuff = []
        self.grad_stuff = gradient_stuff
        self.text = text
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.in_center = in_center
        self.layer = 2
        self.background_color = 0
        self.font_var = font_variation
        self.small_c = small_caps
        if background_color is not None:
            self.background_color = background_color
        if does_move:
            self.layer = 1
        self.on = True

    def draw_text(self, screen):
        if self.on:
            text(screen, self.x, self.y, self.text, self.width, self.height, self.color,
                 background_color=self.background_color, in_center=self.in_center, layer=self.layer, font_variation=self.font_var, small_caps=self.small_c, gradient_stuff=self.grad_stuff)


def text(screen, x, y, text_str, width: int, height: int, color, background_color=0, in_center: bool = False,
         alpha: float = 1, layer: int = 1, font_variation: str = 'normal', small_caps: bool = False,
         gradient_stuff=None):
    if gradient_stuff is None:
        gradient_stuff = []
    if in_center:
        center = 'true'
    else:
        center = 'false'
    sc = ''
    if small_caps:
        sc = 'small-caps '
    screen.draw_info.append(
        [layer, 'text', [text_str, [x, y, width, height], list(color) + [alpha], background_color, center, [font_variation, sc], gradient_stuff]])


class rect_ob:
    def __init__(self, color, x, y, width, height, border_width: int = 0, alpha: float = 1, layer: int = 1,
                 in_center: bool = False, gradient_stuff=None):
        self.color, self.x, self.y, self.width, self.height, self.border_width, self.alpha, self.layer, self.in_center = color, x, y, width, height, border_width, alpha, layer, in_center
        if gradient_stuff is None:
            gradient_stuff = []
        self.grad_stuff = gradient_stuff
        self.on = True

    def draw(self, screen):
        if self.on:
            rect(screen, self.color, self.x, self.y, self.width, self.height, self.border_width, self.alpha, self.layer, self.in_center, self.grad_stuff)


def rect(screen, color, x, y, width, height, border_width: int = 0, alpha: float = 1, layer: int = 1,
         in_center: bool = False, gradient_stuff=None):
    if gradient_stuff is None:
        gradient_stuff = []
    screen.draw_info.append([layer, 'rect', [[x, y, width, height], list(color) + [alpha], border_width, in_center, gradient_stuff]])


def circle(screen, color, center, radius: float, width: int = 0, alpha: float = 1, layer: int = 1, gradient_stuff=None):
    if gradient_stuff is None:
        gradient_stuff = []
    screen.draw_info.append([layer, 'circle', [list(center), radius, list(color) + [alpha], width, gradient_stuff]])


class poly_ob:
    def __init__(self, color, points, width: int = 0, alpha: float = 1, layer: int = 1, gradient_stuff=None):
        self.color, self.points, self.width, self.alpha, self.layer = color, points, width, alpha, layer
        if gradient_stuff is None:
            gradient_stuff = []
        self.grad_stuff = gradient_stuff
        self.on = True

    def draw(self, screen):
        if self.on:
            polygon(screen, self.color, self.points, self.width, self.alpha, self.layer, self.grad_stuff)


def polygon(screen, color, points, width: int = 0, alpha: float = 1, layer: int = 1, gradient_stuff=None):
    if gradient_stuff is None:
        gradient_stuff = []
    screen.draw_info.append([layer, 'poly', [points, list(color) + [alpha], width, gradient_stuff]])


def ellipse(screen, color, rect, alpha: float = 1, width: int = 0, layer: int = 1, gradient_stuff=None):
    if gradient_stuff is None:
        gradient_stuff = []
    screen.draw_info.append([layer, 'ellipse', [list(rect), list(color) + [alpha], width, gradient_stuff]])
