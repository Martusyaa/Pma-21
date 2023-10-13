INPUT_FILE_NAME = 'input.txt'


class Vector:
    def __init__(self, elements):
        try:
            if not all(isinstance(elem, (int, float)) for elem in elements):
                raise ValueError("Список елементів має містити тільки числа (int або float).")
            self.elements = elements
        except ValueError as e:
            print(e)

    def __str__(self):
        return str(self.elements)

    def __len__(self):
        return len(self.elements)

    def __add__(self, other):
        try:
            if len(self) != len(other):
                raise ValueError("Вектори мають мати однакову довжину для додавання")

            result_elements = [a + b for a, b in zip(self.elements, other.elements)]
            return Vector(result_elements)
        except ValueError as e:
            print(e)
            return None

    def __sub__(self, other):
        try:
            if len(self) != len(other):
                raise ValueError("Вектори мають мати однакову довжину для віднімання")

            result_elements = [a - b for a, b in zip(self.elements, other.elements)]
            return Vector(result_elements)
        except ValueError as e:
            print(e)
            return None

    def __mul__(self, other):
        try:
            if len(self) != len(other):
                raise ValueError("Вектори мають мати однакову довжину для поелементного множення")

            result_elements = [a * b for a, b in zip(self.elements, other.elements)]
            return Vector(result_elements)
        except ValueError as e:
            print(e)
            return None

    def __truediv__(self, other):
        try:
            if len(self) != len(other):
                raise ValueError("Вектори мають мати однакову довжину для поелементного ділення")
            if any(b == 0 for b in other.elements):
                raise ValueError("Ділення на нуль неможливе.")

            result_elements = [a / b for a, b in zip(self.elements, other.elements)]
            return Vector(result_elements)
        except ValueError as e:
            print(e)
            return None

try:
    with open(INPUT_FILE_NAME, 'r') as file:
        lines = file.readlines()
except FileNotFoundError:
    print("File not found: ", INPUT_FILE_NAME)

vectors = []
for line in lines:
    values = line.split()
    vector = [float(value) for value in values]
    vectors.append(vector)
vector_first = Vector(vectors[0])
vector_second = Vector(vectors[1])
# Приклад використання:


print("Вектор 1:", vector_first)
print("Вектор 2:", vector_second)

# Додавання векторів
summa = vector_first + vector_second
print("Сума векторів:", summa)

# Віднімання векторів
sub = vector_first - vector_second
print("Різниця векторів:", sub)

# Множення вектора на скаляр
mult = vector_first.__mul__(vector_second)
print("Поелементне множення векторів:", mult)

# Ділення вектора на скаляр
div = vector_first.__truediv__(vector_second)
print("Поелементне ділення векторів:", div)

with open('result.txt', 'w') as output_file:
    output_file.write(f"{vector_first} + {vector_second} = {summa}\n")
    output_file.write(f"{vector_first} - {vector_second} = {sub}\n")
    output_file.write(f"{mult}\n")
    output_file.write(f"{div}\n")
