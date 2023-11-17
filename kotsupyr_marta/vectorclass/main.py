INPUT_FILE="input.txt"
RESULT_FILE="result.txt"
ERROR="Vectors must have the same length "
ERROR1="Division by zero is not allowed"
class Vector:
    def __init__(self, elements):
        self.elements = elements
    def __str__(self):
        return str(self.elements)
    def __add__(self, other):
        if len(self.elements) != len(other.elements):
            raise ValueError(ERROR)
        result = [x + y for x, y in zip(self.elements, other.elements)]
        return Vector(result)
    def __sub__(self, other):
        if len(self.elements) != len(other.elements):
            raise ValueError(ERROR)
        result = [x - y for x, y in zip(self.elements, other.elements)]
        return Vector(result)
    def __mul__(self, other):
        result = sum([x * y for x,y in zip(self.elements,other.elements)])
        return Vector(result)
    def __truediv__(self, scalar):
        if scalar == 0:
            raise ValueError(ERROR1)
        result = [x / scalar for x in self.elements]
        return Vector(result)
def read_vectors_from_file(INPUT_FILE):
    vectors = []
    with open(INPUT_FILE, 'r') as file:
        for line in file:
            elements = [float(x) for x in line.split()]
            vectors.append(Vector(elements))
    return vectors
def write_vector_to_file(vector, explanation, RESULT_FILE):
    with open(RESULT_FILE, 'a') as file:
        file.write(explanation + '\n')
        file.write(str(vector) + '\n')
vectors = read_vectors_from_file(INPUT_FILE)
result_addition = vectors[0] + vectors[1]
result_subtraction = vectors[0] - vectors[1]
result_multiplication = vectors[0] * vectors[1]
scalar = 2
result_division = vectors[1] / scalar
write_vector_to_file(result_addition, "Результат додавання:", RESULT_FILE)
write_vector_to_file(result_subtraction, "Результат віднімання:", RESULT_FILE)
write_vector_to_file(result_multiplication, "Результат множення:", RESULT_FILE)
write_vector_to_file(result_division, "Результат ділення на скаляр:", RESULT_FILE)
