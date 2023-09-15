FILE_INPUT = "input.txt"
BREAK = "break.txt"
FILE_OUTPUT = "output.txt"

my_list_fibon = []
class Fibonacci:
    def __init__(self):
        self.list_fibon = []
        self.read_from_file()
        self.break_n = 0
        self.check_break()


    def read_from_file(self,start_counter=0):
        try:
            with open(FILE_INPUT, "r") as file:
                lines = file.readlines()
            data = lines[start_counter].replace("\n", "")
            vector = [int(x) for x in data.split(",") if x.isdigit()]
            for i in vector:
                self.list_fibon.append(i)
        except Exception as e:
            print("Error:", e)

    def check_break(self):
        with open(BREAK, "r") as file:
            data = file.readline().replace("\n", "")
            for x in data.split(","):
                if x.isdigit() == True:
                    self.break_n = int(x)

    def write_to_file(self):
        with open(FILE_OUTPUT, "a") as file:
            file.write("Result_From_Class:" + str(self.list_fibon) + "\n")

    def fibonacci(self,my_list_fibon):
        my_list_fibon.append(self.list_fibon[0])
        my_list_fibon.append(self.list_fibon[1])
        def calculating(self,my_list_fibon, last_value=0,):
            value = my_list_fibon[-1] + my_list_fibon[-2]
            if value > self.break_n:
                return
            my_list_fibon.append(value)
            return calculating(self,my_list_fibon=my_list_fibon,last_value=value)
        calculating(self,my_list_fibon,last_value=0)


    def print_fff(self):
        print(self.list_fibon)



f = Fibonacci()
f.fibonacci(my_list_fibon=my_list_fibon)
print(my_list_fibon)




