class Vector:

    FILE_NOT_FOUND = "File not found"
    SIZE_VECTOR_ERROR = "Вектори повинні мати однакову довжину"
    ZERO_DIVISION_ERROR = "Не можна ділити на нуль"
    SEPARATOR = ", "
    FILE_VECTOR_IS_EMPTY = "У файлі пустий вектор"
    NEWLINE = '\n'
    OUTPUT_FILE = "output.txt"

    def __init__(self, filename):
        self.filename = filename
        self.values = self.read_file()

    def read_file(self):
        try:
            with open(self.filename) as file:
                lines = file.readlines()
                if lines:
                    values = [float(i) for i in lines[0].split(Vector.SEPARATOR)]
                    return values
                else:
                    raise ValueError(Vector.FILE_VECTOR_IS_EMPTY)
        except FileNotFoundError:
            raise Exception(Vector.FILE_NOT_FOUND)

    def sum(self, other):
        if len(self.values) == len(other.values):
            result = [x + y for x, y in zip(self.values, other.values)]
            return result
        else:
            raise ValueError(Vector.SIZE_VECTOR_ERROR)

    def difference(self, other):
        if len(self.values) == len(other.values):
            result = [x - y for x, y in zip(self.values, other.values)]
            return result
        else:
            raise ValueError(Vector.SIZE_VECTOR_ERROR)

    def multiplication(self, other):
        if len(self.values) == len(other.values):
            result = [x * y for x, y in zip(self.values, other.values)]
            return result
        else:
            raise ValueError(Vector.SIZE_VECTOR_ERROR)

    def division(self, other):
        try:
            if len(self.values) == len(other.values):
                result = [x / y for x, y in zip(self.values, other.values)]
                return result
            else:
                raise ValueError(Vector.SIZE_VECTOR_ERROR)
        except ZeroDivisionError:
            print(Vector.ZERO_DIVISION_ERROR)

    def write_file(self, result_vector):
        try:
            with open(Vector.OUTPUT_FILE, "a") as file:
                if result_vector is not None:
                    file.write(" ".join(map(str, result_vector)) + Vector.NEWLINE)
        except FileNotFoundError:
            print(FILE_NOT_FOUND)