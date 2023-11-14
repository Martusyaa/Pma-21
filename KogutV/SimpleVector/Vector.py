from Files import SEPARATOR
from Validator import *

def ReadVectorFromFile(filename):
    with open(filename) as file:
        line = file.readline().split(SEPARATOR)
    return [int(num) for num in line]

@validator
def add(vector_one, vector_two):
    return [vector_one[i] + vector_two[i] for i in range(len(vector_one))]

@validator
def subtract(vector_one, vector_two):
    return [vector_one[i] - vector_two[i] for i in range(len(vector_one))]

@validator
def multiply(vector_one, vector_two):
    return [vector_one[i] * vector_two[i] for i in range(len(vector_one))]

@validator
def divide(vector_one, vector_two):
    return [vector_one[i] / vector_two[i] for i in range(len(vector_one))]

def write_vector_to_file(file_name, vector):
    with open(file_name, 'w') as file:
        file.write(' '.join(str(x) for x in vector))
