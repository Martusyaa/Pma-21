from Student import Student
if __name__ == '__main__':
    try:
        filename = "Student.txt"
        students = Student.read_matrix_from_file(filename)
        Student.print_failed_students(students)
    except FileNotFoundError:
        print(f"Файл '{filename}' не знайдено.")