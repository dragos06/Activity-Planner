from src.repository.repo_exceptions import RepositoryException
from src.services.undo_service import UndoRedoException


class UI:
    def __init__(self, person_service, activity_service, undo_service):
        self.__person_service = person_service
        self.__activity_service = activity_service
        self.__undo_service = undo_service

    @staticmethod
    def print_menu_top():
        print("1. Manage persons and activities")
        print("2. Add/remove activities")
        print("3. Search for persons or activities")
        print("4. Create statistics")
        print("5. Undo")
        print("6. Redo")
        print("7. Exit")

    @staticmethod
    def print_menu_option_1():
        print("1. Add person")
        print("2. Add activity")
        print("3. Remove person")
        print("4. Remove activity")
        print("5. Update person")
        print("6. Update activity")
        print("7. List all persons")
        print("8. List all activities")
        print("9. Go back")

    @staticmethod
    def print_menu_option_2():
        print("1. Add a person to an activity")
        print("2. Remove a person from an activity")
        print("3. Go back")

    @staticmethod
    def print_menu_option_3():
        print("1. Search person by name")
        print("2. Search person by phone number")
        print("3. Search activity by date")
        print("4. Search activity by time")
        print("5. Search activity by description")
        print("6. Go back")

    @staticmethod
    def print_menu_option_4():
        print("1. Activities for a given date. List the activities for a given date, in the order of their start time")
        print("2. Busiest days. Upcoming dates with activities, sorted in ascending order of the free time in that day")
        print(
            "3. Activities with a given person. List all upcoming activities to which a given person will participate")
        print("4. Go back")

    def add_person_ui(self):
        person_id = input("Please enter the person's id: ")
        name = input("Please enter the person's name: ")
        phone_number = input("Please enter the person's phone number: ")
        try:
            self.__person_service.add_person(person_id, name, phone_number)
        except RepositoryException as re:
            print("Error occurred: " + str(re))
        except Exception as e:
            print("Error occurred: " + str(e))

    def add_activity_ui(self):
        activity_id = input("Please enter the activity's id: ")
        date = input("Please enter the activity's date: ")
        time = input("Please enter the activity's time: ")
        description = input("Please enter the activity's description: ")
        try:
            self.__activity_service.add_activity(activity_id, [], date, time, description)
        except RepositoryException as re:
            print("Error occurred: " + str(re))
        except Exception as e:
            print("Error occurred: " + str(e))

    def remove_person_ui(self):
        person_id = input("Please enter the person's id which you want to delete: ")
        try:
            self.__person_service.delete_person(person_id)
        except RepositoryException as re:
            print("Error occurred: " + str(re))
        except Exception as e:
            print("Error occurred: " + str(e))

    def remove_activity_ui(self):
        activity_id = input("Please enter the activity's id which you want to delete: ")
        try:
            self.__activity_service.delete_activity(activity_id)
        except RepositoryException as re:
            print("Error occurred: " + str(re))
        except Exception as e:
            print("Error occurred: " + str(e))

    def update_person_ui(self):
        person_id = input("Please enter the person's id which you want to update: ")
        name = input("Please enter the person's new name: ")
        phone_number = input("Please enter the person's new phone number: ")
        try:
            self.__person_service.update_person(person_id, name, phone_number)
        except RepositoryException as re:
            print("Error occurred: " + str(re))
        except Exception as e:
            print("Error occurred: " + str(e))

    def update_activity_ui(self):
        activity_id = input("Please enter the activity's id which you want to update: ")
        date = input("Please enter the activity's new date: ")
        time = input("Please enter the activity's new time: ")
        description = input("Please enter the activity's new description: ")
        try:
            self.__activity_service.update_activity(activity_id, [], date, time, description)
        except RepositoryException as re:
            print("Error occurred: " + str(re))
        except Exception as e:
            print("Error occurred: " + str(e))

    @staticmethod
    def list_persons(persons):
        for person in persons:
            print(f"ID: {person.person_id} | Name: {person.name} | Phone number: {person.phone_number}")

    @staticmethod
    def list_activities(activities):
        for activity in activities:
            print(
                f"ID: {activity.activity_id} | Date: {activity.date} | Time: {activity.time} | "
                f"Description: {activity.description} | {activity.person_id}")

    def tie_person_to_activity_ui(self):
        activity_id = input("Please enter the activity's id which you want to bond to: ")
        person_id = input("Please enter the person's id which you want to be bonded with: ")
        try:
            self.__activity_service.tie_person_to_activity(activity_id, person_id)
        except RepositoryException as re:
            print("Error occurred: " + str(re))
        except Exception as e:
            print("Error occurred: " + str(e))

    def remove_person_from_activity_ui(self):
        activity_id = input("Please enter the activity's id which you want to remove from: ")
        person_id = input("Please enter the person's id which you want to be remove from: ")
        try:
            self.__activity_service.remove_person_from_activity(activity_id, person_id)
        except RepositoryException as re:
            print("Error occurred: " + str(re))
        except Exception as e:
            print("Error occurred: " + str(e))

    def search_person_using_name_ui(self):
        name = input("Please enter the person's name which you want to search: ")
        try:
            to_print_list = self.__person_service.search_person_using_name(name)
            self.list_persons(to_print_list)
        except RepositoryException as re:
            print("Error occurred: " + str(re))
        except Exception as e:
            print("Error occurred: " + str(e))

    def search_person_using_phone_number_ui(self):
        phone_number = input("Please enter the person's phone number which you want to search: ")
        try:
            to_print_list = self.__person_service.search_person_using_phone_number(phone_number)
            self.list_persons(to_print_list)
        except RepositoryException as re:
            print("Error occurred: " + str(re))
        except Exception as e:
            print("Error occurred: " + str(e))

    def search_activity_using_date_ui(self):
        date = input("Please enter the activity's date which you want to search: ")
        try:
            to_print_list = self.__activity_service.search_activity_using_date(date)
            self.list_activities(to_print_list)
        except RepositoryException as re:
            print("Error occurred: " + str(re))
        except Exception as e:
            print("Error occurred: " + str(e))

    def search_activity_using_time_ui(self):
        time = input("Please enter the activity's time which you want to search: ")
        try:
            to_print_list = self.__activity_service.search_activity_using_time(time)
            self.list_activities(to_print_list)
        except RepositoryException as re:
            print("Error occurred: " + str(re))
        except Exception as e:
            print("Error occurred: " + str(e))

    def search_activity_using_description_ui(self):
        description = input("Please enter the activity's description which you want to search: ")
        try:
            to_print_list = self.__activity_service.search_activity_using_description(description)
            self.list_activities(to_print_list)
        except RepositoryException as re:
            print("Error occurred: " + str(re))
        except Exception as e:
            print("Error occurred: " + str(e))

    def statistic_given_date_ui(self):
        given_date = input("Please enter the date for which the statistic will be computed: ")
        try:
            to_print_list = self.__activity_service.statistic_given_date(given_date)
            self.list_activities(to_print_list)
        except RepositoryException as re:
            print("Error occurred: " + str(re))
        except Exception as e:
            print("Error occurred: " + str(e))

    def busiest_day_ui(self):
        try:
            to_print_list = self.__activity_service.busiest_day()
            self.list_activities(to_print_list)
        except RepositoryException as re:
            print("Error occurred: " + str(re))
        except Exception as e:
            print("Error occurred: " + str(e))

    def statistic_given_person_ui(self):
        given_person = input("Please enter the person's id based on which the statistic will be generated: ")
        try:
            to_print_list = self.__activity_service.statistic_given_person(given_person)
            self.list_activities(to_print_list)
        except RepositoryException as re:
            print("Error occurred: " + str(re))
        except Exception as e:
            print("Error occurred: " + str(e))

    def undo(self):
        try:
            self.__undo_service.undo()
        except UndoRedoException as ure:
            print("Error occurred: " + str(ure))
        except Exception as e:
            print("Error occurred: " + str(e))

    def redo(self):
        try:
            self.__undo_service.redo()
        except UndoRedoException as ure:
            print("Error occurred: " + str(ure))
        except Exception as e:
            print("Error occurred: " + str(e))

    def start(self):
        if self.__person_service.length_person_list() == 0:
            self.__person_service.generate_20_persons()
        if self.__activity_service.length_activity_list() == 0:
            self.__activity_service.generate_20_activities()
        while True:
            self.print_menu_top()
            user_option = input("Please choose an option: ")
            if user_option == '1':
                while True:
                    self.print_menu_option_1()
                    user_option_1 = input("Please choose an option: ")
                    if user_option_1 == '1':
                        self.add_person_ui()
                    elif user_option_1 == '2':
                        self.add_activity_ui()
                    elif user_option_1 == '3':
                        self.remove_person_ui()
                    elif user_option_1 == '4':
                        self.remove_activity_ui()
                    elif user_option_1 == '5':
                        self.update_person_ui()
                    elif user_option_1 == '6':
                        self.update_activity_ui()
                    elif user_option_1 == '7':
                        self.list_persons(self.__person_service.get_all_persons())
                    elif user_option_1 == '8':
                        self.list_activities(self.__activity_service.get_all_activities())
                    elif user_option_1 == '9':
                        break
                    else:
                        print("Invalid option!")
            elif user_option == '2':
                while True:
                    self.print_menu_option_2()
                    user_option_2 = input("Please choose an option: ")
                    if user_option_2 == '1':
                        self.tie_person_to_activity_ui()
                    elif user_option_2 == '2':
                        self.remove_person_from_activity_ui()
                    elif user_option_2 == '3':
                        break
                    else:
                        print("Invalid option!")
            elif user_option == '3':
                while True:
                    self.print_menu_option_3()
                    user_option_3 = input("Please choose an option: ")
                    if user_option_3 == '1':
                        self.search_person_using_name_ui()
                    elif user_option_3 == '2':
                        self.search_person_using_phone_number_ui()
                    elif user_option_3 == '3':
                        self.search_activity_using_date_ui()
                    elif user_option_3 == '4':
                        self.search_activity_using_time_ui()
                    elif user_option_3 == '5':
                        self.search_activity_using_description_ui()
                    elif user_option_3 == '6':
                        break
                    else:
                        print("Invalid option!")
            elif user_option == '4':
                while True:
                    self.print_menu_option_4()
                    user_option_4 = input("Please choose an option: ")
                    if user_option_4 == '1':
                        self.statistic_given_date_ui()
                    elif user_option_4 == '2':
                        self.busiest_day_ui()
                    elif user_option_4 == '3':
                        self.statistic_given_person_ui()
                    elif user_option_4 == '4':
                        break
                    else:
                        print("Invalid option!")
            elif user_option == '5':
                self.undo()
            elif user_option == '6':
                self.redo()
            elif user_option == '7':
                print("Exiting...")
                break
            else:
                print("Invalid option!")
