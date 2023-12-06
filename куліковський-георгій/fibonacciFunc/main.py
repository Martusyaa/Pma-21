class BaseListError(Exception):
    "Base list error"
    

class ReadingModeError(Exception):
    "Wrong mode error"


def fibonacci(base_list:list, steps:int):
    if len(base_list) != 2:
        raise BaseListError
    result_list = [*base_list,]
    val_one = base_list[0]
    val_two = base_list[1]
    for i in range(steps-2):
        temp = val_two
        val_two = val_one + val_two
        result_list.append(val_two)
        val_one = temp
    return result_list


def read(path:str, mode:str):
    if mode == "steps":
        with open(path, "r") as file: 
            return int(file.read())
    elif mode == "numbers":
        with open(path, "r") as file:
            return list(map(float, file.read().split()))
    else:
        raise ReadingModeError
        
        
def write(path:str, array:list):
    with open(path, "a") as file:
        file.write(str(array)+"\n")
        
        
write("fibonacciFunc/output.txt", fibonacci(read("fibonacciFunc/input.txt", "numbers"), \
steps=read("fibonacciFunc/steps.txt", "steps")))