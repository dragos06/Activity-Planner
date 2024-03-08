class RepositoryException(Exception):
    def __init__(self, error_message):
        self._error_msg = error_message

    @property
    def message(self):
        return self._error_msg

    def __str__(self):
        return "Repo Exception: " + str(self.message)


class DuplicateIDException(RepositoryException):
    def __init__(self):
        RepositoryException.__init__(self, "There already is a person with that ID.")


class PersonDoesNotExistException(RepositoryException):
    def __init__(self):
        RepositoryException.__init__(self, "There is no person with those attributes.")


class ActivityAlreadyExistsException(RepositoryException):
    def __init__(self):
        RepositoryException.__init__(self, "There already is an activity with that ID.")


class ActivityDoesNotExistException(RepositoryException):
    def __init__(self):
        RepositoryException.__init__(self, "There is no activity with those attributes.")


class ActivityOverlapException(RepositoryException):
    def __init__(self):
        RepositoryException.__init__(self, "Activity overlaps with other activity")
