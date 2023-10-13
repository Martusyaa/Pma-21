with open('input.txt', 'r') as file :

    vector1 = list(map(float, file.readline().split()))
    vector2 = list(map(float, file.readline().split()))


if len(vector1) != len(vector2):
    print("Вектори мають різну довжину і не можуть бути просумовані.")
else:
    # Обчислення суми векторів
    sum_vector = [vector1[i] + vector2[i] for i in range(len(vector1))]

   with open('output.txt', 'w') as output_file :
   output_file.write("sum_vector".format(sum_vector))