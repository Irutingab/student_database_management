import mysql.connector
import pandas as pd

# Database connection class
class TruncateDatabase:
    def __init__(self, host, user, password, database):
        self.db_config = {
            "host": host,
            "user": user,
            "password": password,
            "database": database
        }
        self.conn = None
        self.cursor = None

    def connect_to_database(self):
        try:
            self.conn = mysql.connector.connect(**self.db_config)
            self.cursor = self.conn.cursor()
            print("Connected to the database successfully!")
        except mysql.connector.Error as err:
            print(f"Error connecting to the database: {err}")
            self.conn = None
            self.cursor = None

    def close_connection(self):
        try:
            if self.cursor:
                self.cursor.close()
            if self.conn:
                self.conn.close()
                print("Connection closed.")
        except mysql.connector.Error as err:
            print(f"Error closing the connection: {err}")

    def truncate_database(self):
        if not self.cursor:
            print("No active database connection.")
            return
        try:
            self.cursor.execute("TRUNCATE TABLE students_records")  # Replace with your actual table name
            self.conn.commit()
            print("Table truncated successfully.")
        except mysql.connector.Error as err:
            print(f"Error: {err}")

# Main block
if __name__ == "__main__":
    db_manager = TruncateDatabase(
        host="localhost",
        user="root",
        password="irutingaboRai1@",
        database="students"
    )
    try:
        db_manager.connect_to_database()
        db_manager.truncate_database()
    finally:
        db_manager.close_connection()
