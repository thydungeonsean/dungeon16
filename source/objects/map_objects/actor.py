from source.objects.map_objects.map_object import MapObject
from source.objects.mobility_component import MobilityComponent
from source.image.tilesets.sprite_archive import SpriteArchive


class Actor(MapObject):

    def __init__(self, (x, y), sprite):
        self.sprite = sprite
        MapObject.__init__(self, (x, y))
        self.mobility_component = MobilityComponent(self)

    def move(self, c):
        self.mobility_component.move(c)

    def set_images(self):
        return SpriteArchive.get_tileset(self.sprite)

    def get_image_key(self):
        return 'down_a'
