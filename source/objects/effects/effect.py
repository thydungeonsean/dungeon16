from source.objects.map_objects.map_object import MapObject
from source.image.tilesets.sprite_archive import SpriteArchive


class Effect(MapObject):

    def __init__(self, (x, y), effect_img):
        self.effect_img = effect_img
        MapObject.__init__(self, (x, y))

        self.block_move = False

    def set_images(self):
        return SpriteArchive.get_effect_tileset(self.effect_img).tiles

