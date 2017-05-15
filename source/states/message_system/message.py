from message_center import MessageCenter


class Message(object):

    m_id_types = ('actor_move', 'actor_die')

    def __init__(self, m_id, *tags):

        assert m_id in Message.m_id_types  # make sure we're sending valid messages

        self.m_id = m_id
        self.tags = set(tags)

    def send(self):
        center = MessageCenter.get_instance()
        center.receive_message(self)
