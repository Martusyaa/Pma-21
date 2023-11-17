INPUT_FILE_A = "vectorA.txt"
INPUT_FILE_B = "vectorB.txt"
OUTPUT_FILE = "output_results.txt"

class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"

    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y, self.z + other.z)
        else:
            raise ValueError("error")

    def __sub__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y, self.z - other.z)
        else:
            raise ValueError("error")

    def __mul__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x * other.x, self.y * other.y, self.z * other.z)
        else:
            raise ValueError("error")

    def __truediv__(self, other):
        if isinstance(other, Vector):
            if other.x == 0 or other.y == 0 or other.z == 0:
                raise ValueError("error-ділити на нуль не можна")
            return Vector(self.x / other.x, self.y / other.y, self.z / other.z)
        else:
                raise ValueError("error")


with open(INPUT_FILE_A, 'r') as file_A, open(INPUT_FILE_B, 'r') as file_B:
    lines_A = file_A.readlines()
    lines_B = file_B.readlines()

    vectors_A = []
    vectors_B = []

    for line in lines_A:
        values = line.strip().split()
        if len(values) == 3:
            x, y, z = map(float, values)
            vectors_A.append(Vector(x, y, z))

    for line in lines_B:
        values = line.strip().split()
        if len(values) == 3:
            x, y, z = map(float, values)
            vectors_B.append(Vector(x, y, z))

addition = vectors_A[0] + vectors_B[0]
subtraction = vectors_A[0] - vectors_B[0]
multiplication = vectors_A[0] * vectors_B[0]
division = vectors_A[0] / vectors_B[0]


with open(OUTPUT_FILE, 'w') as file:
    file.write("Додавання:\n")
    file.write(str(addition) + '\n')

    file.write("\nВіднімання:\n")
    file.write(str(subtraction) + '\n')

    file.write("\nМноження:\n")
    file.write(str(multiplication) + '\n')

    file.write("\nДілення:\n")
    file.write(str(division) + '\n')
