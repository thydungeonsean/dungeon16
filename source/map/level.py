from base_map import BaseMap


class Level(object):

    def __init__(self):

        self.base_map = None
        self.map_image = None

    def set_base_map(self, base_map):
        self.base_map = base_map

    def set_map_image(self, map_image):
        self.map_image = map_image

