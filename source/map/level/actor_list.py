

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

