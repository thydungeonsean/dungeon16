from control_component import ControlComponent
from controller import Controller


class MoveControl(ControlComponent):

    def __init__(self, owner):

        ControlComponent.__init__(self)
        self.owner = owner

    def set_key_map(self):
        return {
            Controller.key_bind['up']: self.up,
            Controller.key_bind['down']: self.down,
            Controller.key_bind['right']: self.right,
            Controller.key_bind['left']: self.left
        }

    def up(self):
        self.owner.try_move('up')

    def down(self):
        self.owner.try_move('down')

    def right(self):
        self.owner.try_move('right')

    def left(self):
        self.owner.try_move('left')
