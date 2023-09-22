INPUT_TXT = "input.txt"
OUTPUT_TXT = "output.txt"
try:
    with open(INPUT_TXT, 'r') as file:
      vector1 = file.readline().split()
      vector2 = file.readline().split()

except FileNotFoundError:
    print("File not found: ", INPUT_TXT)

print(vector1)
print(vector2)

vector1 = [float(x) for x in vector1]
vector2 = [float(x) for x in vector2]

def vector_addition(vector1, vector2):
  if len(vector1) != len(vector2):
    ValueError("Very bed")
  sum_vector = []
  for i in range(len(vector1)):
    sum_vector.append(vector1[i] + vector2[i])
  return sum_vector

def vector_subtraction(vector1, vector2):
  if len(vector1) != len(vector2):
    ValueError("Very bed")
  subtraction_vector = []
  for i in range(len(vector1)):
    subtraction_vector.append(vector1[i] - vector2[i])
  return subtraction_vector

def vector_multiplication(vector1, vector2):
  if len(vector1) != len(vector2):
    ValueError("Very bed")
  multiplication_vector = []
  for i in range(len(vector1)):
    multiplication_vector.append(vector1[i] * vector2[i])
  return multiplication_vector

def vector_division(vector1, vector2):
  if len(vector1) != len(vector2):
    ValueError("Very bed")
  division_vector = []
  for i in range(len(vector1)):
    division_vector.append(vector1[i] / vector2[i])
  return division_vector

vector3 = vector_addition(vector1, vector2)

vector4 = vector_subtraction(vector1, vector2)

vector5 = vector_multiplication(vector1, vector2)

vector6 = vector_division(vector1, vector2)
with open(OUTPUT_TXT, 'w') as file:
  print(f"{vector1} + {vector2} = {vector3}", file=file)
  print(f"{vector1} - {vector2} = {vector4}", file=file)
  print(f"{vector1} * {vector2} = {vector5}", file=file)
  print(f"{vector1} / {vector2} = {vector6}", file=file)
  file.write('\n')

# def write_in_file(vector3):
#   with open(OUTPUT_TXT, 'a') as file:
#     print(vector3, file = file)
#     file.write('\n')
#
# vector3 = vector_addition(vector1, vector2)
# write_in_file(vector3)
#
# vector4 = vector_subtraction(vector1, vector2)
# write_in_file(vector4)
#
# vector5 = vector_multiplication(vector1, vector2)
# write_in_file(vector5)
#
# vector6 = vector_division(vector1, vector2)
# write_in_file(vector6)