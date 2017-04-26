from tileset import TileSet


class ActorTileSet(TileSet):

    def __init__(self, set_id):

        TileSet.__init__(self, 'monsters', 'sprite', set_id)
        self.set_id = set_id
