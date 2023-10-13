class Matrix:
    def __init__(self, data):
        self.data = data
        self.rows = len(data)
        self.cols = len(data[0])

    def __str__(self):
        return '\n'.join([' '.join(map(str, row)) for row in self.data])

    def __add__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("error")

        result_data = [[self.data[i][j] + other.data[i][j] for j in range(self.cols)] for i in range(self.rows)]
        return Matrix(result_data)

    def __sub__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("error")

        result_data = [[self.data[i][j] - other.data[i][j] for j in range(self.cols)] for i in range(self.rows)]
        return Matrix(result_data)

    def __mul__(self, other):
        if self.cols != other.rows:
            raise ValueError("error")

        result_data = [[sum(self.data[i][k] * other.data[k][j] for k in range(self.cols)) for j in range(other.cols)]
                       for i in range(self.rows)]
        return Matrix(result_data)

    def __truediv__(self, divisor):
        if divisor == 0:
            raise ZeroDivisionError("error")

        result_data = [[self.data[i][j] / divisor for j in range(self.cols)] for i in range(self.rows)]
        return Matrix(result_data)


def read_matrix(file_name):
    with open(file_name, 'r') as file:
        lines = file.readlines()
        matrix_data = [[float(num) for num in line.split()] for line in lines]
        return Matrix(matrix_data)

def write_matrix(matrix, file_name):
    with open(file_name, 'w') as file:
        file.write(str(matrix))

def main():
    try:
        fmatrix = read_matrix("matrixA.txt")
        smatrix = read_matrix("matrixB.txt")
        operations = ['+', '-', '*', '/']

        with open("output_results.txt", "w") as result_file:
            for operation in operations:
                result_file.write(f"Operation: {operation}\n")
                try:
                    if operation == '+':
                        result_matrix = fmatrix + smatrix
                    elif operation == '-':
                        result_matrix = fmatrix - smatrix
                    elif operation == '*':
                        result_matrix = fmatrix * smatrix
                    elif operation == '/':
                        divisor = 2
                        result_matrix = fmatrix / divisor

                    write_matrix(result_matrix, "output_results.txt")
                    result_file.write(str(result_matrix) + "\n")
                except Exception as e:
                    result_file.write(str(e) + "\n")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
