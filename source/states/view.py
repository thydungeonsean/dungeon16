from source.objects.pixel_coord import PixelCoord
from settings import Settings


class View(object):

    # width and height are in tiles, and should be odd to allow for centering
    w = 25
    h = 17

    x_offset = -1 * ((w - 1) / 2) * Settings.SC_TILE_W
    y_offset = -1 * ((h - 1) / 2) * Settings.SC_TILE_H

    def __init__(self):

        self.map_image = None
        self.focused_object = None

        self.coord = self.init_coord()  # pixel_coord

    def init_coord(self):
        coord = PixelCoord()
        coord.set_x_offset(View.x_offset)
        coord.set_y_offset(View.y_offset)
        coord.set_owner(self)
        coord.toggle_auto_position_owner()
        return coord

    def reset_position(self):
        pass

    def focus_object(self, map_object):

        if self.focused_object is not None:
            self.focused_object.pixel_coord.unbind()

        self.focused_object = map_object
        self.focused_object.pixel_coord.bind(self.coord)

    def set_map_image(self, map_image):
        self.map_image = map_image
        self.coord.bind(self.map_image.coord)

    def deinit_map_image(self):
        self.coord.unbind()
        self.map_image = None

    def draw(self, surface):
        self.map_image.draw(surface)
        # feature_map.draw
        # object_manager.draw
        # actor_manager.draw
        # effect_manager.draw
