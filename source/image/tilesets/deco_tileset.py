from source.image.tilesets.map_tileset import MapTileSet
from random import randint


class DecoTileSet(MapTileSet):

    gore = 5
    bones = 3
    tuft = 5
    root = 5
    lilypad = 4

    @classmethod
    def get_any_gore(cls):
        return ''.join(('gore_', str(randint(1, cls.gore))))

    @classmethod
    def get_any_bones(cls):
        return ''.join(('bones_', str(randint(1, cls.bones))))

    @classmethod
    def get_any_tuft(cls):
        return ''.join(('tuft_', str(randint(1, cls.tuft))))

    @classmethod
    def get_any_root(cls):
        return ''.join(('root_', str(randint(1, cls.root))))

    @classmethod
    def get_any_lilypad(cls):
        return ''.join(('lilypad_', str(randint(1, cls.lilypad)), '_ani'))

    def __init__(self, set_id):
        MapTileSet.__init__(self, 'deco', set_id)

    def get_torch_tile(self, anikey):
        return ''.join(('torch_ani_', anikey))

    def get_torch_glow_tile(self, anikey):
        return ''.join(('torch_bot_ani_', anikey))
