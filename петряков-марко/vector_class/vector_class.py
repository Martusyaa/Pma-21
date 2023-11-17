line_number = 0
class Vector:
    def __init__(self):
        self.vector = []
        self.create_vector()

    def vector_check(self, vector2):
        if len(self.vector) != len(vector2.vector):
            raise Exception("Can`t do action cause of len error!")

    def create_vector(self):
        global line_number
        with open("vectors.txt", "r+") as file:
            lines = file.readlines()

            if line_number > len(lines):
                raise IndexError("Enter new line to a file!")

            data = lines[line_number].split(",")
            self.vector = [int(x) for x in data if x.isdigit()]
            line_number = line_number + 1

    def add_vector(self,vector2):
        self.vector_check(vector2)
        for element in range(len(self.vector)):
            self.vector[element] += vector2.vector[element]

    def subtract(self, vector2):
        self.vector_check(vector2)
        for element in range(len(self.vector)):
            self.vector[element] -= vector2.vector[element]

    def multiply_vectorno(self, vector2):
        if len(self.vector) != 3 or len(vector2.vector) != 3:
            raise Exception("One of the vector length is not equal to 3")
        matrix = []
        matrix.append(self.vector)
        matrix.append(vector2.vector)

        value1 = matrix[0][1] * matrix[1][2] - matrix[0][2] * matrix[1][1]
        value2 = -1 * (matrix[0][0] * matrix[1][2] - matrix[1][0] * matrix[0][2])
        value3 = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

        self.vector.clear()
        self.vector.append(value1)
        self.vector.append(value2)
        self.vector.append(value3)

    def multiply_on_vector(self,vector2):
        for i in range(len(self.vector)):
            value = self.vector[i] * vector2.vector[i]
            self.vector[i] = value

    def dilennia(self, vector2):
        for i in range(len(self.vector)):
            value = self.vector[i] / vector2.vector[i]
            value = round(value, 1)
            self.vector[i] = value

    def print_vector(self):
        for element in self.vector:
            print(element,end="\t")
        print()
        print()

    def output_vector(self):
        with open("vectors_output.txt", "w") as file_output:
            for e in self.vector:
                file_output.write(str(e) + ",")


v = Vector()
v.print_vector()
v2 = Vector()
v2.print_vector()

# v.add_vector(v2)
# v.print_vector()


# v.subtract(v2)
# v.print_vector()

v.multiply_on_vector(v2)
v.print_vector()
v.output_vector()


