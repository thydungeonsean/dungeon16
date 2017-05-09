import source.map.dijkstra_maps.dijkstra_map as dm
from time import time
from random import randint

from source.map.map_generator import MapGenerator


l = MapGenerator.load_map('map')

w = l.w
h = l.h


def f(self, (x, y)):

    return self.get_tile_code((x, y)) in ('.','~')

l.passable = f


m = dm.DijkstraMap(w, h, l, l.passable)

#src = [(5, 5), (5, 10), (15, 15), (7, 7), (0, 0), (3, 3), (40, 40)]

src = [(4, 3), (25, 25), (30, 10), (45, 16)]

t = time()
m.calculate(src)
print time()-t

m._print()
print m.count

import pygame

tw = 10

s = pygame.display.set_mode((800, 600))

image = pygame.Surface((w*tw, h*tw)).convert()

dot = pygame.Surface((tw, tw)).convert()
r = dot.get_rect()

for y in range(h):
    for x in range(w):
        col_v = m.d_map[x][y]
        if col_v > 255:
            col_v = 255
        col = (col_v, col_v, col_v)
        dot.fill(col)
        r.topleft = (x*tw, y*tw)
        image.blit(dot, r)


s.blit(image, image.get_rect())
pygame.display.update()

while True:
    x = pygame.event.wait()
    if x.type == pygame.KEYDOWN:
        break
