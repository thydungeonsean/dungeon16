from actor_tileset import ActorTileSet
from effect_tileset import EffectTileSet


class SpriteArchive(object):

    loaded_tilesets = {}

    @classmethod
    def get_actor_tileset(cls, tileset_key):

        if tileset_key not in cls.loaded_tilesets.keys():
            cls.loaded_tilesets[tileset_key] = cls.generate_actor_tileset(tileset_key)

        return cls.loaded_tilesets[tileset_key]

    @classmethod
    def generate_actor_tileset(cls, tileset_key):
        return ActorTileSet(tileset_key)

    @classmethod
    def get_effect_tileset(cls, tileset_key):

        if tileset_key not in cls.loaded_tilesets.keys():
            cls.loaded_tilesets[tileset_key] = cls.generate_effect_tileset(tileset_key)

        return cls.loaded_tilesets[tileset_key]

    @classmethod
    def generate_effect_tileset(cls, tileset_key):

        if tileset_key.endswith('_bolt'):
            set_type = 'bolt'
        elif tileset_key.endswith('_magic'):
            set_type = 'magic'
        elif tileset_key.endswith('_arrow'):
            set_type = 'arrow'
        elif tileset_key.endswith('_imp'):
            set_type = 'impact'
        else:
            set_type = 'special'

        return EffectTileSet(set_type, tileset_key)
