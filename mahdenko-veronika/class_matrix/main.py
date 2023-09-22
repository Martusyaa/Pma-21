from matrix import Matrix

if __name__ == '__main__':
    result_file="Result.txt"

try:
    mat1 = Matrix.read_matrix_from_file("MatrixFirst.txt")
    mat2 = Matrix.read_matrix_from_file("MatrixSecond.txt")

    try:
        print("Додавання матриць: ")
        add_result = mat1.add_matrix(mat2)
        add_result.print_matrix()
        add_result.write_matrix_to_file(result_file, "additional")
    except ValueError as e:
        print(e)

    try:
        print("Віднімання матриць: ")
        difference_result = mat1.difference_matrix(mat2)
        difference_result.print_matrix()
        difference_result.write_matrix_to_file(result_file, "difference")
    except ValueError as e:
        print(e)

    try:
        print("Множення матриць: ")
        multiplication_result = mat1.multiplication_matrix(mat2)
        multiplication_result.print_matrix()
        multiplication_result.write_matrix_to_file(result_file, "multiplication")
    except ValueError as e:
        print(e)

    try:
        print("Ділення матриць: ")
        division_result = mat1.divide_matrix(mat2)
        division_result.print_matrix()
        division_result.write_matrix_to_file(result_file, "division")
    except ValueError as e:
        print(e)

except FileNotFoundError as e:
        print(f"Файл {result_file} не знайдено!")
except Exception as e:
        print(f"Щось не так: {e}")