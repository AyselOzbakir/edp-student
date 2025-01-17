from event import SponsorshipGrantedEvent

class Sponsor:
    def __init__(self, name):
        self.name = name

    def grant_sponsorship(self, student, queue):
        event = SponsorshipGrantedEvent({"student": student.name, "sponsor": self.name})
        queue.send_event(event)
        print(f"{self.name} granted sponsorship to {student.name}.")
