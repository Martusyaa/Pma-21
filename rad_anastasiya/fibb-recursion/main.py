from constants import *
from fibbonachi_class import Fibbonachi


def exception(message: str):
    print(message)
    exit(-1)


def fibbonachi_algorithm(batch: list, criteria: float) -> list:
    next_one = 0
    try:
        next_one = batch[-1] + batch[-2]
    except IndexError:
        exception(NOT_ENOUGH_DATA)
    if next_one < criteria:
        batch.append(next_one)
        return fibbonachi_algorithm(batch, criteria)
    else:
        return batch


to_float = lambda item: float(item)

try:
    with open(INPUT_FILE) as file:
        input_data = file.readline().split()
except FileNotFoundError:
    exception(FILE_NOT_FOUND)

input_data = [to_float(i) for i in input_data]

try:
    with open(CRITERIA_FILE) as file:
        criteria = to_float(file.read())
except FileNotFoundError:
    exception(FILE_NOT_FOUND)
except TypeError:
    exception(INCORRECT_TYPE)

try:
    with open(OUTPUT_FILE, APPEND_MODE) as file:
        file.write("This is function response: " + str(fibbonachi_algorithm(input_data, criteria)) + NEXT_LINE)
except Exception:
    exception(SOMETHING_WENT_WRONG)

# Class
f_class = Fibbonachi(input_data, criteria)
output = f_class.fibbonachi_algorithm([])

try:
    with open(OUTPUT_FILE, APPEND_MODE) as file:
        file.write("This is class response: " + str(output) + NEXT_LINE)
except Exception:
    exception(SOMETHING_WENT_WRONG)
