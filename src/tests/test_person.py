import unittest
from src.domain.person_domain import PersonDomain
from src.domain.validators import PersonValidator
from src.repository.person_repository import PersonMemoryRepository
from src.repository.activity_repository import ActivityMemoryRepository
from src.services.person_service import PersonService


class UnitTesting(unittest.TestCase):
    def setUp(self):
        self.person_repository = PersonMemoryRepository()
        self.activity_repository = ActivityMemoryRepository()
        self.person_validator = PersonValidator()
        self.person_service = PersonService(self.person_repository, self.activity_repository, self.person_validator)

    def test_add_person(self):
        self.person_service.add_person('1', 'Alex', '0712345678')
        self.assertEqual(self.person_service.get_all_persons(), [PersonDomain('1', 'Alex', '0712345678')])

        self.person_service.add_person('2', 'Ana', '0786543211')
        self.assertEqual(self.person_service.get_all_persons(),
                         [PersonDomain('1', 'Alex', '0712345678'), PersonDomain('2', 'Ana', '0786543211')])

        self.person_service.add_person('3', 'Ion', '0711111111')
        self.assertEqual(self.person_service.get_all_persons(),
                         [PersonDomain('1', 'Alex', '0712345678'), PersonDomain('2', 'Ana', "0786543211"),
                          PersonDomain('3', 'Ion', '0711111111')])

    def test_remove_person(self):
        self.person_service.add_person('1', 'Alex', '0712345678')
        self.person_service.add_person('2', 'Ana', '0786543211')
        self.person_service.add_person('3', 'Ion', '0711111111')

        self.person_service.delete_person('2')
        self.assertEqual(self.person_service.get_all_persons(),
                         [PersonDomain('1', 'Alex', '0712345678'),
                          PersonDomain('3', 'Ion', '0711111111')])

        self.person_service.delete_person('1')
        self.assertEqual(self.person_service.get_all_persons(),
                         [PersonDomain('3', 'Ion', '0711111111')])

        self.person_service.delete_person('3')
        self.assertEqual(self.person_service.get_all_persons(), [])

    def test_update_person(self):
        self.person_service.add_person('1', 'Alex', '0712345678')
        self.person_service.add_person('2', 'Ana', '0786543211')
        self.person_service.add_person('3', 'Ion', '0711111111')

        self.person_service.update_person('2', 'Relu', '0799999999')
        self.assertEqual(self.person_service.get_all_persons(),
                         [PersonDomain('1', 'Alex', '0712345678'), PersonDomain('2', 'Relu', "0799999999"),
                          PersonDomain('3', 'Ion', '0711111111')])

        self.person_service.update_person('1', 'Dan', '0700000000')
        self.assertEqual(self.person_service.get_all_persons(),
                         [PersonDomain('1', 'Dan', '0700000000'), PersonDomain('2', 'Relu', "0799999999"),
                          PersonDomain('3', 'Ion', '0711111111')])

        self.person_service.update_person('3', 'Vlad', '0755555555')
        self.assertEqual(self.person_service.get_all_persons(),
                         [PersonDomain('1', 'Dan', '0700000000'), PersonDomain('2', 'Relu', "0799999999"),
                          PersonDomain('3', 'Vlad', '0755555555')])
