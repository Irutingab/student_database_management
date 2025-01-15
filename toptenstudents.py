import mysql.connector
import matplotlib.pyplot as plt
from typing import List, Tuple

class DatabaseConnection:
    def __init__(self, host: str, user: str, password: str, database: str):
        self.config = {
            "host": host,
            "user": user,
            "password": password,
            "database": database
        }
        self.conn = None
        self.cursor = None

    def connect(self):
        self.conn = mysql.connector.connect(**self.config)
        self.cursor = self.conn.cursor()

    def close(self):
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()

class StudentReport:
    def __init__(self, db_connection: DatabaseConnection):
        self.db = db_connection
        self.report_data = []
        self.class_average = 0

    def fetch_student_records(self) -> List[Tuple]:
        self.db.cursor.execute("""
            SELECT name, email, mathematics, science, history, english, art, computer_science 
            FROM students_records
        """)
        return self.db.cursor.fetchall()

    def calculate_percentages(self, students: List[Tuple]) -> None:
        total_percentages = 0
        for student in students:
            name, email, math, sci, hist, eng, art, cs = student
            grades = [math, sci, hist, eng, art, cs]
            total = sum(map(float, grades))
            percentage = total / 6
            total_percentages += percentage
            self.report_data.append((name, email, percentage))

        self.class_average = total_percentages / len(students) if students else 0
        self.report_data.sort(key=lambda x: x[2], reverse=True)

    def update_report_table(self) -> None:
        self.db.cursor.execute("DELETE FROM report")
        self.db.conn.commit()

        for data in self.report_data:
            self.db.cursor.execute("""
                INSERT INTO report (name, email, percentage, class_average)
                VALUES (%s, %s, %s, %s)
            """, (*data, self.class_average))
        self.db.conn.commit()

    def print_summary(self) -> None:
        if self.report_data:
            top_student = self.report_data[0]
            print(f"Top Student: {top_student[0]} with {top_student[2]:.2f}%")
        print(f"Class Average: {self.class_average:.2f}%")

    def plot_top_students(self, num_students: int = 10) -> None:
        top_students = self.report_data[:num_students]
        names = [student[0] for student in top_students]
        percentages = [student[2] for student in top_students]

        plt.figure(figsize=(10, 6))
        plt.barh(names, percentages, color='maroon')
        
        for i, percentage in enumerate(percentages):
            plt.text(percentage + 1, i, f"{percentage:.2f}%", va='center', color='black')

        plt.xlabel('Percentage')
        plt.ylabel('Students')
        plt.title(f'Top {num_students} Students by Percentage')
        plt.gca().invert_yaxis()
        plt.tight_layout()
        plt.show()

    def generate_report(self) -> None:
        try:
            self.db.connect()
            students = self.fetch_student_records()
            self.calculate_percentages(students)
            self.update_report_table()
            self.print_summary()
            self.plot_top_students()
        finally:
            self.db.close()

def main():
    db_config = DatabaseConnection(
        host="localhost",
        user="root",
        password="irutingaboRai1@",
        database="students"
    )
    
    report = StudentReport(db_config)
    report.generate_report()

if __name__ == "__main__":
    main()