from Matrix import Matrix
from Vector import Vector


def matrix():
    matrix_obj_one = Matrix('files/matrix_one.txt')
    matrix_obj_two = Matrix('files/matrix_two.txt')


    with open("files/result.txt", "w") as result_file:
        result_file.write("mul result\n")
        for row in matrix_obj_one * matrix_obj_two:
            result_file.write(','.join(map(str, row)) + '\n')

        result_file.write("\ndiv result\n")
        if matrix_obj_one / matrix_obj_two == -1:
            result_file.write("Детермінант = 0")
        else:
            for row in matrix_obj_one / matrix_obj_two:
                result_file.write(','.join(map(str, row)) + '\n')


def vector():
    vector_obj_one = Vector('files/vector_one.txt')
    vector_obj_two = Vector('files/vector_two.txt')

    # print("\n\n\n----VECTOR----")
    # print("vector addition")
    # print(vector_obj_one + vector_obj_two)
    #
    # print("\nvector subtracting")
    # print(vector_obj_one - vector_obj_two)
    #
    # print("\nvector multiplication")
    # print(vector_obj_one * vector_obj_two)
    #
    # print("\nvector dividing")
    # print(vector_obj_one / vector_obj_two)


matrix()
vector()
