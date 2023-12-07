from Students import *
from files import *
from Executor import *

students = read_students_from_file(FILE_PATH)
executor = Executor()
failed_students = executor.find_students_who_failed(students)

if not failed_students:
    print("Impossible, no failed students left.")
else:
    print("Students, who has failed this city:")
    for student in failed_students:
        print(f"{student.first_name} {student.last_name}")