from classVector import Vector

vector_first = Vector('vector_first.txt')
vector_second = Vector('vector_second.txt')

suma_vector = vector_first.sum(vector_second)
difference_vector = vector_first.difference(vector_second)
multiplication_vector = vector_first.multiplication(vector_second)
division_vector = vector_first.division(vector_second)

vector_first.write_file(suma_vector)
vector_first.write_file(difference_vector)
vector_first.write_file(multiplication_vector)
vector_first.write_file(division_vector)