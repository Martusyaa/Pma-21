class StudentDictionary:
    def __init__(self):
        self.students = {}

    def add_student(self, student_id, name, age):
        self.students[student_id] = {'name': name, 'age': age}

    def get_student(self, student_id):
        return self.students.get(student_id, None)

    def update_student(self, student_id, name=None, age=None):
        if student_id in self.students:
            student = self.students[student_id]
            if name is not None:
                student['name'] = name
            if age is not None:
                student['age'] = age
            return True
        else:
            return False

    def delete_student(self, student_id):
        if student_id in self.students:
            del self.students[student_id]
            return True
        else:
            return False

    def display_students(self):
        for student_id, info in self.students.items():
            print(f"Student: {student_id}; Name: {info['name']}; Age: {info['age']}")

student_dict = StudentDictionary()
student_dict.add_student(1, 'John', 20)
student_dict.add_student(2, 'Jane', 22)
print("Список студентів:")
student_dict.display_students()
student_dict.update_student(1, name='John Doe', age=21)
print("\nОновлений список студентів:")
student_dict.display_students()
student_dict.delete_student(2)
print("\nСписок студентів після видалення:")
student_dict.display_students()