from map_tile_set import MapTileSet


class WaterTileSet(MapTileSet):

    edge_var = 'edge_ani'
    center_var = 'center_ani'

    def __init__(self, set_id):
        MapTileSet.__init__(self, 'water', set_id)
        self.all_animated = self.set_all_animated()

    def set_all_animated(self):
        if self.set_id in ('blue', 'sewer'):
            return True
        return False

    def get_base_tile(self, **kwargs):
        if self.all_animated:
            return self.get_varied_tile(**kwargs)
        elif kwargs.get('edge', False):
            return 'edge'
        return 'center'

    def get_varied_tile(self, **kwargs):
        if kwargs.get('edge', False):
            return WaterTileSet.edge_var+'_a'
        return WaterTileSet.center_var+'_a'
