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
        x, y = self.owner.coord.get
        self.owner.coord.set((x, y-1))

    def down(self):
        x, y = self.owner.coord.get
        self.owner.coord.set((x, y+1))

    def right(self):
        x, y = self.owner.coord.get
        self.owner.coord.set((x+1, y))

    def left(self):
        x, y = self.owner.coord.get
        self.owner.coord.set((x-1, y))
