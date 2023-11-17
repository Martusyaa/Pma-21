from student import Student
from dekanat import Dekanat

student = Student()
student.read_from_file()
st = Student()
st.read_from_file()
aboba=Student()
aboba.read_from_file()
d = Dekanat()

d.check_students(student)
d.check_students(st)
d.check_students(aboba)
