from map_tileset import MapTileSet


class DoorTileSet(MapTileSet):

    def __init__(self, set_id):
        MapTileSet.__init__(self, 'door', set_id)
