import unittest
from src.domain.activity_domain import ActivityDomain
from src.domain.validators import ActivityValidator
from src.repository.activity_repository import ActivityMemoryRepository
from src.repository.person_repository import PersonMemoryRepository
from src.services.activity_service import ActivityService


class UnitTesting(unittest.TestCase):
    def setUp(self):
        self.activity_repository = ActivityMemoryRepository()
        self.person_repository = PersonMemoryRepository()
        self.activity_validator = ActivityValidator()
        self.activity_service = ActivityService(self.activity_repository, self.person_repository,
                                                self.activity_validator)

    def test_add_activity(self):
        self.activity_service.add_activity('1', [], '10/10', '12:04', 'football')
        self.assertEqual(self.activity_service.get_all_activities(),
                         [ActivityDomain('1', [], '10/10', '12:04', 'football')])

        self.activity_service.add_activity('2', [], '02/03', '15:33', 'volleyball')
        self.assertEqual(self.activity_service.get_all_activities(),
                         [ActivityDomain('1', [], '10/10', '12:04', 'football'),
                          ActivityDomain('2', [], '02/03', '15:33', 'volleyball')])

    def test_remove_activity(self):
        self.activity_service.add_activity('1', [], '10/10', '12:04', 'football')
        self.activity_service.add_activity('2', [], '02/03', '15:33', 'volleyball')

        self.activity_service.delete_activity('2')
        self.assertEqual(self.activity_service.get_all_activities(),
                         [ActivityDomain('1', [], '10/10', '12:04', 'football')])

        self.activity_service.delete_activity('1')
        self.assertEqual(self.activity_service.get_all_activities(), [])

    def test_update_activity(self):
        self.activity_service.add_activity('1', [], '10/10', '12:04', 'football')
        self.activity_service.add_activity('2', [], '02/03', '15:33', 'volleyball')

        self.activity_service.update_activity('2', [], '01/01', '01:01', 'hiking')
        self.assertEqual(self.activity_service.get_all_activities(),
                         [ActivityDomain('1', [], '10/10', '12:04', 'football'),
                          ActivityDomain('2', [], '01/01', '01:01', 'hiking')])

        self.activity_service.update_activity('1', [], '12/12', '23:23', 'swimming')
        self.assertEqual(self.activity_service.get_all_activities(),
                         [ActivityDomain('1', [], '12/12', '23:23', 'swimming'),
                          ActivityDomain('2', [], '01/01', '01:01', 'hiking')])
