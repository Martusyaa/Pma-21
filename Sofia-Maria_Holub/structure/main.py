class Student:
    def __init__(self, first_name, last_name, birth_date, grades):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date
        self.grades = grades

    def has_passed_session(self):
        return "2" not in self.grades

def read_students_from_file(filename):
    students = []
    with open(filename, 'r') as file:
        for line in file:
            parts = line.strip().split(',')
            if len(parts) == 4:
                first_name = parts[0].strip()
                last_name = parts[1].strip()
                birth_date = parts[2].strip()
                grades = parts[3].strip().split()
                students.append(Student(first_name, last_name, birth_date, grades))
    return students

def find_students_who_failed(students):
    failed_students = [student for student in students if not student.has_passed_session()]
    return failed_students

def print_student(student):
    print(f"Student: {student.first_name} {student.last_name}")
    print(f"Birth Date: {student.birth_date}")
    print(f"Grades: {', '.join(student.grades)}")
    print()

if __name__ == "__main__":
    input_filename = "students.txt"
    students = read_students_from_file(input_filename)

    failed_students = find_students_who_failed(students)

    if failed_students:
        print("Students that failed:")
        for student in failed_students:
            print_student(student)
    else:
        print("All students passed")
