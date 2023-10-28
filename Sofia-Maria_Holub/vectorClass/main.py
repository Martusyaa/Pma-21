class Vector:
    def __init__(self, components):#обєкт,параметр
        self.components = components

    def __str__(self):
        return "(" + ", ".join(map(str, self.components)) + ")"

    def __add__(self, other):
        if len(self.components) != len(other.components):
            raise ValueError("Вектори мають різну довжину")
        return Vector([a + b for a, b in zip(self.components, other.components)])# used to combine two or more iterable dictionaries

    def __sub__(self, other):
        if len(self.components) != len(other.components):
            raise ValueError("Вектори мають різну довжину")
        return Vector([a - b for a, b in zip(self.components, other.components)])

    def __mul__(self, scalar):
        return Vector([a * scalar for a in self.components])

    def __truediv__(self, scalar):
        if scalar == 0:
            raise ValueError("Ділення на нуль неможливе")
        return Vector([a / scalar for a in self.components])


def perform_operations(input_file_name, output_file_name):
    with open(input_file_name, 'r') as input_file, open(output_file_name, 'w') as output_file:
        vector1_components = list(map(float, input_file.readline().strip().split(',')))
        vector2_components = list(map(float, input_file.readline().strip().split(',')))

        firstvector = Vector(vector1_components)
        secondvector = Vector(vector2_components)

        sum_vector = firstvector + secondvector
        diff_vector = firstvector - secondvector
        scalar_mul_vector = firstvector * 2
        scalar_div_vector =firstvector / 2 #скаляр можна змінити

        output_file.write(f"Sum: {sum_vector}\n")
        output_file.write(f"Substraction: {diff_vector}\n")
        output_file.write(f"Multyplication(first): {scalar_mul_vector}\n")
        output_file.write(f"Division(first): {scalar_div_vector}\n")


input_file_name = 'vectors.txt'
output_file_name = 'result.txt'
perform_operations(input_file_name, output_file_name)


with open(output_file_name, 'r') as result_file:
    for line in result_file:
        print(line.strip())
