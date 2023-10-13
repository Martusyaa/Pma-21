INPUT_FILE_NAME = "students.txt"
FILE_NOT_FOUND = "File not found"
ERROR = "File is empty"
ERROR2 = "Invalid data format in line"
from student import Student
def print_student(student):
    for i in student.marks:
        if i < 3:
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
                raise FileNotFoundError(ERROR2)
            first_name = data[0]
            last_name = data[1]
            birth_date = data[2]
            marks = [int(mark) for mark in data[3].split(',')]
            student = Student(first_name, last_name, birth_date, marks)
            students.append(student)

except FileNotFoundError as e:
    print('Error:', e)
count = []
for student in students:
    print_student(student)
    if all(i >= 3 for i in student.marks):
        count.append(1)
    else:
        count.append(0)
if all(i == 1 for i in count):
    print('All students pass exam.')


