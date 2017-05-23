from weakref import ref
from actions.action_assigner import ActionAssigner


class AIComponent(object):

    def __init__(self, owner):

        self.owner = ref(owner)
        self.level = None

        self.action = None

        self.state = 'inactive'

    def set_level(self, level):
        self.level = level

    def dist_to_player(self):
        return 1

    def clear_action(self):
        self.action = None

    def set_next_action(self):

        current_coord = self.owner().coord.get

        next_action = ActionAssigner.get_action('wait')
        self.action = next_action

    def run_action(self):
        if self.action is None:
            self.set_next_action()
            if self.action is None:
                return None
        return self.action.run()
