import pygame


class Image(object):

    def __init__(self, w, h, colorkey=False):

        self.image = pygame.Surface((w, h)).convert()
        self.rect = self.image.get_rect()
        if colorkey:
            self.image.set_colorkey(colorkey)

    def position(self, (x, y)):
        self.rect.topleft = (x, y)

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def blit(self, image, rect):
        self.image.blit(image, rect)

    def scale_up(self, scale=2):

        scaled = pygame.transform.scale(self.image, (int(self.rect.w*scale), int(self.rect.h*scale)))
        self.image = scaled
        self.rect = self.image.get_rect()
