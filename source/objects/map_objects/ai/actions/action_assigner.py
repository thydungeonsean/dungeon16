from wait import WaitAction
from await_input import AwaitInputAction
from move import MoveAction
from bump import BumpAction


class ActionAssigner(object):

    action_keys = ('move', 'bump', 'wait', 'fire', 'await_input')

    @classmethod
    def get_action(cls, action_key, *args):

        assert action_key in cls.action_keys

        if action_key == 'await_input':
            return AwaitInputAction()
        elif action_key == 'wait':
            return WaitAction()
        elif action_key == 'move':
            return MoveAction(*args)
        elif action_key == 'bump':
            return BumpAction(*args)
