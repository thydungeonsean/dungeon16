from random import randint

from source.image.tilesets.map_tilesets.map_tileset import MapTileSet


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

    def __init__(self):
        MapTileSet.__init__(self, 'deco', 'deco')

    def get_torch_tile(self, anikey):
        return ''.join(('torch_ani_', anikey))

    def get_torch_glow_tile(self, anikey):
        return ''.join(('torch_bot_ani_', anikey))
