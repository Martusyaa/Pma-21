class Vector:
    def __init__(self, array: list):
        self.array = array

    @classmethod
    def from_file(cls, file_name: str):
        try:
            with open(file_name) as file:
                array = [int(value) for value in file.read().split()]
            return cls(array)
        except FileNotFoundError:
            print(f"File '{file_name}' not found.")
            return None
        except ValueError:
            print(f"Invalid data in file '{file_name}'. Please make sure the file contains only integers.")
            return None

    def plus(self, other) -> list[int]:
        return [int(round(self.array[i] + other.array[i])) for i in range(len(self.array))]

    def add(self, other):
        return self.plus(other)

    @classmethod
    def static_add(cls, vector, other):
        return Vector([int(round(vector.array[i] + other.array[i])) for i in range(len(vector.array))])

    def minus(self, other) -> list[int]:
        return [int(round(self.array[i] - other.array[i])) for i in range(len(self.array))]

    def subtract(self, other):
        return self.minus(other)

    @classmethod
    def static_sub(cls, vector, other):
        return Vector([int(round(vector.array[i] - other.array[i])) for i in range(len(vector.array))])

    def multiply(self, other) -> list[int]:
        return [int(round(self.array[i] * other.array[i])) for i in range(len(self.array))]

    @classmethod
    def static_mul(cls, vector, other):
        return Vector([int(round(vector.array[i] * other.array[i])) for i in range(len(vector.array))])

    def divide(self, other) -> list[int]:
        result = []
        for i in range(len(self.array)):
            if other.array[i] == 0:
                print("Division by zero encountered.")
                result.append(0)
            else:
                result.append(int(round(self.array[i] / other.array[i])))
        return result

    @classmethod
    def static_div(cls, vector, other):
        result = []
        for i in range(len(vector.array)):
            if other.array[i] == 0:
                print("Division by zero encountered.")
                result.append(0)
            else:
                result.append(int(round(vector.array[i] / other.array[i])))
        return Vector(result)

    def __str__(self):
        return str(self.array)

if __name__ == "__main__":
    first_vector = Vector.from_file('first_vector.txt')
    second_vector = Vector.from_file('second_vector.txt')

    if first_vector and second_vector:
        print("Vector 1:", first_vector)
        print("Vector 2:", second_vector)

        result_addition = first_vector.add(second_vector)
        print("\nAddition:", result_addition)

        result_subtraction = first_vector.subtract(second_vector)
        print("Subtraction:", result_subtraction)

        result_multiplication = first_vector.multiply(second_vector)
        print("Multiplication:", result_multiplication)

        result_division = first_vector.divide(second_vector)
        print("Division:", result_division)