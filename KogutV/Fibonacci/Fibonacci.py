def fibonacci(n, a, b):
    yield a
    yield b
    for _ in range(n - 2):
        a, b = b, a + b
        yield b

def read_from_file(filename):
    with open(filename) as file:
        return int(file.readline())

def write_to_file(filename, data):
    with open(filename, 'w') as file:
        for number in data:
            file.write(f"{number}\n")

s = read_from_file("steps.txt")

try:
    with open("input.txt") as input_file:
        start_numbers = input_file.readline().split()
except FileNotFoundError:
    print("file does not exist")
    
fibonacci_series = fibonacci(s, int(start_numbers[0]), int(start_numbers[1]))

write_to_file("result.txt", fibonacci_series)
