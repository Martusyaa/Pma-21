INPUT_TXT = "input.txt"
OUTPUT_TXT = "output.txt"
OUTPUTT_TXT = "outputt.txt"
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
    ValueError("different len")
  sum_vector = []
  for i in range(len(vector1)):
    sum_vector.append(vector1[i] + vector2[i])
  return sum_vector

def vector_subtraction(vector1, vector2):
  if len(vector1) != len(vector2):
    ValueError("different len")
  subtraction_vector = []
  for i in range(len(vector1)):
    subtraction_vector.append(vector1[i] - vector2[i])
  return subtraction_vector

def vector_multiplication(vector1, vector2):
  if len(vector1) != len(vector2):
    ValueError("different")
  multiplication_vector = []
  for i in range(len(vector1)):
    multiplication_vector.append(vector1[i] * vector2[i])
  return multiplication_vector

def vector_division(vector1, vector2):
  if len(vector1) != len(vector2):
    ValueError("different len")
  division_vector = []
  try:
    for i in range(len(vector1)):
      division_vector.append(vector1[i] / vector2[i])
    return division_vector
  except ZeroDivisionError:
    print("Division by zero")

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

#except NameError:
    #print("Vector1,2 not definded: ", INPUT_TXT)
"""
def write_in_file(vector3):
  with open(OUTPUTT_TXT, 'a') as file:
    vector3_str = ""
    for num in vector3:
      vector3_str += str(num) + "\t \t"
    vector3_str = vector3_str.strip()
    file.write(vector3_str)
    file.write('\n')

def write_in_file(vector3):
  with open(OUTPUT_TXT, 'w') as file:
    vector3_str = ""
    for num in vector3:
      vector3_str += str(num) + "\t \t"
    vector3_str = vector3_str.strip()
    file.write(vector3_str)

vector3 = vector_addition(vector1, vector2)
write_in_file(vector3)

vector4 = vector_subtraction(vector1, vector2)
write_in_file(vector4)

vector5 = vector_multiplication(vector1, vector2)
write_in_file(vector5)

vector6 = vector_division(vector1, vector2)
write_in_file(vector6)"""


'''vector1 = [1,4,2,6]
vector2 = [1,5,6,3]
vector3 = []
matrix_length = len(vector1)
for i in range(len(vector1)):
  vector3[i] = vector1[i] + vector2[i]
  print ("The sum of Matrix M1 and M2 = ", vector3) '''


"""def vector_addition(vector1, vector2):
  # Check if the vectors have the same length
  if len(vector1) != len(vector2):
    raise ValueError("Vectors have different lengths")

  # Initialize the result as an empty vector
  result = []

  # Add each element of vector1 to the corresponding element of vector2
  for i in range(len(vector1)):
    sum_value = vector1[i] + vector2[i]
    result.append(sum_value)

  return result


def vector_subtraction(vector1, vector2):
  # Check if the vectors have the same length
  if len(vector1) != len(vector2):
    raise ValueError("Vectors have different lengths")

  # Initialize the result as an empty vector
  result = []

  # Subtract each element of vector2 from the corresponding element of vector1
  for i in range(len(vector1)):
    difference = vector1[i] - vector2[i]
    result.append(difference)

  return result

def vector_multiplication (vector1, vector2):
    # Check if the vectors have the same length
    if len(vector1) != len(vector2):
      raise ValueError("Vectors have different lengths")

    # Initialize the result as an empty vector
    result = []

    # Add each element of vector1 to the corresponding element of vector2
    for i in range(len(vector1)):
      product_value = vector1[i] * vector2[i]
      result.append(product_value)

    return result


def vector_division(vector1, vector2):
  # Check if the vectors have the same length
  if len(vector1) != len(vector2):
    raise ValueError("Vectors have different lengths")

  # Initialize the result as an empty vector
  result = []

  # Subtract each element of vector2 from the corresponding element of vector1
  for i in range(len(vector1)):
    quotient = vector1[i] / vector2[i]
    result.append(quotient)

  return result



# Example usage of the functions
vector1 = [4, 6, 8]
vector2 = [2, 2, 4]

# Addition
sum_of_vectors = vector_addition(vector1, vector2)
print("Sum of vectors:", sum_of_vectors)

# Subtraction
difference_of_vectors = vector_subtraction(vector1, vector2)
print("Difference of vectors:", difference_of_vectors)

# Multiplication
product_of_vectors = vector_multiplication(vector1, vector2)
print("Product of vectors:", product_of_vectors)

# Division
quotient_of_vectors = vector_subtraction(vector1, vector2)
print("Quotient of vectors:", quotient_of_vectors)
"""
