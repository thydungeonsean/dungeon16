

class Settings(object):

    SCALE = 2
    TILE_W = 16
    TILE_H = 16

    @classmethod
    def set_scate(cls, scale):
        cls.SCALE = scale
        # rescale all images