from map_tileset import MapTileSet


class PitTileSet(MapTileSet):

    def __init__(self, set_id):
        MapTileSet.__init__(self, 'pit', set_id)

    def get_base_tile(self, **kwargs):
        if kwargs.get('edge', False):
            return 'edge'
        return 'pit'

    def get_varied_tile(self, **kwargs):
        return self.get_base_tile(**kwargs)
