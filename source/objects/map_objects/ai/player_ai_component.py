from source.objects.map_objects.ai.ai_component import AIComponent
from actions.action_assigner import ActionAssigner


class PlayerAIComponent(AIComponent):

    def __init__(self, owner):
        AIComponent.__init__(self, owner)

    def dist_to_player(self):
        return 0

    def set_next_action(self):
        pass

    def assign_move(self, d):

        action_packet = self.try_move(d)
        if action_packet is not None:
            action_key, action_args = action_packet
            self.action = ActionAssigner.get_action(action_key, *action_args)

    def skip_turn(self):
        self.action = ActionAssigner.get_action('wait')
