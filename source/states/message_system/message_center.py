

class MessageCenter(object):

    instance = None

    @classmethod
    def get_instance(cls):
        if cls.instance is None:
            cls.instance = cls()
        return cls.instance

    def __init__(self):
        self.new_messages = []
        self.subscribers = []
        self.subscriber_m_ids = {}

    def add_subscription(self, subscriber, m_ids):
        self.subscribers.append(subscriber)
        self.subscriber_m_ids[subscriber] = m_ids

    def remove_subscription(self, subscriber):
        self.subscribers.remove(subscriber)
        del self.subscriber_m_ids[subscriber]

    def receive_message(self, message):
        self.new_messages.append(message)

    def run(self):
        if self.new_messages:
            self.direct_messages()

    def direct_messages(self):

        while self.new_messages:
            next = self.new_messages.pop()
            report_list = filter(lambda x: self.filter_subscribers(x, next), self.subscribers)
            map(lambda x: self.send_report(x, next), report_list)

    @staticmethod
    def filter_subscribers(sub, message):
        return message.m_id in sub.m_ids

    @staticmethod
    def send_report(sub, message):
        sub.receive_report(message)
