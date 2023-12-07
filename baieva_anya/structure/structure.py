class Student:
    name: str
    surname: str
    age: float
    birth_date: str
    marks: float


def read_from_file():
    objects = []
    with open("information.txt") as file:
        lines = file.readlines()
        for i in lines:
            a = Student()
            line = i.split(",")
            obj_marks = [int(i) for i in line[-1].split(" ") if i.isdigit()]
            a.name = line[0]
            a.surname = line[1]
            a.age = line[2]
            a.date_birth = line[3]
            a.marks = obj_marks
            objects.append(a)
    return objects


def talon():
    objects = read_from_file()
    fail_line = 51
    for i in objects:
        if (sum(i.marks) / len(i.marks)) < fail_line:
            print(f"{i.name} {i.surname}, Average estimate: {(int(sum(i.marks) / len(i.marks)))}")


talon()
