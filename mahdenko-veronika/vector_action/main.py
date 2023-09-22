def print_vector(vector):
    print(vector)


def add_vector(vector1, vector2):
    if len(vector1) != len(vector2):
        raise ValueError("Довжина векторів повинна бути однаковою для додавання.")
    else:
        result_vector = [x + y for x, y in zip(vector1, vector2)]
        return result_vector


def subtraction_vector(vector1, vector2):
    if len(vector1) != len(vector2):
        raise ValueError("Довжина векторів повинна бути однаковою для віднімання.")
    else:
        result_vector = [x - y for x, y in zip(vector1, vector2)]
        return result_vector


def multiplication_vector(vector1, vector2):
    if len(vector1) != len(vector2):
        raise ValueError("Довжина векторів повинна бути однаковою для множення.")
    else:
        result_vector = sum(x * y for x, y in zip(vector1, vector2))
        return result_vector


def division_vector(vector1, vector2):
    result_divide = []
    if len(vector1) != len(vector2):
        raise ValueError("Довжина векторів повинна бути однаковою для ділення.")
    else:
        result_divide = [x / y for x, y in zip(vector1, vector2)]
        for i in range(len(result_divide)):
            result_divide[i] = round(result_divide[i], 2)
    return result_divide


def read_matrix_from_file(filename):
    with open(filename, 'r') as file:
        vector = file.readline().split()
        vector = [float(i) for i in vector]
    return vector


def write_vector_to_file(vector, filename, action):
    with open(filename, 'a+') as file:
        file.write(f"Result of {action}: \n")
        vector_str = ', '.join(map(str, vector))
        file.write(vector_str + '\n')
        file.write("\n")


# def clear_file(filename):
#     with open(filename, 'w') as file:
#         file.write('')


if __name__ == '__main__':

     result_file = "result.txt"

     try:
        vector1 = read_matrix_from_file("Vector1.txt")
        vector2 = read_matrix_from_file("Vector2.txt")

        # clear_file(result_file)

        try:
           add_result = add_vector(vector1, vector2)
           print("Результат додавання: ")
           print_vector(add_result)
           write_vector_to_file(add_result, result_file, "addition")
        except ValueError as e:
           print(e)

        try:
          subtraction_result = subtraction_vector(vector1, vector2)
          print("Результат віднімання: ")
          print_vector(subtraction_result)
          write_vector_to_file(subtraction_result, result_file, "subtraction")
        except ValueError as e:
           print(e)

        try:
           multiplication_result = multiplication_vector(vector1, vector2)
           print("Результат множення: ")
           print_vector(multiplication_result)
           with open(result_file, 'a+') as file:
               file.write(f"Result of multiplication: {multiplication_result}\n")
        except ValueError as e:
            print(e)

        try:
           division_result = division_vector(vector1, vector2)
           print("Результат ділення: ")
           print_vector(division_result)
           write_vector_to_file(division_result, result_file, "division")
        except ValueError as e:
            print(e)

     except FileNotFoundError as e:
            print(f"File {result_file} doesn't exist!")
     except Exception as e:
            print(f"Something went wrong: {e}")