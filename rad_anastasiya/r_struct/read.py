from Student import Student


class Read_File:


    def read_file(path):
        processed_list_of_students = []
        with open(path) as file:
            raw_list_of_students = file.read().split("\n")
            for i in raw_list_of_students:
                raw_student = i.split()
                processed_list_of_students.append(Student(raw_student[0], raw_student[1],\
                    raw_student[2], map(int,list(raw_student[3].strip('[]').split(',')))))
        return processed_list_of_students