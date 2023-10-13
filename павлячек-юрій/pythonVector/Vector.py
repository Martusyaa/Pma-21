class Vector:
    def __init__(self, values):
        self.values = values

    def __str__(self):
        return str(self.values)

    def __add__(self, other):
        if len(self.values) != len(other.values):
            raise ValueError("Vectors must be the same size.")
        result_values = [a + b for a, b in zip(self.values, other.values)]
        return Vector(result_values)

    def __sub__(self, other):
        if len(self.values) != len(other.values):
            raise ValueError("Vectors must be the same size.")
        result_values = [a - b for a, b in zip(self.values, other.values)]
        return Vector(result_values)

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            result_values = [a * other for a in self.values]
            return Vector(result_values)
        elif isinstance(other, Vector):
            if len(self.values) != len(other.values):
                raise ValueError("Vectors must be the same size.")
            result_values = [a * b for a, b in zip(self.values, other.values)]
            return Vector(result_values)
        else:
            raise TypeError("Error !")

    def __truediv__(self, other):

        if isinstance(other, (int, float)):
            result_values = [a / other for a in self.values]
            return Vector(result_values)
        elif isinstance(other, Vector):
            if len(self.values) != len(other.values):
                raise ValueError("Vectors must be the same size.")
            result_values = [a / b for a, b in zip(self.values, other.values)]
            return Vector(result_values)
        else:
            raise TypeError("Error !")

    @classmethod
    def read_from_file(cls, file_path):
        vectors = []
        try:
            with open(file_path) as file:
                for line in file:
                    values = [int(i) for i in line.strip().split()]
                    vector = cls(values)
                    vectors.append(vector)
            return vectors
        except:
            print("File is not found", file_path)

    def write_to_file(self, file_path):
        try:
            with open(file_path, 'w') as file:
                file.write(' '.join(map(str, self.values)))
        except:
            print("File is not found", file_path)