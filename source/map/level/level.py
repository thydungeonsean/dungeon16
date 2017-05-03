from source.map.level.actor_list import ActorList
from source.map.level.fov_map import FOVMap
from source.map.feature_map import FeatureMap
from effect_runner import EffectRunner


class Level(object):

    def __init__(self):

        self.base_map = None
        self.map_image = None

        self.actors = ActorList(self)
        self.feature_map = FeatureMap(self)
        self.effects = EffectRunner(self)

        self.fov_map = None

    def set_base_map(self, base_map):
        self.base_map = base_map

    def set_map_image(self, map_image):
        self.map_image = map_image

    def init_fov_map(self):
        self.fov_map = FOVMap(self)
