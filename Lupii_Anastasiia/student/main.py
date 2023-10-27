class Student:
    def __init__(self,first_name,last_name,marks_list, birthday):
        self.first_name = first_name
        self.last_name =last_name
        self.marks_list = marks_list
        self.birthday = birthday

    def __str__(self):
        marks_str = ""
        for mark in self.marks_list:
            marks_str += mark + ' '
        student_str = self.last_name + ' ' + self.first_name + ' ' + 'Marks:\n' + marks_str
        return student_str

    def session_failed(self):

        for mark in self.marks_list:

            if int(mark) < 51:
                return "not pass session"
        return "pass session"
def read_from_file(file_name):
    students_list = []
    try:
        with open(file_name, "r") as file:
                for students in file:
                    current_student = students.split(',')
                    last_name = current_student[0]

                    first_name = current_student[1]
                    birthday = current_student[2]

                    marks_list = current_student[3].split(' ')
                    students_list.append(Student(last_name, first_name, marks_list, birthday))
        return students_list
    except FileNotFoundError:
        print(f"File '{filename}' not found.")



def print_students_who_did_not_pass(students_list):
    print("\nDid not pass:")

    if not students_list:
        print("No students in the list.")
    for student in students_list:
        result = student.session_failed()
        if result == "not pass session":
            print(f"{student.first_name} {student.last_name} {student.birthday} {student.marks_list} did not pass session")
    if result == "pass session":
        print("all students pass session")
try:
    filename = 'students.txt'
    students_list = read_from_file(filename)
    print("All:")
    for student in students_list:
        print(student)

    print_students_who_did_not_pass(students_list)
except Exception as e:
    print(f"Error")
except FileNotFoundError:
    print(f"File '{filename}' not found")