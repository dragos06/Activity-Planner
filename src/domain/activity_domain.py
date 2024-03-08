from copy import deepcopy


class ActivityDomain:
    def __init__(self, activity_id, person_id, date, time, description):
        self.__activity_id = activity_id
        self.__person_id = person_id
        self.__date = date
        self.__time = time
        self.__description = description

    def __eq__(self, other):
        if not isinstance(other, ActivityDomain):
            return False
        return (self.activity_id == other.activity_id and self.person_id == other.person_id and self.date == other.date
                and self.time == other.time and self.description == other.description)

    @property
    def activity_id(self):
        return self.__activity_id

    @property
    def person_id(self):
        return self.__person_id

    @property
    def date(self):
        return self.__date

    @property
    def time(self):
        return self.__time

    @property
    def description(self):
        return self.__description

    @activity_id.setter
    def activity_id(self, value):
        self.__activity_id = value

    @person_id.setter
    def person_id(self, value):
        self.__person_id = deepcopy(value)

    @date.setter
    def date(self, value):
        self.__date = value

    @time.setter
    def time(self, value):
        self.__time = value

    @description.setter
    def description(self, value):
        self.__description = value
