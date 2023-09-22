import os.path

class Vector:
    VECTOR_ERROR = "Вимірність векторів повинна бути однаковою"
    SEPARATOR = ','
    DEFAULT_VECTOR = [1, 1, 1]

    def __init__(self, vector_file):
        self.vector_file = vector_file
        self.vector = self._readVectorFromFile()


    def _readVectorFromFile(self):
        if not os.path.isfile(self.vector_file):
            return self.DEFAULT_VECTOR

        with open(self.vector_file) as file:
            line = file.readline().split(self.SEPARATOR)
        return [int(num) for num in line if num.isdigit()]


    def __add__(self, other):
        if len(self.vector) != len(other.vector):
            raise ValueError(self.VECTOR_ERROR)

        return [self.vector[i] + other.vector[i] for i in range(len(self.vector))]


    def __sub__(self, other):
        if len(self.vector) != len(other.vector):
            raise ValueError(self.VECTOR_ERROR)

        return [self.vector[i] - other.vector[i] for i in range(len(self.vector))]


    def __mul__(self, other):
        if len(self.vector) != len(other.vector):
            raise ValueError(self.VECTOR_ERROR)

        return sum([self.vector[i] * other.vector[i] for i in range(len(self.vector))])


    def __truediv__(self, other):
        if len(self.vector) != len(other.vector):
            raise ValueError(self.VECTOR_ERROR)

        if 0 in self.vector or 0 in other.vector:
            return self.DEFAULT_VECTOR

        return [self.vector[i] / other.vector[i] for i in range(len(self.vector))]
