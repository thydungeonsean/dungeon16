from source.objects.map_objects.ai.ai_component import AIComponent
from actions.action_assigner import ActionAssigner


class PlayerAI(AIComponent):

    def __init__(self, owner):
        AIComponent.__init__(self, owner)

    def dist_to_player(self):
        return 0

    def set_next_action(self):
        pass

    def try_move(self, d):

        action_packet = self.owner().mobility_component.try_move(d)

        if action_packet is None:
            return

        action_key, action_args = action_packet
        action_args.insert(0, self.owner)
        self.action = ActionAssigner.get_action(action_key, *action_args)
