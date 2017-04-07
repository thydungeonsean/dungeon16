from ..tilesheet_key_parser import *
import pygame


class TileSet(object):

    def __init__(self, sheet, set_type, set_id):
        
        self.sheet_key = ''.join((sheet, '_key'))
        self.tilesheet = self.load_tile_sheet()
        
        self.tile_w, self.tile_h = self.load_tile_dimensions()
        
        self.set_dictionary = self.set_tileset_dictionary(set_type, set_id)
              
    def load_tile_sheet(self):
        raise NotImplementedError
        
    def load_tile_dimensions(self):
        return get_tile_dimensions(self.sheet_key)
        
    def set_tileset_dictionary(self, set_type, set_id):
        
        type_key = ''.join((set_type, ' sets'))
        type_block = parse_block(get_block(self.sheet_key, type_key), 'set')
        set_line = get_key_line(type_block, set_id)
        
        set_type_offset =  set_line[1:]
        
        print set_type_offset
        print self.tile_w
    
        
    def get_tile_image(self, tile_key):
        return
        
