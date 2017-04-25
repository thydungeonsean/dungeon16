from map_tileset import MapTileSet


class FeatureTileSet(MapTileSet):

    def __init__(self):
        MapTileSet.__init__(self, 'feature', 'feature')
