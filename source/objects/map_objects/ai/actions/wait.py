from source.objects.map_objects.ai.actions.action import Action


class WaitAction(Action):

    def __init__(self):
        Action.__init__(self, 'wait')

    def run(self):
        # do stuff
        # print 'waiting'
        code = 'fast_complete'
        return code
