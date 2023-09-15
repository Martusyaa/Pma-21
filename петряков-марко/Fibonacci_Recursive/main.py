FILE_INPUT = "input.txt"
BREAK = "break.txt"
FILE_OUTPUT = "output.txt"






def read_from_file(start_counter=0):
    try:
        with open(FILE_INPUT,"r") as file:
            lines = file.readlines()
        data = lines[start_counter].replace("\n","")
        vector = [int(x) for x in data.split(",") if x.isdigit()]
        return vector
    except Exception as e:
        print("Error:",e)


def check_break():
    with open(BREAK,"r") as file:
        data=file.readline().replace("\n","")
        for x in data.split(","):
            if x.isdigit() == True:
                return x

def write_to_file(list):
    with open(FILE_OUTPUT, "a") as file:
        file.write("Result:" + str(list) + "\n")

def fibonacci(list_start):
    break_number = int(check_break())

    def calculating(list_start=list_start,last_value=0,break_number=break_number):
        value = list_start[-1] + list_start[-2]
        if value > break_number:
            return
        list_start.append(value)
        return calculating(list_start=list_start,last_value=value,break_number=break_number)
    calculating(list_start=list_start,break_number=break_number)
    return list_start

a = read_from_file()
result = fibonacci(list_start=a)
write_to_file(result)


