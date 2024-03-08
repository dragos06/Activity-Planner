from src.domain.person_domain import PersonDomain
from src.repository.repo_exceptions import DuplicateIDException, PersonDoesNotExistException
import pickle
import os


class PersonMemoryRepository:
    def __init__(self):
        self._persons = {}

    def store(self, person: PersonDomain) -> None:
        """
        Store person to repository
        :param person: person to add
        :raises: DuplicateIDException if person with same ID exists
        """
        if person.person_id in self._persons:
            raise DuplicateIDException()
        self._persons[person.person_id] = person

    def get(self, person_id: str) -> PersonDomain:
        """
        Gets person from repository
        :param person_id: person to get
        :return: Person with given person_id
        :raises: PersonDoesNotExistException if person with given id does not exist
        """
        if person_id in self._persons:
            return self._persons[person_id]
        raise PersonDoesNotExistException()

    def delete(self, person_id: str) -> PersonDomain:
        """
        Remove person from repository
        :param person_id: person to remove
        :return: removed person
        :raises: PersonDoesNotExistException if person with given id does not exist
        """
        if person_id not in self._persons:
            raise PersonDoesNotExistException()
        deleted_person = self._persons[person_id]
        del self._persons[person_id]
        return deleted_person

    def update(self, person_id: str, name: str, phone_number: str) -> None:
        """
        Update person to repository
        :param person_id: person to update
        :param name: new name
        :param phone_number: new phone number
        :raises: PersonDoesNotExistException if person with given id does not exist
        """
        if person_id not in self._persons:
            raise PersonDoesNotExistException
        person = self.get(person_id)
        person.name = name
        person.phone_number = phone_number
        self._persons[person_id] = person

    def get_all(self) -> list:
        """
        Gets all persons from repository
        :return: all persons from repository
        """
        return list(self._persons.values())

    def search_using_name(self, name):
        searched_persons = []
        for person in self.get_all():
            if name.lower().strip() in person.name.lower().strip():
                searched_persons.append(person)
        if searched_persons:
            return searched_persons
        else:
            raise PersonDoesNotExistException

    def search_using_phone_number(self, phone_number):
        searched_persons = []
        for person in self.get_all():
            if phone_number.lower().strip() in person.phone_number.lower().strip():
                searched_persons.append(person)
        if searched_persons:
            return searched_persons
        else:
            raise PersonDoesNotExistException

    @property
    def size(self):
        return len(self.get_all())


class PersonBinaryFileRepository(PersonMemoryRepository):
    def __init__(self, file_name):
        super().__init__()
        self.__file_name = file_name
        self.load_persons_from_file()

    def load_persons_from_file(self):
        try:
            if os.path.exists(self.__file_name):
                file = open(self.__file_name, 'rb')
                self._persons = pickle.load(file)
                file.close()
        except EOFError:
            raise FileNotFoundError("File not found")

    def save_persons_to_file(self):
        file = open(self.__file_name, 'wb')
        pickle.dump(self._persons, file)


class PersonTextFileRepository(PersonMemoryRepository):
    def __init__(self, file_name):
        super().__init__()
        self.__file_name = file_name
        self.load_persons_from_file()

    def load_persons_from_file(self):
        try:
            if os.path.exists(self.__file_name):
                file = open(self.__file_name, 'r')
                lines = file.readlines()
                for line in lines:
                    person_id, name, phone_number = line.strip().split(' | ')
                    self.store(PersonDomain(person_id, name, phone_number))
        except EOFError:
            raise FileNotFoundError("File not found")

    def save_persons_to_file(self):
        file = open(self.__file_name, 'w')
        for person in self.get_all():
            file.write(f"{person.person_id} | {person.name} | {person.phone_number}\n")
