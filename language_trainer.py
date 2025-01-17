from event import LanguageTrainingScheduledEvent

class LanguageTrainer:
    def __init__(self, name):
        self.name = name

    def schedule_training(self, student, queue):
        event = LanguageTrainingScheduledEvent({"student": student.name, "trainer": self.name})
        queue.send_event(event)
        print(f"{self.name} scheduled language training for {student.name}.")
