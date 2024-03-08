import time

from src.domain.domain_exceptions import PersonValidationException, ActivityValidationException
import datetime


class PersonValidator:
    def __init__(self):
        pass

    def validate(self, person):
        _errors = []
        if not person.person_id.isnumeric():
            _errors.append("Incorrect ID. It should be a number")
        if len(person.phone_number) != 10:
            _errors.append("Incorrect phone number. It should have exactly 10 digits")
        if len(person.name) < 3:
            _errors.append("Name should have at least 3 characters")
        if len(_errors) > 0:
            raise PersonValidationException(_errors)


class ActivityValidator:
    def __init__(self):
        pass

    def validate(self, activity):
        _errors = []
        if not activity.activity_id.isnumeric():
            _errors.append("Incorrect ID. It should be a number")
        try:
            datetime.datetime.strptime(activity.date, "%d/%m")  # /%Y
        except ValueError:
            _errors.append("Incorrect date format, should be DD/MM")  # /YYYY
        try:
            time.strptime(activity.time, "%H:%M")
        except ValueError:
            _errors.append("Incorrect time format, should be HH:MM")
        if len(activity.description) < 3:
            _errors.append("Description should have at least 3 characters")
        if len(_errors) > 0:
            raise ActivityValidationException(_errors)
