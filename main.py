from entities.event_manager import EventManager
from entities.report_manager import ReportManager
from menu import Menu
from helpers.helpers import Helpers  # Updated import

if __name__ == "__main__":
    event_manager = EventManager()
    report_manager = ReportManager()
    menu = Menu()
    helpers = Helpers()

    while True:
        menu.display_menu()
        choice = menu.get_choice()

        if choice == '1':
            event_name = input("Enter event name: ")
            event_category = input("Enter event category: ")
            event_date = input("Enter event date (YYYY-MM-DD): ")
            while not helpers.validate_date(event_date):
                print("Invalid date format. Please use YYYY-MM-DD")
                event_date = input("Enter event date (YYYY-MM-DD): ")
            event_time = input("Enter event time (HH:MM:SS): ")
            event_place = input("Enter event place: ")
            place_address = input("Enter place address: ")
            event_manager.create_event(event_name, event_category, event_date, event_time, event_place, place_address)
        elif choice == '2':
            event_id = input("Enter event ID to update: ")
            event_name = input("Enter new event name: ")
            event_category = input("Enter new event category: ")
            event_date = input("Enter new event date (YYYY-MM-DD): ")
            while not helpers.validate_date(event_date):
                print("Invalid date format. Please use YYYY-MM-DD")
                event_date = input("Enter new event date (YYYY-MM-DD): ")
            event_time = input("Enter new event time (HH:MM:SS): ")
            event_place = input("Enter new event place: ")
            place_address = input("Enter new place address: ")
            event_manager.update_event(event_id, event_name, event_category, event_date, event_time, event_place, place_address)
        elif choice == '3':
            event_id = input("Enter event ID to delete: ")
            event_manager.delete_event(event_id)
        elif choice == '4':
            event_manager.list_events()
        elif choice == '5':
            event_manager.delete_all_events()
        elif choice == '6':
            menu.display_filter_menu()
            filter_choice = menu.get_filter_choice()
            if filter_choice == '1':
                category = input("Enter event category to filter: ")
                event_manager.filter_events_by_category(category)
            elif filter_choice == '2':
                menu.display_date_filter_menu()
                date_filter_choice = menu.get_date_filter_choice()
                if date_filter_choice == '1':
                    year = input("Enter year to filter: ")
                    event_manager.filter_events(year=year)
                elif date_filter_choice == '2':
                    month = input("Enter month (1-12) to filter: ")
                    event_manager.filter_events(month=month)
                else:
                    print("Invalid date filter choice. Please try again.")
            else:
                print("Invalid filter choice. Please try again.")
        elif choice == '7':
            menu.display_report_menu()
            report_choice = menu.get_report_choice()
            if report_choice == '1':
                report_manager.get_total_events()
            elif report_choice == '2':
                year = input("Enter year for report: ")
                report_manager.get_events_count_by_year(year)
            elif report_choice == '3':
                month = input("Enter month (1-12) for report: ")
                report_manager.get_events_count_by_month(month)
            else:
                print("Invalid report choice. Please try again.")
        elif choice == '8':
            event_manager.close_connection()
            report_manager.close_connection()
            break
        else:
            print("Invalid choice. Please try again.")
