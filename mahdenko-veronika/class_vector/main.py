from Vector import Vector


# def clear_file(filename):
#     with open(filename, 'w') as file:
#         file.write('')


if __name__ == '__main__':
    result_file = "Result.txt"
    # clear_file(result_file)

try:
    vectorFirst = Vector.read_vector_from_file("VectorFirst.txt")
    vectorSecond = Vector.read_vector_from_file("VectorSecond.txt")

    try:
        print("Додавання векторів: ")
        add_result = vectorFirst.add_vector(vectorSecond)
        add_result.print_vector()
        add_result.write_vector_to_file(result_file, "addition")
    except ValueError as e:
        print(e)

    try:
        print("Віднімання векторів: ")
        difference_result = vectorFirst.difference_vector(vectorSecond)
        difference_result.print_vector()
        difference_result.write_vector_to_file(result_file, "difference")
    except ValueError as e:
        print(e)

    try:
        print("Множення векторів: ")
        multiplication_result = vectorFirst.multiplication_vector(vectorSecond)
        multiplication_result.print_vector()
        multiplication_result.write_vector_to_file(result_file, "multiplication")
    except ValueError as e:
        print(e)

    try:
        print("Ділення векторів: ")
        division_result = vectorFirst.division_vector(vectorSecond)
        division_result.print_vector()
        division_result.write_vector_to_file(result_file, "division")
    except ValueError as e:
        print(e)

except FileNotFoundError as e:
        print(f"Файл {result_file} не знайдено!")
except Exception as e:
        print(f"Щось не так: {e}")