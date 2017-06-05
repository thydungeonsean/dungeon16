from weakref import ref
from actions.action_assigner import ActionAssigner
from random import shuffle


class AIComponent(object):

    def __init__(self, owner):

        self.owner = ref(owner)
        self.level = None

        self.action = None

        self.state = 'active'

    def set_level(self, level):
        self.level = level

    def deinit(self):
        self.action = None
        self.state = 'dead'

    def dist_to_player(self):

        owner_x, owner_y = self.owner().coord.get
        player_x, player_y = self.level.actor_list.player().coord.get  # need to add player ref to actor_list
        return abs(owner_x - player_x) + abs(owner_y - player_y)

    def clear_action(self):
        self.action = None

    def run_action(self):
        if self.action is None:
            self.set_next_action()
            if self.action is None:
                return None
        return self.action.run()

    def set_next_action(self):
        if self.state == 'dead':
            return None
        elif self.state == 'active':
            next_action = self.attack_party()

            if next_action is None:
                next_action = ActionAssigner.get_action('wait')

            self.action = next_action

    def attack_party(self):

        current_coord = self.owner().coord.get
        adj = self.get_adj(current_coord)
        comparison_map = {}

        d_map = self.level.dijkstra_collection.access_map('party_walker')
        for point in adj:
            dijkstra_value = d_map.get_value(point)
            if dijkstra_value is not None:
                comparison_map[point] = dijkstra_value

        adj = comparison_map.keys()[:]
        if not adj:
            return None

        shuffle(adj)
        adj = sorted(adj, key=lambda x: comparison_map[x])

        for point in adj:

            action_packet = self.try_move(point)
            if action_packet is not None:
                action_key, action_args = action_packet
                action = ActionAssigner.get_action(action_key, *action_args)
                return action

    @staticmethod
    def get_adj((x, y)):
        return [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]

    def try_move(self, d):

        action_packet = self.owner().mobility_component.try_move(d)

        if action_packet is None:
            return None

        action_key, action_args = action_packet
        action_args.insert(0, self.owner)

        return action_key, action_args
