white = (255, 255, 255)
brown = (139, 69, 19)
yellow = (255, 255, 0)
black = (0, 0, 0)
pink = (255, 120, 120)

green = (50, 200, 0)
light_green = (100, 250, 50)

dark_red = (200, 0, 0)
red = (250, 0, 0)
light_red = (255, 100, 100)
hov_red = (255, 40, 40)

grey = (70, 70, 70)
dark_grey = (20, 20, 20)
light_grey = (200, 200, 200)
hov_light_grey = (240, 240, 240)
silver = (120, 120, 120)
mountain_grey = (100, 100, 100)
mid_grey = (110, 110, 110)

light_blue = (0, 100, 255)
hov_light_blue = (50, 180, 255)
blue = (0, 0, 250)
unexplored_blue = (200, 220, 255)
water_blue = (105, 203, 245)
ocean_blue = (75, 147, 255)


def lighten_or_darken(color, change_in_color):
    new_color = []
    for i in color:
        c = i + change_in_color
        if c > 255:
            c = 255
        elif c < 0:
            c = 0
        new_color.append(c)

    return new_color
