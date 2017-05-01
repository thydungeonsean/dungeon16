

class ActorList(object):

    def __init__(self, level):

        self.level = level

        self.actors = []
        self.actor_coords = set()
        self.actor_map = {}

    def add_actor(self, actor):

        actor.set_level(self.level)

        self.actors.append(actor)
        self.actor_coords.add(actor.coord.get)
        self.actor_map[actor.coord.get] = actor

    def move_actor(self, actor, point):

        old = actor.coord.get
        self.actor_coords.remove(old)
        del self.actor_map[old]

        self.actor_coords.add(point)
        self.actor_map[point] = actor

    def remove_actor(self, actor):

        point = actor.coord.get
        self.actor_coords.remove(point)
        del self.actor_map[point]
        self.actors.remove(actor)

