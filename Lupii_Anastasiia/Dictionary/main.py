class Student:
    def __init__(self, first_name, last_name, ticket_number, grade):
        self.first_name = first_name
        self.last_name = last_name
        self.ticket_number = ticket_number
        self.grade = grade

    def __str__(self):
        return f"Name: {self.first_name}, last name: {self.last_name}, ticket number: {self.ticket_number}, grade: {self.grade}"

Students = {
    'Student1': Student("John", "Doe", "S1", 90),
    'Student2': Student("Jane", "Smith", "S2", 85),
    'Student3': Student("Alice", "Johnson", "S3", 92)
}

def display_students():
    print("Current dictionary:")
    for key, student in Students.items():
        print(key, student)

def remove_student(key):
    try:
        del Students[key]
        print("After deletting:")
        display_students()
    except KeyError:
        print(f"Key'{key}' is not found.")

def replace_student(key, new_student):
    try:
        if key in Students:
            Students[key] = new_student
            print("After chainging:")
            display_students()
        else:
            raise KeyError(f"Key '{key}' is not found")
    except KeyError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    display_students()

    remove_key = "Student3"
    remove_student(remove_key)

    new_student = Student( "Brown", "S4", 88)
    replace_key = 'Student3'
    replace_student(replace_key, new_student)