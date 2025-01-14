import mysql.connector
import matplotlib.pyplot as plt

def student_report():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="irutingaboRai1@",
        database="students"
    )
    cursor = conn.cursor()

    cursor.execute("""
        SELECT name, email, mathematics, science, history, english, art, computer_science 
        FROM students_records
    """)
    students = cursor.fetchall()

    report_data = []
    total_percentages = 0
    for student in students:
        name, email, math, sci, hist, eng, art, cs = student
        grades = [math, sci, hist, eng, art, cs]
        total = sum(map(float, grades))
        percentage = total / 6
        total_percentages += percentage
        report_data.append((name, email, percentage))

    class_average = total_percentages / len(students) if students else 0

    # Sort by percentage (from highest to lowest)
    report_data.sort(key=lambda x: x[2], reverse=True)

    cursor.execute("DELETE FROM report")
    conn.commit()

    for data in report_data:
        cursor.execute("""
            INSERT INTO report (name, email, percentage, class_average)
            VALUES (%s, %s, %s, %s)
        """, (*data, class_average))
    conn.commit()

    if report_data:
        top_student = report_data[0] #index 0 for the highest % in report table
        print(f"Top Student: {top_student[0]} with {top_student[2]:.2f}%")
    print(f"Class Average: {class_average:.2f}%")

    top_10_students = report_data[:10]  #top 10 records
    names = [student[0] for student in top_10_students] #names for the top 10 std
    percentages = [student[2] for student in top_10_students]  #%on the second index fir the top 10 std

    plt.figure(figsize=(10, 6))#width:10 inches & height 6 inches.

    plt.barh(names, percentages, color='maroon') #horizontal bar graph, names:y & percentages: x.
    for i, percentage in enumerate(percentages):
        plt.text(percentage + 1, i, f"{percentage:.2f}%", va='center', color='black')

    plt.xlabel('Percentage')
    plt.ylabel('Students')
    plt.title('Top 10 Students by Percentage')
    plt.gca().invert_yaxis()#to make sure the highest % is at the top
    plt.tight_layout()#to adjust the layouts for everything to fit correcty on the graph
    plt.show()

    cursor.close()
    conn.close()

student_report()
