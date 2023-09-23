class Vector():
    def __init__(self, length):
        self.length = length
        self.data = []

    def read_from_file(self, filename):
        with open(filename,'r') as file:
         self.data = [int(x) for x in file.readline().split()]

    def write_to_file(self, filename, vector_first, vector_second, operation, result):
        with open(filename, 'a') as file:
            file.write(f"{vector_first} {operation} {vector_second} = {result}\n")

    def add(self, other):
        try:
            if self.length != other.length:
                raise ValueError("Vector lengths are not equal, and addition is not possible.")

            summed_vector = Vector(self.length)
            for i in range(self.length):
                summed_vector.data.append(self.data[i] + other.data[i])

            return summed_vector
        except Exception as e:
            print(f"An error occurred during vector addition: {e}")
            return None  
    def multiply(self,other):
        multiplyed_vector = Vector(self.length)
        for i in range(self.length):
            multiplyed_vector.data.append(self.data[i] * other.data[i])
        return multiplyed_vector
    def division(self,other):
        divided_vector = Vector(self.length)
        for i in range(self.length):
            divided_vector.data.append(self.data[i] / other.data[i])
        return divided_vector
    def subtraction(self, other):
        substracted_vector = Vector(self.length)
        for i in range(self.length):
            substracted_vector.data.append(self.data[i] - other.data[i])
        return substracted_vector
    def __str__(self):
        return "[" + ", ".join(str(x) for x in self.data) + "]"


vector_first = Vector(5)
vector_second = Vector(5)

vector_first.read_from_file('first_vector.txt')
vector_second.read_from_file('second_vector.txt')

result_addition = vector_first.add(vector_second)
vector_first.write_to_file('results.txt', vector_first, vector_second, '+', result_addition)

result_subtraction = vector_first.subtraction(vector_second)
vector_first.write_to_file('results.txt', vector_first, vector_second, '-', result_subtraction)

result_multiplication = vector_first.multiply(vector_second)
vector_first.write_to_file('results.txt', vector_first, vector_second, '*', result_multiplication)

result_division = vector_first.division(vector_second)
vector_first.write_to_file('results.txt', vector_first, vector_second, '/', result_division)