import pygame
from pygame.locals import *
from source.objects.pixel_coord import PixelCoord


class Image(object):

    def __init__(self, w, h, colorkey=False):

        self.image = pygame.Surface((w, h)).convert()
        self.rect = self.image.get_rect()
        self.coord = PixelCoord()
        self.coord.set_owner(self)
        self.coord.toggle_auto_position_owner()
        if colorkey:
            self.image.set_colorkey(colorkey)

    @property
    def w(self):
        return self.image.get_width()

    @property
    def h(self):
        return self.image.get_height()

    def position(self, (x, y)):
        self.coord.set((x, y))

    def reset_position(self):
        x, y = self.coord.get
        self.rect.topleft = (x, y)

    def draw(self, surface, special_flags=0):
        surface.blit(self.image, self.rect, special_flags=special_flags)

    def blit(self, image, rect, special_flags=0):
        self.image.blit(image, rect, special_flags=special_flags)

    def partial_draw(self, surface, area=None, special_flags=0):
        surface.image.blit(self.image, (0, 0), area, special_flags=special_flags)

    def scale_up(self, scale=2):

        scaled = pygame.transform.scale(self.image, (int(self.rect.w*scale), int(self.rect.h*scale)))
        self.image = scaled
        self.rect = self.image.get_rect()

    def get_blended_image(self, background_image, (x, y)):

        blended = Image(self.w, self.h)

        blended.image.fill((255, 0, 0))
        background_image.partial_draw(blended, area=(x, y, self.w, self.h))

        self.position((0, 0))
        self.draw(blended, special_flags=BLEND_MULT)

        blended.position((x, y))
        return blended
