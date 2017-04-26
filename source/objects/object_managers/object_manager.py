

class ObjectManager(object):

    def __init__(self, state):

        self.state = state
        self.view = self.state.view

        self.coord_list = None
        self.object_map = None

    def get_coords(self):
        return self.coord_list

    def draw(self, surface):

        visible = filter(lambda x: self.view.object_in_view(x), self.get_coords())
        for coord in visible:
            self.object_map[coord].draw_to_map(surface, self.view)
