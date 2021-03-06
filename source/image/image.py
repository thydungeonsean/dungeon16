import pygame
from pygame.locals import *
from source.objects.pixel_coord import PixelCoord
from source.states.settings import Settings


class Image(object):

    def __init__(self, w, h, colorkey=False, alpha=False, auto_scale=True):

        self.image = pygame.Surface((w, h)).convert()
        self.rect = self.image.get_rect()
        self.coord = PixelCoord()
        self.coord.set_owner(self)
        self.coord.toggle_auto_position_owner()
        if colorkey:
            self.set_colorkey(colorkey)
        if alpha:
            self.set_alpha(alpha)
        if auto_scale:
            self.auto_scale()

    @property
    def w(self):
        return self.image.get_width()

    @property
    def h(self):
        return self.image.get_height()

    def set_colorkey(self, colorkey):
        self.image.set_colorkey(colorkey)

    def set_alpha(self, alpha):
        self.image.set_alpha(alpha)

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

    def auto_scale(self):
        self.scale_up(scale=Settings.SCALE)

    def get_blended_image(self, background_image, (x, y)):

        blended = Image(self.w, self.h)

        blended.image.fill((255, 0, 0))
        background_image.partial_draw(blended, area=(x, y, self.w, self.h))

        self.position((0, 0))
        self.draw(blended, special_flags=BLEND_MULT)

        blended.position((x, y))
        return blended
