from source.objects.map_objects.map_object import MapObject
from source.objects.mobility_component import MobilityComponent
from source.image.tilesets.sprite_archive import SpriteArchive
from source.states.clock import Clock


class Actor(MapObject):

    def __init__(self, (x, y), sprite):
        self.sprite = sprite
        MapObject.__init__(self, (x, y))
        self.mobility_component = MobilityComponent(self)

    def move(self, c):
        self.mobility_component.move(c)

    def set_images(self):
        return SpriteArchive.get_tileset(self.sprite).tiles

    def get_image_key(self):
        return '_'.join((self.mobility_component.facing, Clock.get_instance().get_anikey(speed=4)))
