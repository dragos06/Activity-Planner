import configparser

from src.domain.validators import PersonValidator, ActivityValidator
from src.repository.activity_repository import ActivityMemoryRepository, ActivityTextFileRepository, \
    ActivityBinaryFileRepository
from src.repository.person_repository import PersonMemoryRepository, PersonTextFileRepository, \
    PersonBinaryFileRepository
from src.services.activity_service import ActivityService
from src.services.person_service import PersonService
from src.services.undo_service import UndoService
from src.ui.ui import UI

config = configparser.ConfigParser()
config.read('settings.properties')

person_repository_type = config.get('RepositorySettings', 'person_repository_type')
activity_repository_type = config.get('RepositorySettings', 'activity_repository_type')

person_file_location = config.get('FileLocations', 'person_file_location')
activity_file_location = config.get('FileLocations', 'activity_file_location')

if person_repository_type == 'memory':
    person_repository = PersonMemoryRepository()
elif person_repository_type == 'text_file':
    person_repository = PersonTextFileRepository(person_file_location)
elif person_repository_type == 'binary_file':
    person_repository = PersonBinaryFileRepository(person_file_location)
else:
    raise ValueError("Invalid person repository type specified in settings")

if activity_repository_type == 'memory':
    activity_repository = ActivityMemoryRepository()
elif activity_repository_type == 'text_file':
    activity_repository = ActivityTextFileRepository(activity_file_location)
elif activity_repository_type == 'binary_file':
    activity_repository = ActivityBinaryFileRepository(activity_file_location)
else:
    raise ValueError("Invalid activity repository type specified in settings")

person_validator = PersonValidator()
activity_validator = ActivityValidator()

undo_service = UndoService()

activity_service = ActivityService(activity_repository, person_repository, activity_validator, undo_service)
person_service = PersonService(person_repository, activity_repository, person_validator, undo_service, activity_service)

ui = UI(person_service, activity_service, undo_service)
ui.start()
