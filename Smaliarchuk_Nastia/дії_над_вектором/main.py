def read_vectors(filename):
    vectors = []
    with open(filename, 'r') as file:
        for line in file:
            vector = [float(coord) for coord in line.strip().split()]
            vectors.append(vector)
    return vectors

def write_result(filename, result):
    with open(filename, 'a') as file:
        file.write(result + '\n')

def add_vectors(vector1, vector2):
    if len(vector1) != len(vector2):
        return "eror:vectors have different lenght"
    result = [v1 + v2 for v1, v2 in zip(vector1, vector2)]
    return "add_vectors: " + str(result)

def subtract_vectors(vector1, vector2):
    if len(vector1) != len(vector2):
        return "eror:vectors have different lenght"
    result = [v1 - v2 for v1, v2 in zip(vector1, vector2)]
    return "subtract_vectors: " + str(result)

def multiply_vectors_elementwise(vector1, vector2):
    if len(vector1) != len(vector2):
        return "eror:vectors have different lenght"
    result = [v1 * v2 for v1, v2 in zip(vector1, vector2)]
    return "multiply_vectors_elementwise: " + str(result)

def divide_vectors_elementwise(vector1, vector2):
    if len(vector1) != len(vector2):
        return "eror:vectors have different lenght"
    result = [v1 / v2 for v1, v2 in zip(vector1, vector2)]
    return "divide_vectors_elementwise: " + str(result)

def calculate_and_write_result(input_file, output_file, operation, vector1, vector2=None):
    vectors = read_vectors(input_file)
    result = ""

    if operation == "add":
        result = add_vectors(vector1, vector2)
    elif operation == "subtract":
        result = subtract_vectors(vector1, vector2)
    elif operation == "multiply_elementwise":
        result = multiply_vectors_elementwise(vector1, vector2)
    elif operation == "divide_elementwise":
        result = divide_vectors_elementwise(vector1, vector2)

    write_result(output_file, result)

if __name__ == "__main__":
    input_file = "vectors.txt"
    output_file = "results.txt"


    with open(input_file, 'r') as vectors_file:
        lines = vectors_file.readlines()

        vector1 = [float(coord) for coord in lines[0].strip().split()]
        vector2 = [float(coord) for coord in lines[1].strip().split()]

    calculate_and_write_result(input_file, output_file, "add", vector1, vector2)
    calculate_and_write_result(input_file, output_file, "subtract", vector1, vector2)
    calculate_and_write_result(input_file, output_file, "multiply_elementwise", vector1, vector2)
    calculate_and_write_result(input_file, output_file, "divide_elementwise", vector1, vector2)

