from action import Action


class AwaitInputAction(Action):

    def __init__(self):

        Action.__init__(self, 'await_input')
        self.input_received = False

    def run(self):
        print 'awaiting_input'
        if self.input_received:
            return 'complete'
        return None

    def receive_input(self):
        self.input_received = True
