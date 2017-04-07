from ..tilesheet_key_parser import *
import pygame


class TileSet(object):

    def __init__(self, set_type, set_id):
        self.tilesheet = self.load_tile_sheet()
        
        
        
    
    def load_tile_sheet(self):
        raise NotImplementedError
        
    def get_tile_image(self, tile_key):
        return