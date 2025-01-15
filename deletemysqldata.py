import mysql.connector
import pandas as pd
#database connection
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="irutingaboRai1@",
    database="students"  # add database name
)

cursor = conn.cursor()
#Truncate data
try:
    cursor.execute("TRUNCATE TABLE students_records")  # table name
    conn.commit()
    print("Table truncated successfully.")
except mysql.connector.Error as err:
    print(f"Error: {err}")
finally:
    #Close connection
    cursor.close()
    conn.close()
