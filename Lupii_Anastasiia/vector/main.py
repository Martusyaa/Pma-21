
def perform_vector_operations(file_first, file_second):
    try:
     with open(file_first, "r") as first_file, open(file_second, "r") as second_file:
        vector_first = [int(x) for x in first_file.readline().split()]
        vector_second = [int(x) for x in second_file.readline().split()]
     if len(vector_first) != len(vector_second):
         raise ValueError("Vectors have different lengths")

     summed_vectors = []
     difference_vectors = []
     product_vectors = []
     division_vectors = []

     for i in range(len(vector_first)):
        sum_result = vector_first[i] + vector_second[i]
        difference_result = vector_first[i] - vector_second[i]
        product_result = vector_first[i] * vector_second[i]
        division_result = vector_first[i] / vector_second[i]

        summed_vectors.append(sum_result)
        difference_vectors.append(difference_result)
        product_vectors.append(product_result)
        division_vectors.append(division_result)

     with open("results.txt", 'a') as file:
        print(f"{vector_first} + {vector_second} = {summed_vectors}", file=file)
        print(f"{vector_first} - {vector_second} = {difference_vectors}", file=file)
        print(f"{vector_first} * {vector_second} = {product_vectors}", file=file)
        print(f"{vector_first} / {vector_second} = {division_vectors}", file=file)

    except ValueError as e:
          print(f"Error: {e}")
file_first = "vector_first.txt"
file_second = "vector_second.txt"

perform_vector_operations(file_first, file_second)
