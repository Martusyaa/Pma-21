INPUT_VECTOR = "input_vector.txt"
OUTPUT_VECTOR = "output_vector.txt"
start_index = 0
def read_from_file():
    global start_index
    with open(INPUT_VECTOR, "r") as file:
        lines = file.readlines()


        data = lines[start_index].replace("\n","")
        file_vector = [int(x) for x in data.split(",") if x.isdigit()] #додає число до файл вектору
        start_index+=1
    return file_vector

def add_vector(vector1, vector2):
    for index in range(len(vector1)):
        vector1[index]+=vector2[index]

def subtract_vector(vector1, vector2):
    for index in range(len(vector1)):
        vector1[index]-=vector2[index]

def multyply_vector(vector1, vector2):
    for index in range(len(vector1)):
        vector1[index]*=vector2[index]

def divide_vector(vector1, vector2):
    for index in range(len(vector1)):
        vector1[index]/=vector2[index]

def write_in_file(vector):
    with open(OUTPUT_VECTOR, "a") as file:
       file.write(str(vector)+"\n")


a = read_from_file()
b = read_from_file()
print(a)
print(b)
add_vector(a,b)
write_in_file(a)
divide_vector(a,b)
write_in_file(a)