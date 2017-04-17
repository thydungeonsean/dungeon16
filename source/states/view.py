from source.objects.coord import Coord


class View(object):

    w = 25
    h = 17

    def __init__(self):

        self.map_image = None

        self.coord = Coord()

    def bind_view(self, map_object):
        self.coord.unbind()
        self.coord.bind(map_object.coord)

    def set_map_image(self, map_image):
        self.map_image = map_image
        self.map_image.coord.bind(self.coord)

    def deinit_map_image(self):
        self.map_image.coord.unbind()
        self.map_image = None

    def draw(self, surface):
        self.map_image.draw(surface)
        # feature_map.draw
        # object_manager.draw
        # actor_manager.draw
        # effect_manager.draw