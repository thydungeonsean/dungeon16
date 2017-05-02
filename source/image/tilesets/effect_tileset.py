from tileset import TileSet


class EffectTileSet(TileSet):

    def __init__(self, set_type, set_id):

        TileSet.__init__(self, 'effects', set_type, set_id)
        self.set_id = set_id
