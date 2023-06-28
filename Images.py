import colors

bianary_images = []
bianary_data = []


def convert_image_to_bites(filename):
    with open(filename, 'rb') as file:
        binaryData = file.read()
        return binaryData


class image:
    def __init__(self, image, x_offset, y_offset, scale, name):
        self.x_offset = x_offset
        self.y_offset = y_offset
        self.image = image

        self.zoom = 4
        self.scale = scale
        self.name = name
        bianary_images.append([name, x_offset, y_offset, scale])
        bianary_data.append(convert_image_to_bites(image))

    def draw_image(self, user, x, y, zoom, layer):
        self.update_image(zoom)
        user.add_draw_info([layer, 'image', [self.name, x, y, self.zoom]])

    def update_image(self, zoom):
        if self.zoom != zoom:
            self.zoom = zoom


oumaji_animal = image("images_folder/archer-1.png", -12, 2, 27, 'oumaji_animal')
