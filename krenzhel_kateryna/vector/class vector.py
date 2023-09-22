import random

INPUT_FILE_NAME = "input.txt"
OUTPUT_FILE_NAME = "output.txt"
FILE_NOT_FOUND = "File not found"
NOT_DIVISION = "Division imposible."
class Vectors:
    def __init__(self):
        try:
            with open(INPUT_FILE_NAME, 'r') as file:
                self.first_vector = [int(i) for i in file.readline().split()]
                self.second_vector = [int(i) for i in file.readline().split()]
        except FileNotFoundError:
            print(FILE_NOT_FOUND, INPUT_FILE_NAME)
            self.first_vector = [random.randint(1, 11) for j in range(3)]
            self.second_vector = [random.randint(1, 11) for j in range(3)]

        self.sum_vector = self.sum()
        self.subtraction_vector = self.subtraction()
        self.multiplication_vector = self.multiplication()
        self.division_vector = self.division()

    def print(self):
        print(f"First vector: {self.first_vector}")
        print(f"\nSecond vector: {self.second_vector}")
        print(f"\nSum: {self.sum_vector}")
        print(f"\nSubtraction: {self.subtraction_vector}")
        print(f"\nMultiplication: {self.multiplication_vector}")
        print(f"\nDivision: {self.division_vector}")
        with open(OUTPUT_FILE_NAME, 'w') as file:
            print(f"{self.first_vector} + {self.second_vector} = {self.sum_vector}", file=file)
            print(f"{self.first_vector} - {self.second_vector} = {self.subtraction_vector}", file=file)
            print(f"{self.first_vector} * {self.second_vector} = {self.multiplication_vector}", file=file)
            print(f"{self.first_vector} / {self.second_vector} = {self.division_vector}", file=file)

    def sum(self):
        sum = [self.first_vector[i] + self.second_vector[i] for i in range(len(self.first_vector))]
        return sum

    def subtraction(self):
        subtraction = [self.first_vector[i] - self.second_vector[i] for i in range(len(self.first_vector))]
        return subtraction

    def multiplication(self):
        multiplication = [self.first_vector[i] * self.second_vector[i] for i in range(len(self.first_vector))]
        return multiplication

    def division(self):
        try:
            division = [self.first_vector[i]/self.second_vector[i] for i in range(len(self.first_vector))]
        except ZeroDivisionError:
            division = NOT_DIVISION
        return division

vec = Vectors()
vec.print()
