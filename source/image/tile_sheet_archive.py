import os
import pygame


class TileSheetArchive(object):

    sheets = {}

    @classmethod
    def load_sheet(cls, key):
        path = ''.join((os.path.dirname(__file__), '..\\..\\..\\assets\\', key, '.png'))
        return pygame.image.load(path)

    @classmethod
    def get_tilesheet(cls, key):

        if key not in cls.sheets.keys():
            cls.sheets[key] = cls.load_sheet(key)

        return cls.sheets[key]
