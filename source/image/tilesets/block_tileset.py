from source.image.tilesets.map_tileset import MapTileSet
from random import randint


class BlockTileSet(MapTileSet):

    candle = 4
    stalagtite = 2
    jars = 2
    statue = 3
    tree = 2
    mushroom = 3
    altar = 2

    @classmethod
    def get_any_candle(cls):
        return '_'.join(('candle', str(randint(1, cls.candle)), 'ani'))

    @classmethod
    def get_any_mushroom(cls):
        return ''.join(('mushroom_', str(randint(1, cls.mushroom))))

    @classmethod
    def get_any_tree(cls):
        return ''.join(('tree_', str(randint(1, cls.tree))))

    @classmethod
    def get_any_stalagtite(cls):
        return ''.join(('stalagtite_', str(randint(1, cls.stalagtite))))

    @classmethod
    def get_any_statue(cls):
        return ''.join(('statue_', str(randint(1, cls.statue))))

    @classmethod
    def get_any_jars(cls):
        return ''.join(('jars_', str(randint(1, cls.jars))))

    @classmethod
    def get_any_altar(cls):
        return ''.join(('altar_', str(randint(1, cls.altar))))

    def __init__(self):
        MapTileSet.__init__(self, 'block', 'block')

