from constants import ERROR

def add_vectors(firstvector, secondvector):
    if len(firstvector) != len(secondvector):
        raise ValueError(ERROR)

    result = []
    for i in range(len(firstvector)):
        result.append(firstvector[i] + secondvector[i])
    return result

def subtract_vectors(firstvector, secondvector):
    if len(firstvector) != len(secondvector):
        raise ValueError("Довжина векторів має бути однакова")

    result = []
    for i in range(len(firstvector)):
        result.append(firstvector[i] - secondvector[i])
    return result

def multiply_vectors(firstvector, secondvector):
    if len(firstvector) != len(secondvector):
        raise ValueError("Довжина векторів має бути однакова")

    result = []
    for i in range(len(firstvector)):
        result.append(firstvector[i] * secondvector[i])
    return result

def divide_vectors(firstvector, secondvector):
    if len(firstvector) != len(secondvector):
        raise ValueError("Довжина векторів має бути однакова")

    result = []
    for i in range(len(firstvector)):
        if secondvector[i] == 0:
            raise ValueError("Ділення на нуль неможливе")
        result.append(firstvector[i] / secondvector[i])
    return result

def read_vector_from_file(file_path):
    with open(file_path, 'r') as file:
        vector = [int(x) for x in file.readline().strip().split(',')]
        return vector

vector_a = read_vector_from_file('vector_a.txt')
vector_b = read_vector_from_file('vector_b.txt')

sum_vector = add_vectors(vector_a, vector_b)
print("Сума:", sum_vector)

difference_vector = subtract_vectors(vector_a, vector_b)
print("Віднімання:", difference_vector)

product_vector = multiply_vectors(vector_a, vector_b)
print("Множення(вектор):", product_vector)

division_vector = divide_vectors(vector_a, vector_b)
print("Ділення(вектор):", division_vector)

with open('result.txt', 'w') as result_file:
    result_file.write("Sum: " + ', '.join(map(str, sum_vector)) + '\n')
    result_file.write("Substacrion: " + ', '.join(map(str, difference_vector)) + '\n')
    result_file.write("Multiplication(Vector): " + ', '.join(map(str, product_vector)) + '\n')
    result_file.write("Division(Vector): " + ', '.join(map(str, division_vector)) + '\n')
