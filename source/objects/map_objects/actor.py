from source.image.tilesets.sprite_archive import SpriteArchive
from source.objects.map_objects.map_object import MapObject
from source.objects.map_objects.mobility_component import MobilityComponent
from source.objects.map_objects.ai.ai_archive import AIArchive
from source.states.clock import Clock
from source.objects.effects.impact_effect import ImpactEffect
from source.objects.effects.animation_effect import *

from source.states.message_system.message import Message


class Actor(MapObject):

    def __init__(self, (x, y), sprite):
        self.sprite = sprite
        MapObject.__init__(self, (x, y))

        self.profile = self.set_profile()

        self.actor_list = None
        self.mobility_component = MobilityComponent(self)
        self.stat_component = None
        self.ai = self.init_ai()

    def init_ai(self):
        return AIArchive.get_ai(self, 'basic')

    def set_level(self, level):
        self.level = level
        self.mobility_component.set_level(level)
        self.ai.set_level(level)
        self.actor_list = level.actor_list

    def set_images(self):
        return SpriteArchive.get_actor_tileset(self.sprite).tiles

    def get_image_key(self):
        return '_'.join((self.mobility_component.facing, Clock.get_instance().get_anikey(speed=3)))

    def set_profile(self):
        return {}

    def move(self, coord):
        print self.profile['id'] + ' move from ' + str(self.coord.get) + ' to ' + str(coord)
        self.actor_list.move_actor(self, coord)
        self.coord.set(coord)
        self.report_move()

    def report_move(self):
        Message('actor_move').send()

    def bump(self, map_object):

        map_object.on_bump()
        if isinstance(map_object, Actor):
            self.hit_actor(map_object)
            map_object.take_hit()
            # map_object.die()

    def hit_actor(self, actor):

        imp = 'blunt_a_imp'

        p = actor.coord.get
        self.level.effects.add_effect(ImpactEffect(p, imp))

    def take_hit(self):
        self.level.effects.add_effect(Shake(self))

    def die(self):
        self.ai.deinit()
        self.actor_list.remove_actor(self)
        self.report_death()

    def report_death(self):
        Message('actor_die', *self.profile.items()).send()
