import mysql.connector
import pandas as pd

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="irutingaboRai1@",
    database="students"
)

cursor = conn.cursor()

csv_file = 'C:/Users/RAISSA/Desktop/Dev/python/python-exercises/pandas/student_records.csv'

try:
    data = pd.read_csv(csv_file)


    print("CSV Columns:", data.columns)


    for _, row in data.iterrows():
        cursor.execute("""
            INSERT INTO students_records(name, email, phone_number, mathematics, science, history, english, art, computer_science) 
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, (
            row['Name'], 
            row['Email'], 
            row['Phone Number'], 
            row['Mathematics'], 
            row['Science'], 
            row['History'], 
            row['English'], 
            row['Art'], 
            row['Computer Science']
        ))

    conn.commit()
    print("Data imported successfully!")

except FileNotFoundError:
    print(f"Error: The file {csv_file} was not found.")
except KeyError as e:
    print(f"Error: Column not found in the CSV: {e}")
except mysql.connector.Error as err:
    print(f"Database error: {err}")
finally:
    if conn.is_connected():
        cursor.close()
        conn.close()
