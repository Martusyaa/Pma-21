INPUT_FILE_NAME = "students.txt"
FILE_NOT_FOUND = "File not found"
ERROR = "File is empty"
ERROR2 = "Invalid data format in line"
from student import Student
def print_student(student):
    for mark in student.marks:
        if mark < 3:
            print(f"Student {student.first_name.upper()} {student.last_name.upper()} failed the session.")
            break

students = []

try:
    with open(INPUT_FILE_NAME, 'r') as file:
        lines = file.readlines()
        if not lines:
            raise FileNotFoundError(ERROR)
        for line in lines:
            data = line.strip().split(' ')
            if len(data) < 4:
                print('Error:', ValueError(ERROR2))
            else:
                first_name = data[0]
                last_name = data[1]
                birth_date = data[2]
                marks = [int(mark) for mark in data[3].split(',')]
                student = Student(first_name, last_name, birth_date, marks)
                students.append(student)

except FileNotFoundError:
    print('Error:', FILE_NOT_FOUND)
except ValueError as e:
    print('Error:', e)
except Exception as e:
    print('Error:', e)

counts = []
for student in students:
    print_student(student)
for student in students:
    for mark in student.marks:
        if mark >= 3:
            counts.append(1)
        else:
            counts.append(0)
if all(count == 1 for count in counts):
    print('All students pass the exam.')
