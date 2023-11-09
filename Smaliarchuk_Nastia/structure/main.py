from Student import Student
import datetime
import re


def input_from_file(filename):
    students = []
    try:
        with open(filename) as file:
            for line in file:
                try:
                    line = line.strip()
                    if len(line) == 0:
                        continue
                    line = line.split(" ")
                    grades = []
                    for index in range(3, len(line)):
                        grades.append(int(line[index]))
                    date = datetime.date(*reversed([int(elem) for elem in line[2].split(".") ]))
                    student = Student(line[0],line[1], date, grades)
                    students.append(student)
                except ValueError as e:
                    print(f"Invalid data: {e}")
                    continue
                return students
    except FileNotFoundError:(
        print(f"File '{filename}' not found."))
    except Exception as e:
        print(f"An error occurred: {e}")


students = input_from_file("students.txt")
print("\tSurname\tName\tDate\tGrades")
for student in students:
    print(student, "\n")

students_with_2 = [student for student in students if 2 in student.grades]
students_with_2.sort(key=lambda student: student.surname)
print("sorted by surname with mark 2:")
for student in students_with_2:
    print(student, "\n")
if len(students_with_2) == 0:
    print("No students found")
failed_students = [student for student in students if all(grade < 3 for grade in student.grades)]
print("students who did not cope with the session:")
for student in failed_students:
    print(student, "\n")
if len(failed_students) == 0:
    print("No students were found who failed the session")
