from message_center import MessageCenter


class Subscriber(object):

    def __init__(self, owner, m_ids, tags):
        self.owner = owner
        self.m_ids = m_ids
        self.tags = tags
        MessageCenter.get_instance().add_subscription(self, m_ids)

    def receive_report(self, message):
        if self.report_is_relevant(message):
            self.owner.receive_report()

    def report_is_relevant(self, message):

        return self.tags.intersection(message.tags)

