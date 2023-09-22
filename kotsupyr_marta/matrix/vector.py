input_file = 'input.txt'
output_file = 'result.txt'

def add(firstvector, second_vector):
    return [x + y for x, y in zip(firstvector, second_vector)]
def subtract(firstvector, second_vector):
    return [x - y for x, y in zip(firstvector, second_vector)]
def multiply(firstvector, second_vector):
    return sum([x * y for x,y in zip(firstvector,second_vector)])
def divide(vector, scalar):
    return [x / scalar for x in vector]

with open(input_file, 'r') as input_file:
    lines = input_file.readlines()
    first_vector = [float(x) for x in lines[0].split()]
    second_vector = [float(x) for x in lines[1].split()]
result_add = add(first_vector, second_vector)
result_subtract = subtract(first_vector, second_vector)
result_mult = multiply(first_vector,second_vector)
result_divide = divide(second_vector, 2.0)
with open(output_file, 'w') as output_file:
    output_file.write("Додавання: {}\n".format(result_add))
    output_file.write("Віднімання: {}\n".format(result_subtract))
    output_file.write("Множення: {}\n".format(result_mult))
    output_file.write("Ділення: {}\n".format(result_divide))
