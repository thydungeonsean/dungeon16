from object_draw_manager import ObjectDrawManager


class FeatureDrawManager(ObjectDrawManager):

    def __init__(self, state):

        ObjectDrawManager.__init__(self, state)
        self.objects = None
        self.object_map = None

    def init(self):
        self.objects = self.state.level.feature_map.feature_coords
        self.object_map = self.state.level.feature_map.feature_map

    def draw(self, surface):

        visible = filter(lambda x: self.view.coord_in_view(x), self.objects)
        for coord in visible:
            self.object_map[coord].draw_to_map(surface, self.view)
