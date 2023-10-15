def retrieve_vector(file_name: str) -> list[int]:
    try:
        with open(file_name, 'r') as file:
            vector = [int(value) for value in file.read().split()]
        return vector
    except FileNotFoundError:
        print(f"File '{file_name}' not found.")
        return []
    except ValueError:
        print(f"Invalid data in file '{file_name}'. Please make sure the file contains only integers.")
        return []


def plus(first: list[int], second: list[int]) -> list[int]:
    return [int(round(first[i] + second[i])) for i in range(len(first))]


def minus(first: list[int], second: list[int]) -> list[int]:
    return [int(round(first[i] - second[i])) for i in range(len(first))]


def multiply(first: list[int], second: list[int]) -> list[int]:
    return [first[i] * second[i] for i in range(len(first))]


def divide(first: list[int], second: list[int]) -> list[int]:
    result = []
    for i in range(len(first)):
        if second[i] == 0:
            print("Division by zero encountered.")
            result.append(0)
        else:
            result.append(int(round(first[i] / second[i])))
    return result

FIRST_VECTOR = 'first_vector.txt'
SECOND_VECTOR = 'second_vector.txt'

first_vector = retrieve_vector(FIRST_VECTOR)
second_vector = retrieve_vector(SECOND_VECTOR)

if first_vector and second_vector:
    print("Multiplication:", multiply(first_vector, second_vector))
    print("Addition:", plus(first_vector, second_vector))
    print("Division:", divide(first_vector, second_vector))
    print("Subtraction:", minus(first_vector, second_vector))