from student import Student
from embassy import Embassy
from embassy_appointment_request_event import EmbassyAppointmentRequestEvent
from appointment_confirmation_event import AppointmentConfirmationEvent

event_queue = []

student1 = Student("Piotr1", "Brudny", '1.02.1984', 'Ankara', '5435345345', 'ED4234323', event_queue)
polish_embassy = Embassy('Polish Embassy', 'Ankara, Harika 10', '343242344', 'polishembassy@gov.tr', event_queue)


student1.ask_for_embassy_appointment('10.12.2024')


while event_queue: 
    event = event_queue.pop(0) 


    if isinstance(event, EmbassyAppointmentRequestEvent):
        polish_embassy.handle_appointment_request(event) 
    elif isinstance(event, AppointmentConfirmationEvent):
        student1.handle_appointment_confirmation(event)

    
