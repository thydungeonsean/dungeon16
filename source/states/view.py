from source.objects.pixel_coord import PixelCoord
from source.objects.coord import Coord
from settings import Settings
import pygame


class View(object):

    # width and height are in tiles, and should be odd to allow for centering
    w = 25
    h = 17

    x_offset = -1 * ((w - 1) / 2) * Settings.SC_TILE_W
    y_offset = -1 * ((h - 1) / 2) * Settings.SC_TILE_H

    def __init__(self, state):

        self.state = state
        self.feature_manager = None
        self.actor_manager = None

        self.view_surface = self.init_view_surface()
        self.view_rect = self.view_surface.get_rect()

        self.map_image = None
        self.focused_object = None

        self.pixel_coord = self.init_pixel_coord()
        self.coord = self.init_coord()
        self.pixel_coord.bind(self.coord)

    def init_pixel_coord(self):
        coord = PixelCoord()
        coord.set_x_offset(View.x_offset)
        coord.set_y_offset(View.y_offset)
        coord.set_owner(self)
        coord.toggle_auto_position_owner()
        return coord

    def init(self):
        self.feature_manager = self.state.feature_manager

    def init_coord(self):  # the nearest map coord of the topleft corner of view
        coord = Coord()
        return coord

    def init_view_surface(self):
        return pygame.Surface((View.w*Settings.SC_TILE_W, View.h*Settings.SC_TILE_H)).convert()

    def reset_position(self):
        pass

    def focus_object(self, map_object):

        if self.focused_object is not None:
            self.focused_object.pixel_coord.unbind()

        self.focused_object = map_object
        self.focused_object.pixel_coord.bind(self.pixel_coord)

    def set_map_image(self, map_image):
        self.map_image = map_image
        self.pixel_coord.bind(self.map_image.coord)

    def deinit_map_image(self):
        self.pixel_coord.unbind()
        self.map_image = None

    def draw(self, surface):
        self.view_surface.fill((0, 0, 0))
        self.map_image.draw(self.view_surface)

        self.feature_manager.draw(self.view_surface)
        # object_manager.draw
        # actor_manager.draw
        # effect_manager.draw

        surface.blit(self.view_surface, self.view_rect)

    def object_in_view(self, (mx, my)):

        vx, vy = self.coord.get

        x = mx - vx
        y = my - vy

        return 0 < x < 5 and 0 < y < 5
