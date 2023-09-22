FILE_READ_NAME = "file.txt"
FILE_INPUT_NAME = "file2.txt"

def fibonachi(list_of_fibonachi,n):
    for i in range(n):
        new_value = 0
        if i == 0 or i == 1:
            pass
        else:
            new_value_in_list_of_fibonachi = list_of_fibonachi[i-1]+list_of_fibonachi[i-2]
            list_of_fibonachi.append(new_value_in_list_of_fibonachi)

    with open(FILE_INPUT_NAME,"w") as file_input:
        for i in list_of_fibonachi:
            file_input.write(str(i)+"\n")
        file_input.close()


with open(FILE_READ_NAME) as file_read:
    data = file_read.read()

    file_read.close()
    list_of_start_numbers = [int(x) for x in data if x.isdigit()]

    list_of_fibonachi = [i for i in list_of_start_numbers]
    fibonachi(list_of_fibonachi,10)


