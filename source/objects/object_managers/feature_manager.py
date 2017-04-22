from object_manager import ObjectManager


class FeatureManager(ObjectManager):

    def __init__(self, state):

        ObjectManager.__init__(self, state)

    def init(self):
        self.coord_list = self.state.level.feature_map.feature_coords
        self.object_map = self.state.level.feature_map.feature_map
