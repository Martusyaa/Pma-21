from vector import add_vectors, subtract_vectors, multiply_vectors, divide_vectors


def write_result(filename, result_add=None, result_sub=None, result_mul=None, result_div=None):
    with open(filename, "w") as f:
        if result_add is not None:
            f.write("Result of Addition: " + " ".join(map(str, result_add)) + "\n")
        if result_sub is not None:
            f.write("Result of Subtraction: " + " ".join(map(str, result_sub)) + "\n")
        if result_mul is not None:
            f.write("Result of Multiplication: " + str(result_mul) + "\n")
        if result_div is not None:
            f.write("Result of Division: " + " ".join(map(str, result_div)) + "\n")


def read_vector(filename):
    with open(filename, "r") as f:
        line = f.readline()
        vector = list(map(int, line.strip().split()))
        return vector


vector1 = read_vector("vector1.txt")
vector2 = read_vector("vector2.txt")
result_add = add_vectors(vector1, vector2)
result_sub = subtract_vectors(vector1, vector2)
result_mul = multiply_vectors(vector1, vector2)
result_div = divide_vectors(vector1, vector2)

write_result("result.txt", result_add, result_sub, result_mul, result_div)
