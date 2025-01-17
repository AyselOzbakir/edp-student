from communication_queue import CommunicationQueue
from student import Student
from embassy import Embassy
from sponsor import Sponsor
from language_trainer import LanguageTrainer

if __name__ == "__main__":
    queue = CommunicationQueue()

    student = Student("Alice")
    embassy = Embassy("Global Embassy")
    sponsor = Sponsor("EduFund")
    trainer = LanguageTrainer("LinguaPro")

    student.apply_to_embassy(embassy, queue)
    embassy.process_application(queue)
    response_event = queue.receive_event()
    if response_event:
        student.receive_response(response_event)

    sponsor.grant_sponsorship(student, queue)
    training_event = queue.receive_event()
    if training_event:
        student.receive_response(training_event)

    trainer.schedule_training(student, queue)
    training_event = queue.receive_event()
    if training_event:
        student.receive_response(training_event)
