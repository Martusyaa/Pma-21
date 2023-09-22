VECTOR_ERROR = "Вимірність векторів повинна бути однаковою"
VECTOR_ONE_FILE = "vector_one.txt"
VECTOR_TWO_FILE = "vector_two.txt"
SEPARATOR = ','

def readFirstVectorFromFile():
    with open(VECTOR_ONE_FILE) as file:
        line = file.readline().split(SEPARATOR)
    return [int(num) for num in line]


def readSecondVectorFromFile():
    with open(VECTOR_TWO_FILE) as file:
        line = file.readline().split(SEPARATOR)
    return [int(num) for num in line]


def add(vector_one, vector_two):
    if len(vector_one) != len(vector_two):
        raise ValueError(VECTOR_ERROR)

    return [vector_one[i] + vector_two[i] for i in range(len(vector_one))]


def subtract(vector_one, vector_two):
    if len(vector_one) != len(vector_two):
        raise ValueError(VECTOR_ERROR)

    return [vector_one[i] - vector_two[i] for i in range(len(vector_one))]


def multiply(vector_one, vector_two):
    if len(vector_one) != len(vector_two):
        raise ValueError(VECTOR_ERROR)

    return sum([vector_one[i] * vector_two[i] for i in range(len(vector_one))])


def divide(vector_one, vector_two):
    if len(vector_one) != len(vector_two):
        raise ValueError(VECTOR_ERROR)

    return [vector_one[i] / vector_two[i] for i in range(len(vector_one))]


def main():
    vector_one = readFirstVectorFromFile()
    vector_two = readSecondVectorFromFile()

    print("vector addition")
    print(add(vector_one, vector_two))

    print("\nvector subtracting")
    print(subtract(vector_one, vector_two))

    print("\nvector multiplication")
    print(multiply(vector_one, vector_two))

    print("\nvector dividing")
    print(divide(vector_one, vector_two))


main()
