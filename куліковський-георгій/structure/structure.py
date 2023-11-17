from read_file import Read_File


class Structure:
    
    
    def __init__(self, path):
        self.list_of_students = Read_File.read_file(path)
        
    def print_failed_students(self) -> list:
        self.failed_students = []
        for i in self.list_of_students:
            if not i.has_passed:
                self.failed_students.append(i)
        print(list(map(str,self.failed_students)))
        