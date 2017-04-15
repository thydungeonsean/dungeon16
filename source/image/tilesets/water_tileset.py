from map_tile_set import MapTileSet


class WaterTileSet(MapTileSet):

    edge_var = 'edge_ani'
    center_var = 'center_ani'

    deco_toggle_keys = ('lilypad', )

    deco_toggle_def = {
        'blue': ('lilypad',)
    }

    def __init__(self, set_id):
        MapTileSet.__init__(self, 'water', set_id)
        self.all_animated = self.set_all_animated()

        self.deco_toggles = self.set_deco_toggles()

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
            return WaterTileSet.edge_var
        return WaterTileSet.center_var

    def set_deco_toggles(self):

        cls = WaterTileSet

        deco_toggles = {}

        if self.set_id in cls.deco_toggle_def.keys():
            modify = cls.deco_toggle_def[self.set_id]
        else:
            modify = ()

        for key in cls.deco_toggle_keys:
            if key in modify:
                deco_toggles[key] = True
            else:
                deco_toggles[key] = False

        return deco_toggles
