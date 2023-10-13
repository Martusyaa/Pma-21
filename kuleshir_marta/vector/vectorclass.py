class Vector:
    def __init__(self, values):
        if not all(isinstance(x, (int, float)) for x in values):
            raise ValueError("All elements of the vector must be numbers")
        self.values = values

    def __add__(self, other):
        if len(self.values) != len(other.values):
            raise ValueError("Для додавання векторів повинні мати однакові розміри.")
        result = [x + y for x, y in zip(self.values, other.values)]
        return Vector(result)

    def __sub__(self, other):
        if len(self.values) != len(other.values):
            raise ValueError("Для віднімання векторів повинні мати однакові розміри.")
        result = [x - y for x, y in zip(self.values, other.values)]
        return Vector(result)

    def dot(self, other):
        if len(self.values) != len(other.values):
            raise ValueError("Для скалярного добутку векторів повинні мати однакові розміри.")
        result = sum(x * y for x, y in zip(self.values, other.values))
        return result

    def __truediv__(self, other):
        if len(self.values) != len(other.values):
            raise ValueError("Для поелементного ділення векторів повинні мати однакові розміри.")
        result = [x / y for x, y in zip(self.values, other.values)]
        return Vector(result)


try:
    with open('input.txt') as input_file:
        lines = input_file.readlines()

        vector1 = Vector([float(x) for x in lines[0].split()])
        vector2 = Vector([float(x) for x in lines[1].split()])

except FileNotFoundError:
    print("Файл 'input.txt' не знайдений.")

try:
    with open('output.txt', 'w') as output_file:
        output_file.write("Вектор 1: {}\n".format(vector1.values))
        output_file.write("Вектор 2: {}\n".format(vector2.values))

        result_addition = vector1 + vector2
        output_file.write("Додавання: {}\n".format(result_addition.values))

        result_subtraction = vector1 - vector2
        output_file.write("Віднімання: {}\n".format(result_subtraction.values))

        dot_product = vector1.dot(vector2)
        output_file.write("Скалярний добуток: {}\n".format(dot_product))

        result_elementwise_division = vector1 / vector2
        output_file.write("Поелементне ділення: {}\n".format(result_elementwise_division.values))
except FileNotFoundError:
    print("Файл 'output.txt' не знайдений.")
