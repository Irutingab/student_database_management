import csvintosql
import mysql.connector
import pandas as pd
import csv

def add_new_student():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="irutingaboRai1@",
        database="students"
    )
    cursor = conn.cursor()

    print("Enter the details of the new student:")
    
    name = input("Enter the student's name: ")
    email = input("Enter the student's email: ")
    
    cursor.execute("SELECT * FROM students_records WHERE email = %s", (email,))
    if cursor.fetchone():
        print("Error: This email already exists!")
        with open('failedstudents.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([email])
        print(f"Duplicate email {email} saved to 'failedstudents.csv'.")
    else:
        phone_number = input("Enter the student's phone number: ")
        mathematics = input("Enter the grade for Mathematics: ")
        science = input("Enter the grade for Science: ")
        history = input("Enter the grade for History: ")
        english = input("Enter the grade for English: ")
        art = input("Enter the grade for Art: ")
        computer_science = input("Enter the grade for Computer Science: ")

        cursor.execute(""" 
            INSERT INTO students_records (name, email, phone_number, mathematics, science, history, english, art, computer_science) 
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, (name, email, phone_number, mathematics, science, history, english, art, computer_science))
        
        conn.commit()
        print("New student added successfully!")
    
    cursor.close()
    conn.close()
def update_student_info():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="irutingaboRai1@",
        database="students"
    )
    cursor = conn.cursor()

    email_to_update = input("Enter the student's email to update: ")
    
    cursor.execute("SELECT * FROM students_records WHERE email = %s", (email_to_update,))
    student = cursor.fetchone()
    
    if student:
        print(f"Student found: {student}")
        print("What would you like to update?")
        print("1. Update name")
        print("2. Update grades")
        print("3. Update email")
        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            new_name = input(f"Enter the new name (current: {student[0]}): ")
            if new_name:
                cursor.execute("""
                    UPDATE students_records 
                    SET name = %s
                    WHERE email = %s
                """, (new_name, email_to_update))
                conn.commit()
                print("Name updated successfully!")
        
        elif choice == '2':
            mathematics = input(f"Enter new grade for Mathematics (current: {student[3]}): ")
            science = input(f"Enter new grade for Science (current: {student[4]}): ")
            history = input(f"Enter new grade for History (current: {student[5]}): ")
            english = input(f"Enter new grade for English (current: {student[6]}): ")
            art = input(f"Enter new grade for Art (current: {student[7]}): ")
            computer_science = input(f"Enter new grade for Computer Science (current: {student[8]}): ")

            cursor.execute("""
                UPDATE students_records 
                SET mathematics = %s, science = %s, history = %s, english = %s, art = %s, computer_science = %s
                WHERE email = %s
            """, (mathematics or student[3], science or student[4], history or student[5],
                english or student[6], art or student[7], computer_science or student[8], email_to_update))
            conn.commit()
            print("Grades updated successfully!")

        elif choice == '3':
            new_email = input(f"Enter the new email (current: {student[2]}): ")
            cursor.execute("SELECT * FROM students_records WHERE email = %s", (new_email,))
            if cursor.fetchone():
                print("Error: This email already exists!")
                
                with open('failedstudents.csv', 'a', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow([new_email])
                print(f"Duplicate email {new_email} saved to 'failedstudents.csv'.")
            else:
                cursor.execute("UPDATE students_records SET email = %s WHERE email = %s", (new_email, email_to_update))
                conn.commit()
                print("Email updated successfully!")
        
        else:
            print("Invalid choice! Please try again.")
    else:
        print("Error: No student found with this email.")
    
    cursor.close()
    conn.close()

def delete_student_info():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="irutingaboRai1@",
        database="students"
    )
    cursor = conn.cursor()

    email_to_delete = input("Enter the student's email to delete: ")
    
    cursor.execute("SELECT * FROM students_records WHERE email = %s", (email_to_delete,))
    student = cursor.fetchone()

    if student:
        confirm = input(f"Are you sure you want to delete the record for {student[0]} (y/n)? ")
        if confirm.lower() == 'y':
            cursor.execute("DELETE FROM students_records WHERE email = %s", (email_to_delete,))
            conn.commit()
            print("Student record deleted successfully.")
        else:
            print("Deletion canceled.")
    else:
        print("Error: No student found with this email.")
    
    cursor.close()
    conn.close()

def main():
    while True:
        print("Student Database Management")
        print("1. Add New Student")
        print("2. Update Student Information")
        print("3. Delete Student Information")
        print("4. Exit")
        
        choice = input("Enter your choice: ")

        if choice == '1':
            add_new_student()
        elif choice == '2':
            update_student_info()
        elif choice == '3':
            delete_student_info()
        elif choice == '4':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
