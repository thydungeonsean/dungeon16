from object_manager import ObjectManager


class ActorManager(ObjectManager):

    def __init__(self, state):

        ObjectManager.__init__(self, state)

    def init(self):
        self.objects = self.state.level.actors.actors

    def draw(self, surface):

        visible = filter(lambda x: self.view.object_in_view(x), self.objects)
        for obj in visible:
            obj.draw_to_map(surface, self.view)
