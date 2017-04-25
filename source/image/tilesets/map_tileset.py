from source.image.tilesets.tileset import TileSet


class MapTileSet(TileSet):

    def __init__(self, set_type, set_id):

        TileSet.__init__(self, 'world', set_type, set_id)
        self.set_type = set_type
        self.set_id = set_id
