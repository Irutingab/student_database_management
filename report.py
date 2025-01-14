import csvintosql
import mysql.connector

def student_report():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="irutingaboRai1@",
        database="students"
    )
    cursor = conn.cursor() #to excute the query in mysql

    cursor.execute("""
        SELECT name, email, mathematics, science, history, english, art, computer_science 
        FROM students_records
    """)
    students = cursor.fetchall() # retrieves all the students(info)

    report_data = []
    total_percentages = 0
    for student in students:
        name, email, math, sci, hist, eng, art, cs = student
        grades = [math, sci, hist, eng, art, cs]
        total = sum(map(float, grades)) # map executes a specified function, here since the grades are saved as strings, it tranforms them into floats
        percentage = total / 6
        total_percentages += percentage
        report_data.append((name, email, percentage)) #name, email, and student's percentage is saved as a tuple
        #report_data contains a list of tuples
        
        #the total_percentages eaquals to the sum of all the students' percentages devided by the number of students

    class_average = total_percentages / len(students) if students else 0

    report_data.sort(key=lambda x: x[2], reverse=True)# Specifies that the sorting should be based on the third item (percentage) in each tuple.
#reverse ensures that we sorted from the highest percentage to the lowest

    cursor.execute("DELETE FROM report")#clear exiting data, replace it with the most recent
    conn.commit()

    for data in report_data: #student's percentage along with the class average into the report table 
        cursor.execute("""
            INSERT INTO report (name, email, percentage, class_average)
            VALUES (%s, %s, %s, %s)
        """, (*data, class_average)) #inserts the class average as the fourth value
    conn.commit()

    if report_data:
        top_student = report_data[0]
        print(f"Top Student: {top_student[0]} with {top_student[2]:.2f}%")
    print(f"Class Average: {class_average:.2f}%")

    cursor.close()
    conn.close()

student_report()
