import mysql.connector
import pandas as pd

class StudentDatabaseManagement:
    def __init__(self, host, user, password, database):
        
        self.db_config = {
            "host": host,
            "user": user,
            "password": password,
            "database": database
        }
        self.conn = None #To store the connection to the databasee
        self.cursor = None # Allow us to execute commands on the database.

    def connect_to_database(self):
        try:
            self.conn = mysql.connector.connect(**self.db_config)
            self.cursor = self.conn.cursor()
            print("Connected to the database successfully.")
        except mysql.connector.Error as err:
            print(f"Error connecting to the database: {err}")

    def close_connection(self):
        if self.cursor:
            self.cursor.close()#closes command execution
        if self.conn:
            self.conn.close()#closes database connection
            print("Database connection closed.")

    def read_csv(self, csv_file):
        try:
            data = pd.read_csv(csv_file)
            print("CSV Columns:", data.columns)
            return data
        except FileNotFoundError:
            print(f"Error: File {csv_file} not found.")
            return None
        except Exception as e:
            print(f"Error reading CSV: {e}")
            return None

    def add_data_to_database(self, data):
        if self.conn is None or self.cursor is None:
            print("Database connection is not established.")
            return
        
        try:
            for _, row in data.iterrows():
                self.cursor.execute("""
                    INSERT INTO students_records (Name, Email, Phone_Number, Mathematics, Science, History, English, Art, Computer_Science)
                    VALUES (%s, %s, %s, %s, %s, %s, %s,%s, %s)
                """, (
                    row['Name'],
                    row['Email'],
                    row['Phone_Number'],
                    row['Mathematics'],
                    row['Science'],
                    row['History'],
                    row['English'],
                    row['Art'],
                    row['Computer_Science']
                ))
            self.conn.commit()
            print("Data imported successfully!")
        except KeyError as e:
            print(f"Error: Missing column in CSV: {e}")
        except mysql.connector.Error as err:
            print(f"Database error: {err}")

    def import_csv_to_database(self, csv_file):
        self.connect_to_database()
        data = self.read_csv(csv_file)
        if data is not None:
            self.add_data_to_database(data)
        self.close_connection()


if __name__ == "__main__":
    db_manager = StudentDatabaseManagement(
        host="localhost",
        user="root",
        password="irutingaboRai1@",
        database="students"
    )

    csv_file_path = "C:/Users/RAISSA/Desktop/PYTHON/student_database_management/student_records.csv"
    db_manager.import_csv_to_database(csv_file_path)
