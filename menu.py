class Menu:
    @staticmethod
    def display_menu():
        print("\nEvent Management System")
        print("1. Create Event")
        print("2. Update Event")
        print("3. Delete Event")
        print("4. List Events")
        print("5. Delete All Events")
        print("6. Filter")
        print("7. Reports")
        print("8. Exit")

    @staticmethod
    def display_filter_menu():
        print("\nFilter Events")
        print("1. By event category")
        print("2. By date")

    @staticmethod
    def display_date_filter_menu():
        print("\nFilter Events by Date")
        print("1. By year")
        print("2. By month")

    @staticmethod
    def display_report_menu():
        print("\nReports")
        print("1. Total number of events")
        print("2. Events count by year")
        print("3. Events count by month")

    @staticmethod
    def get_choice():
        return input("Enter your choice: ")

    @staticmethod
    def get_filter_choice():
        return input("Enter your filter choice: ")

    @staticmethod
    def get_date_filter_choice():
        return input("Enter your date filter choice: ")

    @staticmethod
    def get_report_choice():
        return input("Enter your report choice: ")
