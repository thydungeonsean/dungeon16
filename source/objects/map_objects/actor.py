from source.image.tilesets.sprite_archive import SpriteArchive
from source.objects.map_objects.map_object import MapObject
from source.objects.map_objects.mobility_component import MobilityComponent
from source.states.clock import Clock
from source.objects.effects.impact_effect import ImpactEffect


class Actor(MapObject):

    def __init__(self, (x, y), sprite):
        self.sprite = sprite
        MapObject.__init__(self, (x, y))

        self.actor_list = None
        self.mobility_component = MobilityComponent(self)

    def try_move(self, c):
        self.mobility_component.try_move(c)

    def set_level(self, level):
        self.level = level
        self.mobility_component.level = level
        self.actor_list = level.actors

    def set_images(self):
        return SpriteArchive.get_actor_tileset(self.sprite).tiles

    def get_image_key(self):
        return '_'.join((self.mobility_component.facing, Clock.get_instance().get_anikey(speed=3)))

    def move(self, coord):
        self.coord.set(coord)

    def bump(self, map_object):

        map_object.on_bump()
        if isinstance(map_object, Actor):
            self.hit_actor(map_object)
            map_object.die()

    def hit_actor(self, actor):

        imp = 'blunt_a_imp'

        p = actor.coord.get
        self.level.effects.add_effect(ImpactEffect(p, imp))

    def die(self):
        self.actor_list.remove_actor(self)
