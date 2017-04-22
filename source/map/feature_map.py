

class FeatureMap(object):

    def __init__(self, base_map):
        self.base_map = base_map

        self.feature_map = {}
        self.feature_coords = []

    def add_feature(self, point, feature):
        self.feature_map[point] = feature
        self.feature_coords.append(point)
