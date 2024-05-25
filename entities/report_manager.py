from .base_event_manager import BaseEventManager
import mysql.connector

class ReportManager(BaseEventManager):
    def get_total_events(self):
        try:
            self.cursor.execute("SELECT COUNT(*) as total FROM event")
            result = self.cursor.fetchone()
            print(f"Total number of events: {result['total']}")
        except mysql.connector.Error as err:
            print("Error:", err)

    def get_events_count_by_year(self, year):
        try:
            self.cursor.execute("SELECT COUNT(*) as total FROM event WHERE YEAR(event_date) = %s", (year,))
            result = self.cursor.fetchone()
            print(f"Total number of events in {year}: {result['total']}")
        except mysql.connector.Error as err:
            print("Error:", err)

    def get_events_count_by_month(self, month):
        try:
            self.cursor.execute("SELECT COUNT(*) as total FROM event WHERE MONTH(event_date) = %s", (month,))
            result = self.cursor.fetchone()
            print(f"Total number of events in month {month}: {result['total']}")
        except mysql.connector.Error as err:
            print("Error:", err)
