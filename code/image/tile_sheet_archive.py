

class TileSheetArchive(object):

    world_sheet = None

    @classmethod
    def load_world_sheet(cls):
        path = ''.join((os.path.dirname(__file__), ccc'..\\assets\\world.png'))
        cls.world_sheet = pygame.image.load(path)