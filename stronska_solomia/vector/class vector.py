class Vector:
    def __init__(self, elements):
        if not all(isinstance(x, (int, float)) for x in elements):
            raise ValueError("All elements of the vector must be numbers")
        self.elements = elements

    def add(self, other):
        if len(self.elements) != len(other.elements):
            raise ValueError("Vectors must have the same length for addition")
        result = [x + y for x, y in zip(self.elements, other.elements)]
        return Vector(result)

    def subtract(self, other):
        if len(self.elements) != len(other.elements):
            raise ValueError("Vectors must have the same length for subtraction")
        result = [x - y for x, y in zip(self.elements, other.elements)]
        return Vector(result)

    def divide(self, other):
        if len(self.elements) != len(other.elements):
            raise ValueError("Vectors must have the same length for division")
        result = [x / y if y != 0 else float('inf') for x, y in zip(self.elements, other.elements)]
        return Vector(result)

    def dot_product(self, other):
        if len(self.elements) != len(other.elements):
            raise ValueError("Vectors must have the same length for dot product")
        result = sum(x * y for x, y in zip(self.elements, other.elements))
        return result


with open('input.txt', 'r') as input_file:
    lines = input_file.readlines()

    vector1_elements = [float(x) for x in lines[0].split()]


    vector2_elements = [float(x) for x in lines[1].split()]


    vector1 = Vector(vector1_elements)
    vector2 = Vector(vector2_elements)


with open('output.txt', 'w') as output_file:
    # Додавання
    result_addition = vector1.add(vector2)
    output_file.write("Addition Result: {}\n".format(result_addition.elements))


    result_subtraction = vector1.subtract(vector2)
    output_file.write("Subtraction Result: {}\n".format(result_subtraction.elements))


    result_division = vector1.divide(vector2)
    output_file.write("Division Result: {}\n".format(result_division.elements))


    result_dot_product = vector1.dot_product(vector2)
    output_file.write("Dot Product Result: {}\n".format(result_dot_product))
