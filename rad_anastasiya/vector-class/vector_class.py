from constants import VALUE_ERROR


class Vector:
    def __init__(self, base=[]):
        try:
            self.array = base
        except ValueError:
            print(VALUE_ERROR)

    def __add__(self, other):
        self.length_check(other)
        return Vector([self.array[i] + other.array[i] for i in range(0, self.length())])

    def __sub__(self, other):
        self.length_check(other)
        return Vector([self.array[i] - other.array[i] for i in range(0, self.length())])

    def __mul__(self, other):
        self.length_check(other)
        return Vector([self.array[i] * other.array[i] for i in range(0, self.length())])

    def __truediv__(self, other):
        self.length_check(other)
        return Vector([self.array[i] / other.array[i] for i in range(0, self.length())])

    @classmethod
    def static_add(cls, vector, other):
        return vector + other

    @classmethod
    def static_sub(cls, vector, other):
        return vector - other

    @classmethod
    def static_mul(cls, vector, other):
        return vector * other

    @classmethod
    def static_div(cls, vector, other):
        return vector / other

    @classmethod
    def read_from_file(cls, filename: str):
        with open(filename) as file:
            content = file.read().split()
        return Vector([float(i) for i in content if i.isdigit()])

    def length_check(self, other):
        if self.length() != other.length():
            raise Exception()

    def length(self):
        return len(self.array)

    def __str__(self):
        return str(self.array)
