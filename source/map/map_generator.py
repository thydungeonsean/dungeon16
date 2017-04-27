from base_map import BaseMap
from random import *
import os


class MapGenerator(object):


    @classmethod
    def load_map(cls, filename):
        asset_path = ''.join((os.path.dirname(__file__), '\\..\\..\\assets\\maps\\', filename, '.txt'))
        f = open(asset_path, 'r')
        map_lines = []
        for line in f:
            if line.strip() == '':
                continue
            map_lines.append(list(line.rstrip()))
        f.close()

        h = len(map_lines)
        w = len(map_lines[0])
        map = [[map_lines[y][x] for y in range(h)] for x in range(w)]
        new = BaseMap(w, h)
        new.set_map(map)
        return new
