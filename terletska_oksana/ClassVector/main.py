INPUT_TXT = "input.txt"
OUTPUT_TXT = "output.txt"

class Vectors():

    def __init__(self, vector1=None, vector2=None):
        self.vector1 = vector1
        self.vector2 = vector2

    def read_from_file(self, filename=INPUT_TXT):
        try:
            with open(filename, 'r') as file:
                lines = file.readlines()
                if len(lines) != 2:
                    raise ValueError("Input file must contain exactly two lines for two vectors.")
                self.vector1 = [float(num) for num in lines[0].strip().split()]
                self.vector2 = [float(num) for num in lines[1].strip().split()]
        except FileNotFoundError:
            print(f"File '{filename}' not found.")
        except ValueError as e:
            print(e)

    def write_in_file(self, vector, filename=OUTPUT_TXT, operation_name=""):
        with open(filename, 'a') as file:
            vector_str = "\t\t".join(str(num) for num in vector)
            file.write(operation_name + ":\n")
            file.write(vector_str + "\n")

    def vector_addition(self):
        if len(self.vector1) != len(self.vector2):
            raise ValueError("Vectors must have the same length for addition.")
        sum_vector = [a + b for a, b in zip(self.vector1, self.vector2)]
        self.write_in_file(sum_vector, operation_name="Sum")

    def vector_subtraction(self):
        if len(self.vector1) != len(self.vector2):
            raise ValueError("Vectors must have the same length for subtraction.")
        subtraction_vector = [a - b for a, b in zip(self.vector1, self.vector2)]
        self.write_in_file(subtraction_vector, operation_name="Subtraction")

    def vector_multiplication(self):
        if len(self.vector1) != len(self.vector2):
            raise ValueError("Vectors must have the same length for multiplication.")
        multiplication_vector = [a * b for a, b in zip(self.vector1, self.vector2)]
        self.write_in_file(multiplication_vector, operation_name="Multiplication")

    def vector_division(self):
        if len(self.vector1) != len(self.vector2):
            raise ValueError("Vectors must have the same length for division.")
        try:
            division_vector = [a / b for a, b in zip(self.vector1, self.vector2)]
            self.write_in_file(division_vector, operation_name="Division")
        except ZeroDivisionError:
            print("Division by zero")

v = Vectors()

v.read_from_file()

v.vector_addition()
v.vector_subtraction()
v.vector_multiplication()
v.vector_division()


"""INPUT_TXT = "input.txt"
OUTPUT_TXT = "output.txt"
class Vectors():

    def __init__ (self ,vector1, vector2):
        self.vector1 = vector1
        self.vector2 = vector2

    def read_from_file(self, filename):
        try:
            with open(filename, 'r') as file:
                lines = file.readlines()
                if len(lines) != 2:
                    raise ValueError("Input file must contain exactly two lines for two vectors.")
                self.vector1 = [float(num) for num in lines[0].strip().split()]
                self.vector2 = [float(num) for num in lines[1].strip().split()]
        except FileNotFoundError:
            print(f"File '{filename}' not found.")
        except ValueError as e:
            print(e)

        self.vector_addition = self.sum_vector()
        self.vector_subtraction = self.subtraction_vector()
        self.vector_multiplication = self.multiplication_vector()
        self.vector_division = self.division_vector()

'''
    def write_in_file(self, vector, OUTPUT_TXT, operation_name):
        with open(OUTPUT_TXT, 'a') as file:
            vector_str = ""
            for num in vector:
                vector_str += str(num) + "\t \t"
            vector_str = vector_str.strip()
            file.write(vector_str)
            file.write('\n') '''


def print(self):
    print(f"First vector: {self.first_vector}")
    print(f"\nSecond vector: {self.second_vector}")
    print(f"\nSum: {self.sum_vector}")
    print(f"\nSubtraction: {self.subtraction_vector}")
    print(f"\nMultiplication: {self.multiplication_vector}")
    print(f"\nDivision: {self.division_vector}")
    with open(OUTPUT_TXT, 'w') as file:
        print(f"{self.first_vector} + {self.second_vector} = {self.sum_vector}", file=file)
        print(f"{self.first_vector} - {self.second_vector} = {self.subtraction_vector}", file=file)
        print(f"{self.first_vector} * {self.second_vector} = {self.multiplication_vector}", file=file)
        print(f"{self.first_vector} / {self.second_vector} = {self.division_vector}", file=file)

    def vector_addition(self, vector1, vector2):
        if len(vector1) != len(vector2):
            ValueError("different len")
        sum_vector = []
        for i in range(len(vector1)):
            sum_vector.append(vector1[i] + vector2[i])
        self.write_in_file(sum_vector, OUTPUT_TXT,"Sum:")
        return sum_vector

    def vector_subtraction(self, vector1, vector2):
        if len(vector1) != len(vector2):
            ValueError("different len")
        subtraction_vector = []
        for i in range(len(vector1)):
            subtraction_vector.append(vector1[i] - vector2[i])
        return subtraction_vector

    def vector_multiplication(self, vector1, vector2):
        if len(vector1) != len(vector2):
            ValueError("different")
        multiplication_vector = []
        for i in range(len(vector1)):
            multiplication_vector.append(vector1[i] * vector2[i])
        return multiplication_vector

    def vector_division(self, vector1, vector2):
        if len(vector1) != len(vector2):
            ValueError("different len")
        division_vector = []
        try:
            for i in range(len(vector1)):
                division_vector.append(vector1[i] / vector2[i])
            return division_vector
        except ZeroDivisionError:
            print("Division by zero")

    """
