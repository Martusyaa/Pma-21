from Matrix import Matrix
from Vector import Vector


def matrix():
    matrix_obj_one = Matrix('files/matrix_one.txt')
    matrix_obj_two = Matrix('files/matrix_two.txt')

    print("----MATRIX----")
    print("matrix addition")
    for k in matrix_obj_one + matrix_obj_two:
        print(k)

    print("\nmatrix subtracting")
    for k in matrix_obj_one - matrix_obj_two:
        print(k)

    print("\nmatrix multiplication")
    for k in matrix_obj_one * matrix_obj_two:
        print(k)

    print("\nmatrix dividing")
    for k in matrix_obj_one / matrix_obj_two:
        print(k)


def vector():
    vector_obj_one = Vector('files/vector_one.txt')
    vector_obj_two = Vector('files/vector_two.txt')

    print("\n\n\n----VECTOR----")
    print("vector addition")
    print(vector_obj_one + vector_obj_two)

    print("\nvector subtracting")
    print(vector_obj_one - vector_obj_two)

    print("\nvector multiplication")
    print(vector_obj_one * vector_obj_two)

    print("\nvector dividing")
    print(vector_obj_one / vector_obj_two)


matrix()
vector()
