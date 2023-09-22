import random

class Vectors:
    def Create(self, elements):
        self.first_vector = [random.randint(1, 11) for i in range(elements)]
        self.second_vector = [random.randint(1, 11) for i in range(elements)]
        self.elements = elements
        # return self.vector
    def Print(self):
        print(f"First vector: {self.first_vector}")
        print(f"\nSecond vector: {self.first_vector}")
        print(f"\nSum: {self.sum}")
        print(f"\nSubtraction: {self.subtraction}")
        print(f"\nMultiplication: {self.multiplication}")

    def Sum(self):
        self.sum = [self.first_vector[i] + self.second_vector[i] for i in range(self.elements)]

    def Subtraction(self):
        self.subtraction = [self.first_vector[i] - self.second_vector[i] for i in range(self.elements)]

    def Multiplication(self):
        self.multiplication = 0
        for i in range(self.elements):
            self.multiplication += self.first_vector[i] * self.second_vector[i]

vec = Vectors()
elements = int(input('elements = '))
vec.Create(elements)
vec.Sum()
vec.Subtraction()
vec.Multiplication()
vec.Print()
