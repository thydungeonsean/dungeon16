from control_component import ControlComponent
from controller import Controller
from weakref import ref


class MoveControl(ControlComponent):

    def __init__(self, owner):

        ControlComponent.__init__(self, 'move_control')
        self.owner = ref(owner)
        self.ready = True

    def set_key_map(self):
        return {
            Controller.key_bind['up']: self.up,
            Controller.key_bind['down']: self.down,
            Controller.key_bind['right']: self.right,
            Controller.key_bind['left']: self.left,
            Controller.key_bind['wait']: self.wait
        }

    def up(self):
        if self.ready:
            self.ready = not self.owner().ai.assign_move('up')

    def down(self):
        if self.ready:
            self.ready = not self.owner().ai.assign_move('down')

    def right(self):
        if self.ready:
            self.ready = not self.owner().ai.assign_move('right')

    def left(self):
        if self.ready:
            self.ready = not self.owner().ai.assign_move('left')

    def wait(self):
        if self.ready:
            self.owner().ai.skip_turn()
            self.ready = False

    def start_turn(self):
        self.ready = True

