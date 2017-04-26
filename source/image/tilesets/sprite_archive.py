from actor_tileset import ActorTileSet


class SpriteArchive(object):

    loaded_tilesets = {}

    @classmethod
    def get_tileset(cls, tileset_key):

        if tileset_key not in cls.loaded_tilesets.keys():
            cls.loaded_tilesets[tileset_key] = cls.generate_tileset(tileset_key)

        return cls.loaded_tilesets[tileset_key]

    @classmethod
    def generate_tileset(cls, tileset_key):
        return ActorTileSet(tileset_key)
