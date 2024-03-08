from src.domain.person_domain import PersonDomain
from src.domain.validators import PersonValidator
from src.repository.person_repository import PersonTextFileRepository, PersonBinaryFileRepository
from src.services.undo_service import UndoService, Command, Operation, CascadedOperation
import random


class PersonService:
    def __init__(self, person_repository, activity_repository, person_validator: PersonValidator, undo_service,
                 activity_service):
        self.__person_repository = person_repository
        self.__activity_repository = activity_repository
        self.__person_validator = person_validator
        self.__undo_service = undo_service
        self.__activity_service = activity_service

    def add_person(self, person_id: str, name: str, phone_number: str) -> None:
        """
        Add person to repository
        :param person_id: Person's id
        :param name: Person's name
        :param phone_number: Person's phone number
        :raises: DuplicateIDException if person with same ID exists
        """
        person = PersonDomain(person_id, name, phone_number)
        self.__person_validator.validate(person)
        self.__person_repository.store(person)
        undo_action = Command(self.delete_person, person_id)
        redo_action = Command(self.add_person, person_id, name, phone_number)
        operation = Operation(undo_action, redo_action)
        self.__undo_service.record_for_undo(operation)
        self.save_persons_to_file()

    def delete_person(self, person_id: str) -> PersonDomain:
        """
        Remove person from repository
        :param person_id: person to remove
        :return: removed person
        :raises: PersonDoesNotExistException if person with given id does not exist
        """
        self.__activity_repository.search_all_activities_for_person_id(person_id)
        self.save_persons_to_file()
        deleted_person = self.__person_repository.delete(person_id)
        undo_action = Command(
            self.add_person, deleted_person.person_id, deleted_person.name, deleted_person.phone_number)
        redo_action = Command(self.delete_person, person_id)
        person_operation = Operation(undo_action, redo_action)
        cascaded_ops = [person_operation]
        person_activities = []
        for activity in self.__activity_repository.get_all():
            if deleted_person.person_id in activity.person_id:
                person_activities.append(activity)
        for activity in person_activities:
            activity_operation = self.__activity_service.delete_activity(activity.activity_id)
            cascaded_ops.append(activity_operation)
        self.__undo_service.record_for_undo(CascadedOperation(cascaded_ops))
        self.save_persons_to_file()
        return deleted_person

    def update_person(self, person_id: str, name: str, phone_number: str):
        """
        Update person to repository
        :param person_id: person to update
        :param name: new name
        :param phone_number: new phone number
        :raises: PersonDoesNotExistException if person with given id does not exist
        """
        old_name = self.__person_repository.get(person_id).name
        old_phone_number = self.__person_repository.get(person_id).phone_number
        person = PersonDomain(person_id, name, phone_number)
        self.__person_validator.validate(person)
        self.__person_repository.update(person_id, name, phone_number)
        undo_action = Command(self.update_person, person_id, old_name, old_phone_number)
        redo_action = Command(self.update_person, person_id, name, phone_number)
        operation = Operation(undo_action, redo_action)
        self.__undo_service.record_for_undo(operation)
        self.save_persons_to_file()

    def get_all_persons(self):
        """
        Gets all persons from repository
        :return: all persons from repository
        """
        return self.__person_repository.get_all()

    def search_person_using_name(self, name):
        return self.__person_repository.search_using_name(name)

    def search_person_using_phone_number(self, phone_number):
        return self.__person_repository.search_using_phone_number(phone_number)

    def length_person_list(self):
        return self.__person_repository.size

    def generate_20_persons(self):
        name_list = ["Andrei", "Elena", "Vlad", "Ioana", "Mihai", "Ana", "Alexandru", "Maria", "Stefan", "Andreea",
                     "Cristian", "Roxana", "Radu", "Laura", "Bogdan", "Diana", "Florin", "Gabriela", "Sorin", "Adriana"]
        for person_id in range(1, 21):
            name = name_list[random.randint(0, 19)]
            phone_number = '07'
            for phone_digit in range(0, 8):
                phone_number += str(random.randint(0, 9))
            self.add_person(str(person_id), name, phone_number)
        self.__undo_service._undo_stack = []
        self.__undo_service._redo_stack = []
        self.__undo_service._is_undoredo_op = False
        self.__undo_service._can_redo = False

    def save_persons_to_file(self):
        if isinstance(self.__person_repository, PersonTextFileRepository) or isinstance(self.__person_repository,
                                                                                        PersonBinaryFileRepository):
            self.__person_repository.save_persons_to_file()
