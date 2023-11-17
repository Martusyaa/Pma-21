from Vector import Vector

if __name__ == "__main__":
    input_file = "input.txt"
    output_add = "output_add.txt"
    output_sub = "output_subtract.txt"
    output_mul = "output_multiply.txt"
    output_div = "output_divide.txt"

    vectors = Vector.read_from_file(input_file)

    result_sum = vectors[0]
    result_diff = vectors[0]
    result_mul = vectors[0]
    result_div = vectors[0]

    for vector in vectors[1:]:
        try:
            result_sum += vector
            result_diff -= vector
            result_mul *= vector
            result_div /= vector
        except:
            print("Vector 2 is zero")


    result_sum.write_to_file(output_add)
    result_diff.write_to_file(output_sub)
    result_mul.write_to_file(output_mul)
    result_div.write_to_file(output_div)


    try:
        with open("output.txt", 'w') as output_file:
            output_file.write("Suma: {}\n".format(result_sum))
            output_file.write("Dif: {}\n".format(result_diff))
            output_file.write("Mulp: {}\n".format(result_mul))
            output_file.write("Div: {}\n".format(result_div))
    except:
        print("File is not found", "output.txt")

    print("Результати обчислень записані у відповідні файли.")
