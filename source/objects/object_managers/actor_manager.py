from object_manager import ObjectManager


class ActorManager(ObjectManager):

    def __init__(self, state):

        ObjectManager.__init__(self, state)
        self.actors = []

    def init(self):
        self.coord_list = self.state.level.feature_map.feature_coords
        self.object_map = self.state.level.feature_map.feature_map

    def get_coords(self):
        return [x.coord.get for x in self.actors]
