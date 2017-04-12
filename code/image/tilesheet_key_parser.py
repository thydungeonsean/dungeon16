import os


asset_path = ''.join((os.path.dirname(__file__), '\\..\\..\\assets\\'))


def get_block(key_id, block_id):

    block_lines = []
    state = 0

    f = open(''.join((asset_path, key_id, '.txt')))
    for line in f:
    
        if state == 0 and line.rstrip() == ''.join((':', block_id, ':')):
            state = 1
            
        elif state == 1:
            if line.rstrip() == '[':
                pass
            elif line.rstrip() == ']':
                f.close()
                return block_lines
            else:
                block_lines.append(line.strip().lstrip('[').rstrip(']'))
    
    f.close()
    if not block_lines:
        raise Exception('no data for %s in %s' % (block_id, key_id))
    
    
# region block parsing funcions
def parse_block(block, block_type):

    if block_type == 'tuple':
        return parse_tuple_block(block)
    elif block_type == 'set':
        return parse_set_block(block)
    elif block_type == 'tile':
        return parse_tile_block(block)
    else:
        raise Exception('no valid block type for parse call')

    
def parse_tuple_block(block):  # parses single line blocks for data on tilesheet key
    return tuple(map(int, block[0].split(', ')))


def parse_set_block(block):
    parsed = []
    for line in block:
        parsed.append(parse_set_line(line))
    return parsed

    
def parse_set_line(line):
    split = list(map(str.strip, line.split(':')))
    key = split[0]
    row = int(split[1])
    x = int(split[2])
    return key, row, x
    

def parse_tile_block(block):
    parsed = []
    for line in block:
        parsed.append(parse_tile_line(line))
    return parsed   
    
    
def parse_tile_line(line):
    split = list(map(str.strip, line.split(':')))
    key = split[0]
    row = int(split[1])
    if len(split) == 3:
        x = int(split[2])
    else:
        x = 0
    return key, row, x
# end region


def get_key_line(parsed_block, key_id):
    for line in parsed_block:
        if line[0] == key_id:
            return line
    raise Exception('Tried to find invalid key: %s in tile_set block' % (key_id))
        

def get_set_keys_from_block(parsed_block):
    keys = []
    for line in parsed_block:
        keys.append(line[0])
    return keys


# combo functions
def get_sheet_dimentions(key_id):
    return parse_block(get_block(key_id, 'sheet_dim'), 'tuple')
    
    
def get_tile_dimensions(key_id):
    return parse_block(get_block(key_id, 'tile_dim'), 'tuple')
    
    
def get_colorkey(key_id):
    return parse_block(get_block(key_id, 'colorkey'), 'tuple')


def get_set_keys(key_id, block_id):
    return get_set_keys_from_block(parse_set_block(get_block(key_id, ''.join((block_id, ' sets')))))
