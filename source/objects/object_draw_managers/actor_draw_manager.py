from object_draw_manager import ObjectDrawManager


class ActorDrawManager(ObjectDrawManager):

    def __init__(self, state):

        ObjectDrawManager.__init__(self, state)
        self.objects = None

    def init(self):
        self.objects = self.state.level.actors.actors

    def draw(self, surface):

        visible = filter(lambda x: self.view.object_in_view(x), self.objects)
        for obj in visible:
            obj.draw_to_map(surface, self.view)
