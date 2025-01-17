from event import ApplicationProcessedEvent, SponsorshipGrantedEvent, LanguageTrainingScheduledEvent, ApplicationSentEvent

class Student:
    def __init__(self, name):
        self.name = name
        self.application_status = None

    def apply_to_embassy(self, embassy, queue):
        payload = {"student": self.name, "embassy": embassy.name}
        event = ApplicationSentEvent(payload)
        queue.send_event(event)
        print(f"{self.name} applied to {embassy.name}.")

    def receive_response(self, event):
        if isinstance(event, ApplicationProcessedEvent):
            self.application_status = event.payload["status"]
            print(f"{self.name} received an update from {event.payload['embassy']}: {self.application_status}.")
        elif isinstance(event, SponsorshipGrantedEvent):
            print(f"{self.name} was granted sponsorship by {event.payload['sponsor']}.")
        elif isinstance(event, LanguageTrainingScheduledEvent):
            print(f"{self.name} was scheduled for a language training session.")
