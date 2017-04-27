

class ObjectManager(object):

    def __init__(self, state):

        self.state = state
        self.view = self.state.view

        self.objects = None
        self.object_map = None

    def draw(self, surface):

        visible = filter(lambda x: self.view.coord_in_view(x), self.objects)
        for coord in visible:
            self.object_map[coord].draw_to_map(surface, self.view)
