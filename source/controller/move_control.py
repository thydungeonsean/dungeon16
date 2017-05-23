from control_component import ControlComponent
from controller import Controller
from weakref import ref


class MoveControl(ControlComponent):

    def __init__(self, owner):

        ControlComponent.__init__(self, 'move_control')
        self.owner = ref(owner)

    def set_key_map(self):
        return {
            Controller.key_bind['up']: self.up,
            Controller.key_bind['down']: self.down,
            Controller.key_bind['right']: self.right,
            Controller.key_bind['left']: self.left,
            Controller.key_bind['wait']: self.wait
        }

    def up(self):
        self.owner().ai.try_move('up')

    def down(self):
        self.owner().ai.try_move('down')

    def right(self):
        self.owner().ai.try_move('right')

    def left(self):
        self.owner().ai.try_move('left')

    def wait(self):
        print self.owner().party_rank
        pass
