from queue import Queue

class CommunicationQueue:
    def __init__(self):
        self.queue = Queue()

    def send_event(self, event):
        self.queue.put(event)

    def receive_event(self):
        if not self.queue.empty():
            return self.queue.get()
        return None
