from action import Action
from source.states.settings import Settings


class MoveAction(Action):

    def __init__(self, *args):
        Action.__init__(self, 'move')
        self.complete = True
        self.owner = args[0]
        self.move = args[1]
        self.complete_code = self.check_for_instant_move()

    def run(self):

        if self.complete:
            self.complete_move()
            return self.complete_code
        else:
            pass
            # run animation

    def complete_move(self):
        self.owner().mobility_component.move(self.move)

    def check_for_instant_move(self):

        """
        If move animations are on and either the moving actor, or its destination is visible on the map,
        we will run the actors animation.
        Otherwise, we return fast_complete to tell the turn_phase to batch more ai calls into the same frame

        """

        level = self.owner().level
        owner_coord = self.owner().coord.get

        owner_is_in_fov = level.fov_map.point_is_visible(owner_coord)
        move_is_in_fov = level.fov_map.point_is_visible(self.move)

        if owner_is_in_fov or move_is_in_fov:

            return 'complete'

        elif not Settings.MOVE_ANIMATION:

            return 'fast_complete'

        else:

            self.complete = True
            return 'fast_complete'
