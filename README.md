STUDENT DATABASE MANAGEMENT
This project contains a csv file conataing students records(name, email, phone number, and their grades in 6 courses).
The program(csvintosql.py) imports the data from python to (students_records) in mysql.
After importing the data into our data base, we have to make sure users can interact with it be bale to accomplish various operations.
Since, students may come and go, we have to make sure the staff could edit students information through(studentdatabmanagement.py).

Users can:
 1. Add a new student
 2. Delete an existing student
 3. update students records(name, email, grades). Note that you can edit one oh these or all of them.
 4. Exit. If there nothing to edit,users can easly exit the program by entering 4.                                                                                                 
While updating students information, if you enter an email that already exits(email is our primary key in the database since it was the only thing that can be unique and controled by the school staff),
the program kindly tells you that the email already exists, and that you should, enter a valid email.
Meanwhile for the program not to crash, we save the duplicated email in  a csv file(failedstudents.csv).

