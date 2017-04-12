from map_tile_set import MapTileSet


class ShadowTileSet(MapTileSet):

    def __init__(self, set_id):
        MapTileSet.__init__(self, 'shadow', set_id)
        # set alpha
        self.tiles['shadow'].image.set_alpha(100)

    def get_base_tile(self, **kwargs):
        return 'shadow'

    def get_varied_tile(self, **kwargs):
        return self.get_base_tile(**kwargs)
