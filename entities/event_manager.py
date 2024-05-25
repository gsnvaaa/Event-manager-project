from .base_event_manager import BaseEventManager
from tabulate import tabulate
import mysql.connector

class EventManager(BaseEventManager):
    def create_event(self, event_name, event_category, event_date, event_time, event_place, place_address):
        if not self.helpers.validate_date(event_date):
            print("Invalid date format. Please use YYYY-MM-DD")
            return

        try:
            self.cursor.execute("INSERT INTO event (event_name, event_category, event_date, event_time, event_place, place_address) VALUES (%s, %s, %s, %s, %s, %s)",
                                (event_name, event_category, event_date, event_time, event_place, place_address))
            self.conn.commit()
            print("Event created successfully")
        except mysql.connector.Error as err:
            print("Error:", err)
            self.conn.rollback()

    def update_event(self, event_id, event_name, event_category, event_date, event_time, event_place, place_address):
        if not self.helpers.validate_date(event_date):
            print("Invalid date format. Please use YYYY-MM-DD")
            return

        try:
            self.cursor.execute("UPDATE event SET event_name = %s, event_category = %s, event_date = %s, event_time = %s, event_place = %s, place_address = %s WHERE event_id = %s",
                                (event_name, event_category, event_date, event_time, event_place, place_address, event_id))
            self.conn.commit()
            print("Event updated successfully")
        except mysql.connector.Error as err:
            print("Error:", err)
            self.conn.rollback()

    def delete_event(self, event_id):
        try:
            self.cursor.execute("DELETE FROM event WHERE event_id = %s", (event_id,))
            self.conn.commit()
            print("Event deleted successfully")
        except mysql.connector.Error as err:
            print("Error:", err)
            self.conn.rollback()

    def delete_all_events(self):
        try:
            self.cursor.execute("DELETE FROM event")
            self.cursor.execute("ALTER TABLE event AUTO_INCREMENT = 1")
            self.conn.commit()
            print("All events deleted successfully")
        except mysql.connector.Error as err:
            print("Error:", err)
            self.conn.rollback()

    def list_events(self):
        try:
            self.cursor.execute("SELECT * FROM event")
            rows = self.cursor.fetchall()
            print(tabulate(rows, headers="keys", tablefmt="grid"))
        except mysql.connector.Error as err:
            print("Error:", err)

    def filter_events_by_category(self, category):
        try:
            self.cursor.execute("SELECT * FROM event WHERE event_category = %s", (category,))
            rows = self.cursor.fetchall()
            print(tabulate(rows, headers="keys", tablefmt="grid"))
        except mysql.connector.Error as err:
            print("Error:", err)

    def filter_events(self, year=None, month=None):
        query = "SELECT * FROM event WHERE "
        conditions = []

        if year:
            conditions.append("YEAR(event_date) = {}".format(year))
        if month:
            conditions.append("MONTH(event_date) = {}".format(month))

        query += " AND ".join(conditions)

        try:
            self.cursor.execute(query)
            rows = self.cursor.fetchall()
            print(tabulate(rows, headers="keys", tablefmt="grid"))
        except mysql.connector.Error as err:
            print("Error:", err)
