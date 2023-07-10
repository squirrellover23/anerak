import colors
import draw
from Screens.Screen import screen
from Profile import profile


class create_new_deck_start(screen):
    def __init__(self, screen_width: int, screen_height: int, profile: profile, user):
        super().__init__(screen_width, screen_height, profile, [draw.text_info('Select A Hero', 10, 150, 180, 60, colors.white), draw.text_info('Anerak', 35, 30, 150, 60, colors.white, False)], [], [], colors.black, user)
        self.rects += [draw.rect_ob(colors.black, 0, 20, screen_width, 70,
                                    gradient_stuff=[(0, 20, 0, 135), [(0, colors.black), (1, colors.light_grey)]]),
                       draw.poly_ob(colors.black, ((0, 20), (230, 20), (230, 90), (200, 120), (0, 120)),
                                    gradient_stuff=[(0, 20, 0, 135), [(0, colors.black), (1, colors.light_grey)]])]