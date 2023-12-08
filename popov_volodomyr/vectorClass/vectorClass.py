import json

class VectorOperations:
    def __init__(self, input_file, output_file):
        self.INPUT_FILE = input_file
        self.OUTPUT_FILE = output_file
        self.firstVector = []
        self.secondVector = []

    def read_vectors(self):
        with open(self.INPUT_FILE, "r") as file:
            lines = json.load(file)
            self.firstVector = lines[0]
            self.secondVector = lines[1]

    def save_file(self, vector):
        with open(self.OUTPUT_FILE, "a") as file:
            file.write(str(vector) + "\n")

    def vector_add(self):
        return [(self.firstVector[i] + self.secondVector[i]) for i in range(3)]

    def vector_subtract(self):
        return [(self.firstVector[i] - self.secondVector[i]) for i in range(3)]

    def vector_multiply(self):
        return [(self.firstVector[i] * self.secondVector[i]) for i in range(3)]

    def vector_divide(self):
        return [(self.firstVector[i] / self.secondVector[i]) for i in range(3)]

    def perform_operations(self):
        self.read_vectors()
        self.save_file(self.vector_add())
        self.save_file(self.vector_subtract())
        self.save_file(self.vector_divide())
        self.save_file(self.vector_multiply())
calculator = VectorOperations("input.json", "output.txt")
calculator.perform_operations()
