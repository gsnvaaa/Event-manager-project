import mysql.connector
from helpers.helpers import Helpers

class BaseEventManager:
    def __init__(self):
        self.conn = mysql.connector.connect(
            database="event_manager",
            user="root",
            password="gasanova7",
            host="localhost"
        )
        self.cursor = self.conn.cursor(dictionary=True)
        self.helpers = Helpers()

    def close_connection(self):
        self.cursor.close()
        self.conn.close()
