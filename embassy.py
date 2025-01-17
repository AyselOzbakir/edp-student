from event import ApplicationSentEvent, ApplicationProcessedEvent

class Embassy:
    def __init__(self, name):
        self.name = name

    def process_application(self, queue):
        event = queue.receive_event()
        if event and isinstance(event, ApplicationSentEvent):
            student_name = event.payload["student"]
            decision = "Accepted" if len(student_name) % 2 == 0 else "Rejected"
            response_event = ApplicationProcessedEvent({
                "student": student_name,
                "embassy": self.name,
                "status": decision
            })
            queue.send_event(response_event)
            print(f"{self.name} processed application for {student_name}. Decision: {decision}")
