

class FeatureMap(object):

    def __init__(self, level):
        self.level = level
        self.base_map = level.base_map

        self.feature_map = {}
        self.feature_coords = []

    def add_feature(self, point, feature):

        feature.set_level(self.level)

        self.feature_map[point] = feature
        self.feature_coords.append(point)
