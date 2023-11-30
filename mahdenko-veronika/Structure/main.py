from Student import Dekanat
if __name__ == '__main__':
    data_file = "Student.txt"
    dekanat_instance = Dekanat()
    dekanat_instance.read_matrix_from_file(data_file)
    dekanat_instance.print_failed_students()