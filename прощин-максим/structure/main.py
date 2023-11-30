from Class_Dekanat import Decanat

dekanat_instance = Decanat()

filename = "students.txt"

students = dekanat_instance.read_students(filename)

dekanat_instance.failed_students(students)