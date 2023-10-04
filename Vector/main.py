from Vector import *
from Files import *

first_vector = Vector()
second_vector = Vector()
first_vector.read(FIRST_VECTOR)
second_vector.read(SECOND_VECTOR)
summary_result = first_vector.multiplication(second_vector)
first_vector.write(RESULT, summary_result)