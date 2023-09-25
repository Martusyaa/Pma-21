input_file = 'input.txt'
output_file = 'result.txt'

def add(firstvector, vector2):
    return [x + y for x, y in zip(firstvector, vector2)]
def subtract(firstvector, vector2):
    return [x - y for x, y in zip(firstvector, vector2)]
def multiply(firstvector, vector2):
    return sum([x * y for x,y in zip(firstvector,vector2)])
def divide(vector, scalar):
    return [x / scalar for x in vector]

with open(input_file, 'r') as input_file:
    lines = input_file.readlines()
    first_vector = [float(x) for x in lines[0].split()]
    vector2 = [float(x) for x in lines[1].split()]
result_add = add(first_vector, vector2)
result_subtract = subtract(first_vector, vector2)
result_mult = multiply(first_vector,vector2)
result_divide = divide(vector2, 2.0)
with open(output_file, 'w') as output_file:
    output_file.write("Додавання: {}\n".format(result_add))
    output_file.write("Віднімання: {}\n".format(result_subtract))
    output_file.write("Множення: {}\n".format(result_mult))
    output_file.write("Ділення: {}\n".format(result_divide))
