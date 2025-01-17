class Event:
    def __init__(self, payload):
        self.payload = payload

class ApplicationSentEvent(Event):
    def __init__(self, payload):
        super().__init__(payload)

class ApplicationProcessedEvent(Event):
    def __init__(self, payload):
        super().__init__(payload)

class SponsorshipGrantedEvent(Event):
    def __init__(self, payload):
        super().__init__(payload)

class LanguageTrainingScheduledEvent(Event):
    def __init__(self, payload):
        super().__init__(payload)
