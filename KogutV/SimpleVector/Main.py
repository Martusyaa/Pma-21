from Vector import *
from Files import FIRST_VECTOR,SECOND_VECTOR,RESULT

vector_one = ReadVectorFromFile(FIRST_VECTOR)
vector_two = ReadVectorFromFile(SECOND_VECTOR)

addition_result = add(vector_one,vector_two)
write_vector_to_file(RESULT,addition_result)
