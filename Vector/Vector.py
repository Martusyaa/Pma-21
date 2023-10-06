from Validator import *

class Vector:
    def __init__(self, n=1):
        self.size = n
        self.vector = [0 for i in range(self.size)]

    def read(self, filename):
        with open(filename) as f:
            line = f.readlines()
            self.vector = []
            for i in line:
                items = i.split()
                for j in items:
                    self.vector.append(int(j))
            self.size = len(self.vector)

    @validator
    def add(self, a):
        result = Vector(self.size)
        for i in range(self.size):
            result.vector[i] = self.vector[i] + a.vector[i]
        return result

    @validator
    def substruct(self, a):
        result = Vector(self.size)
        for i in range(self.size):
            result.vector[i] = self.vector[i] - a.vector[i]
        return result
    
    def scalar(self,scalar):
        result = Vector(self.size)
        for i in range(self.size):
            result.vector[i] = self.vector[i] * scalar
        return result
    
    @validator
    def multiplication(self, a):
        result = Vector(self.size)
        for i in range(self.size):
            result.vector[i] = self.vector[i] * a.vector[i]
        return result

    @validator
    def division(self, a):
        result = Vector(self.size)
        for i in range(self.size):
            result.vector[i] = self.vector[i] / a.vector[i]
        return result

    def write(self, filename, result):
        with open(filename, "w") as f:
                f.write("Result: " + " ".join(map(str, result.vector)) + "\n")