from map_tileset import MapTileSet


class ShadowTileSet(MapTileSet):

    def __init__(self):
        MapTileSet.__init__(self, 'shadow', 'shadow')

    def get_base_tile(self, **kwargs):
        return 'shadow'

    def get_varied_tile(self, **kwargs):
        return self.get_base_tile(**kwargs)
