from Students import *

class Executor:
    @staticmethod
    def find_students_who_failed(students, fail_grade=2):
        failed_students = []
        for student in students:
            if any(grade <= fail_grade for grade in student.grades):
                failed_students.append(student)
        return failed_students