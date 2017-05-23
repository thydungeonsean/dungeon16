

class TurnPhase(object):

    def __init__(self, level):
        self.level = level
        self.current_actor = None
        self.available_actors = None

    def run(self):

        if self.current_actor is None:
            self.initialize_phase()
            self.current_actor = self.get_next_actor()
            if self.current_actor is None:  # no actors in this phase group
                self.deinitialize_phase()
                return True  # phase is over

        end = self.run_action_batch()

        return end

    def initialize_phase(self):
        self.available_actors = self.get_available_actors()
        self.sort_available()

    def deinitialize_phase(self):
        pass

    def get_next_actor(self):
        if not self.available_actors:
            next_actor = None
        else:
            next_actor = self.available_actors.pop()
        return next_actor

    def get_available_actors(self):
        return list(filter(lambda actor: self.is_available(actor), self.level.actors.actors))

    def is_available(self, actor):
        raise NotImplementedError

    def sort_available(self):
        raise NotImplementedError

    def run_action_batch(self):

        if self.current_actor is None:
            return True

        action_code = 'fast_complete'

        while action_code == 'fast_complete':

            action_code = self.current_actor.ai.run_action()

            if action_code is None:
                return False

            if action_code in ('complete', 'fast_complete'):
                self.current_actor.ai.clear_action()
                self.current_actor = self.get_next_actor()
                if self.current_actor is None:
                    return True

            elif action_code == 'pass':
                self.available_actors.insert(0, self.current_actor)
                self.current_actor = self.get_next_actor()
                if self.current_actor is None:
                    return True

        return self.current_actor is None
