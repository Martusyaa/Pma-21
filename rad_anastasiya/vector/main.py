def retrieve_vector(file_name: str) -> []:
    with open(file_name) as file:
        vector = file.read().split()
        for i in range(0, len(vector)):
            vector[i] = float(vector[i])
    return vector


def plus(first: [], second: []) -> []:
    return [first[i] + second[i] for i in range(0, len(first))]


def minus(first: [], second: []) -> []:
    return [first[i] - second[i] for i in range(0, len(first))]


def multiple(first: [], second: []) -> []:
    return [first[i] * second[i] for i in range(0, len(first))]


def divide(first: [], second: []) -> []:
    return [first[i] / second[i] for i in range(0, len(first))]


FIRST_VECTOR = 'first_vector.txt'
SECOND_VECTOR = 'second_vector.txt'

first_vector = retrieve_vector(FIRST_VECTOR)
second_vector = retrieve_vector(SECOND_VECTOR)
print(multiple(first_vector, second_vector))
print(plus(first_vector, second_vector))
print(divide(first_vector, second_vector))
print(minus(first_vector, second_vector))
