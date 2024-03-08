class PersonDomain:
    def __init__(self, person_id, name, phone_number):
        self.__person_id = person_id
        self.__name = name
        self.__phone_number = phone_number

    def __str__(self):
        return f"ID: {self.person_id} | Name: {self.name} | Phone number: {self.phone_number}"

    def __eq__(self, other):
        if not isinstance(other, PersonDomain):
            return False
        return self.person_id == other.person_id and self.name == other.name and self.phone_number == other.phone_number

    @property
    def person_id(self):
        return self.__person_id

    @property
    def name(self):
        return self.__name

    @property
    def phone_number(self):
        return self.__phone_number

    @person_id.setter
    def person_id(self, value):
        self.__person_id = value

    @name.setter
    def name(self, value):
        self.__name = value

    @phone_number.setter
    def phone_number(self, value):
        self.__phone_number = value
