

class ObjectManager(object):

    def __init__(self, state):

        self.state = state
        self.view = self.state.view

        self.coord_list = None
        self.object_map = None

    def draw(self, surface):

        visible = filter(lambda x: self.view.object_in_view(x), self.coord_list)
        for coord in visible:
            self.object_map[coord].draw(surface)
