import csv

with open('pandas/student_records.csv', 'r')as csvfile:
    csvz_reader = csv.reader(csvfile)
    for line in csvz_reader:
        print(line)