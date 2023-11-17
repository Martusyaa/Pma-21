from Class_Student import Student
info = {'Name': '', 'Surname': '', 'Date of Birth': '', 'Grades': ''}
FILENOTFOUND = "File not found"
def read_students(filename):
    students = []
    try:
        with open(filename, 'r') as file:
            student_info = info
            for line in file:
                line = line.strip()
                print(line)
                if line:
                    key, value = [item.strip() for item in line.split(':', 1)]
                    student_info[key] = value
                else:
                    students.append(Student(
                        name=student_info['Name'],
                        surname=student_info['Surname'],
                        birthdate=student_info['Date of Birth'],
                        grades=[int(grade) for grade in student_info['Grades'].split(',')]
                    ))
                    student_info = info
        return students
    except FileNotFoundError:
        print(FILENOTFOUND)


def failed_students(students):
    for student in students:
        if any(grade < 51 for grade in student.grades):
            print()
            print(f"{student.name} {student.surname} failed the session. At least one grade is below 51.")