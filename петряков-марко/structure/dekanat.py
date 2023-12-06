import json
from datetime import date
from student import Student


class Dekanat:
    def check_students(self, stud: Student):
        target = 51
        average = int(sum(stud.marks) / len(stud.marks))
        if average < target:
            print(f"{stud.name} {stud.surname} Average:{int(sum(stud.marks) / len(stud.marks))} Target:{target}")



