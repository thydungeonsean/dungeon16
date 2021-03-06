from weakref import ref


class ActorList(object):

    def __init__(self, level):

        self.level = level

        self.player = None
        self.actors = []
        self.actor_coords = set()
        self.actor_map = {}

    def add_actor(self, actor):

        actor.set_level(self.level)

        self.actors.append(actor)
        self.actor_coords.add(actor.coord.get)
        self.actor_map[actor.coord.get] = ref(actor)

    def add_player(self, actor):
        self.add_actor(actor)
        self.player = ref(actor)

    def move_actor(self, actor, point):

        old = actor.coord.get
        self.actor_coords.remove(old)
        del self.actor_map[old]

        self.actor_coords.add(point)
        self.actor_map[point] = ref(actor)

    def remove_actor(self, actor):
        point = actor.coord.get
        self.actor_coords.remove(point)
        del self.actor_map[point]
        self.actors.remove(actor)

    def show_list(self):

        for actor in self.actors:
            print 'actor: %s, coord: %s' % (actor.profile['id'], str(actor.coord.get))
            print self.actor_map

